import numpy as np
import math
import cv2

class Tile:
    ANGLES = [math.radians(alpha) for alpha in [36, 108]]
    ROTMATS = [np.array([[math.cos(alpha), -math.sin(alpha)],[math.sin(alpha), math.cos(alpha)]]) for alpha in ANGLES]

    def __init__(self, type, A, B, C=-1, dir=1) -> None:
        self.type = type
        self.alpha = self.ANGLES[self.type]
        self.dir = dir
        self.rotmat = self.ROTMATS[self.type].copy()
        if dir == -1:
            self.rotmat[0][1] = -1*self.rotmat[0][1]
            self.rotmat[1][0] = -1*self.rotmat[1][0]
        self.A = np.array(A)
        self.B = np.array(B)
        self.C = self.calc_c() if isinstance(C, int) else C

    def calc_c(self):
        AB =  self.B - self.A
        AC = self.rotate(AB)
        C = self.A + AC
        return C
        
    def rotate(self, v):
        out = self.rotmat@v
        return out

    def get_coords(self):
        A = (int(self.A[0]), int(self.A[1]))
        B = (int(self.B[0]), int(self.B[1]))
        C = (int(self.C[0]), int(self.C[1]))
        coords = np.array([A,B,C])
        return coords

class TilesSet:
    GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

    def __init__(self) -> None:
        self.tiles = []
    def add_tile(self, tile):
        self.tiles.append(tile)
    def divide(self):
        tmp_tiles = []
        for tile in self.tiles:
            if tile.type == 0:
                # Type 0 division
                P = tile.A + ((tile.B - tile.A) / self.GOLDEN_RATIO)
                tmp_tiles.append(Tile(0, tile.C, P, dir=tile.dir))
                tmp_tiles.append(Tile(1, P, tile.C, dir=tile.dir))
            else:
                # Type 1 division
                Q = tile.B + ((tile.A - tile.B) / self.GOLDEN_RATIO)
                R = tile.B + ((tile.C - tile.B) / self.GOLDEN_RATIO)
                tmp_tiles.append(Tile(0, R, Q, dir=-1*tile.dir))
                tmp_tiles.append(Tile(1, R, tile.C, dir=tile.dir))
                tmp_tiles.append(Tile(1, Q, R, dir=-1*tile.dir))
        self.tiles = tmp_tiles

def draw_tiles(img, tiles):
    for tile in tiles:
        
        coords = tile.get_coords()
        color = (31,89,37) if tile.type else (60,140,129)
        cv2.drawContours(img, [coords], 0, color, -1)
        cv2.line(img, coords[0], coords[1], (22,22,22), 1)
        cv2.line(img, coords[0], coords[2], (22,22,22), 1)

        #cv2.circle(image, coords[0], 2, (0,0,255), -1)
        #cv2.circle(image, coords[1], 2, (0,255,0), -1)

tiles = TilesSet()
r = 400; cx = 400; cy = 400
for i in range(5):
    alpha = i * (2*math.pi/5)
    tile1 = Tile(0, [cx,cy], [cx+r*math.sin(alpha), cy+r*math.cos(alpha)])
    tile2 = Tile(0, [cx,cy], [cx+r*math.sin(alpha), cy+r*math.cos(alpha)], dir=-1)
    tiles.add_tile(tile1)
    tiles.add_tile(tile2)

for i in range(0, 8):
    image = np.zeros((800,800,3), dtype=np.uint8)
    draw_tiles(image, tiles.tiles)
    tiles.divide()
    cv2.imshow("image", image)
    cv2.imwrite("image.png", image)
    cv2.waitKey(-1)