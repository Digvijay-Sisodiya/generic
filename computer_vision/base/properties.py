import cv2
import os


class ImageProperties:
    def __init__(self, filename):
        self.filename = filename
        self.image = None
        self.width = 0
        self.height = 0
        self.format = ''

class GetImageProperties(ImageProperties):
    def __init__(self, filename):
        ImageProperties.__init__(self, filename)

    def get_image(self):
        self.image = cv2.imread(self.filename)
        self.filename = (self.filename.split(os.sep))[-1]
        return self.image, self.filename

    def get_image_size(self):
        """
        TODO: Add check with exception
        """
        if self.image is not None:
            self.height, self.width = self.image.shape[:2]
            return self.height, self.width

    def get_dimensions(self):
        return (self.width, self.height)

    def get_format(self):
        self.format = self.filename.split('.')[-1]
        return self.format