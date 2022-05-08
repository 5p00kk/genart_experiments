import cv2

def img_inc(image, coordinates, val):
    if image[coordinates] <= 255-val:
        image[coordinates] += val

def img_set(image, coordinates, val):
    image[coordinates] = val

def line_plot(ts, x_func, y_func, image, video_writer=None, im_show = False, incremental = False):
    
    assert(image.shape[0] == image.shape[1])
    frame_skip = 7000 if incremental else 50
    
    for i, t in enumerate(ts):
        # Equation
        x = x_func[0](t)
        y = y_func[0](t)

        # FP coordinates
        coord = (x, y)
        # FP coordinates (0,1)
        coord_norm = ((coord[0]-x_func[1])/x_func[2], (coord[1]-y_func[1])/y_func[2])
        # Make sure normalization went well
        assert(coord_norm[0]<=1 and coord_norm[0]>0)
        assert(coord_norm[1]<=1 and coord_norm[1]>0)
        # Image coordinates
        coord_int = (int(coord_norm[0]*(image.shape[0]-1)), int(coord_norm[1]*(image.shape[1]-1)))

        # Update image
        if incremental:
            if i > 15000: # first few lines are too strong
                img_inc(image, (coord_int[0], coord_int[1]), 5)
        else:
            img_set(image, (coord_int[0], coord_int[1]), 255)

        # Display stuff
        if i%frame_skip==0:
            if video_writer:
                video_writer.write(image)
            if im_show:
                cv2.imshow("out", image)
                cv2.waitKey(1)
    return image