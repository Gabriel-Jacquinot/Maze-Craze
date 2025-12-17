def size(width, height, w, h):
        sf_x = 100 / width # Scale factor of 100 compared to the window width
        sf_y = 100 / ((width /height) * height) # Getting the y postion in the same ratio as the x at a scale factor of 100 compared to the window height
        ### CHANGE TO 177.7 ###
        w = int(w / sf_x) # Divide the width of the object by the scale factor x
        h = int(h / sf_y) # Divide the height of the object by the scale factor y
        
        return w, h # Return the scaled values

def pos(width, height, x, y, size_w, size_h):
        sf_x = 100 / width # Scale factor of 100 compared to the window
        sf_y = (1600/ 9) / ((width /height) * height) # Getting the y postion in the same ratio as the x at a scale factor of 177.7 to acommodate for the resolution compared to the window height 
        
        x = int(x / sf_x) - int(size_w / 2) # Divide the width of the object by the scale factor x
        y = int(y / sf_y) - int(size_h / 2) # Divide the height of the object by the scale factor y 
        
        return x, y # Return the scaled values