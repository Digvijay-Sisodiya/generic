def crop_image(image, x, y, w, h):
        """
        TODO: Add this to image operations 
        Crop the input image to the specified region defined by the (x, y) coordinates of the top-left corner and the width and height of the rectangle.
        """
        return image[y:y+h, x:x+w]

