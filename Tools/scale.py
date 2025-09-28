def size(width, height, w, h):
        sf_x = 100 / width
        sf_y = 100 / ((width /height) * height)
        
        w = int(w / sf_x)
        h = int(h / sf_y)
        
        return w, h

def pos(width, height, x, y, size_w, size_h):
        sf_x = 100 / width
        sf_y = 177.7 / ((width /height) * height)
        
        x = int(x / sf_x) - int(size_w / 2)
        y = int(y / sf_y) - int(size_h / 2)
        
        return x, y