import cv2

def img_inc(image, coordinates, val):
    if image[coordinates] <= 255-val:
        image[coordinates] += val

def img_set(image, coordinates, val):
    image[coordinates] = val

def line_plot(ts, x_func, y_func, image, video_writer=None, im_show = False, incremental = False):
    
    assert(image.shape[0] == image.shape[1])
    
    for i, t in enumerate(ts):
        # Equation
        x = x_func(t)
        y = y_func(t)

        # FP coordinates
        coord = (x, y)
        # Convert to image coordinates (do it nicer)
        coord_int = (int((coord[0]/2+1)*(image.shape[0]/2-1)), int((coord[1]/2+1)*(image.shape[0]/2-1)))

        # Update image
        if incremental:
            if i > 5000: # first few lines are too strong
                img_inc(image, (coord_int[0], coord_int[1]), 5)
        else:
            img_set(image, (coord_int[0], coord_int[1]), 255)

        # Display stuff
        if i%7000==0:
            if video_writer:
                video_writer.write(image)
            if im_show:
                cv2.imshow("out", image)
                cv2.waitKey(1)
    return image