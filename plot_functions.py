def line_plot(ts, x_func, y_func, image):
    for i, t in enumerate(ts):
        # Equation
        x = x_func(t)
        y = y_func(t)
        # FP coordinates
        coord = (x, y)
        # Convert to image coordinates (do it nicer)
        coord_int = (int((coord[0]/2+1)*(SIZE/2-1)), int((coord[1]/2+1)*(SIZE/2-1)))
    
        image[coord_int[0], coord_int[1]] = 255
        # Update image
        #if i>50000:
        #    if image[coord_int[0], coord_int[1]] <= 255-10:
        #        image[coord_int[0], coord_int[1]] += 5
        # Add frame to video
        if i%50==0:
            #video_writer.write(image)
            #cv2.imwrite("itr_"+str(i)+".png", image)
            cv2.imshow("out", image)
            cv2.waitKey(1)
    return image