from time import time

import cv2


class Camera(object):
    def __init__(self):
        ext = '.jpg'
        self.frames = [open(f + ext, 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frames[int(time()) % len(self.frames)]


class LaptopCamera(object):
    def __init__(self):
        pass

    def get_frame(self):
        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite("video.jpg", image)
        camera.release()
        return open("video.jpg", 'rb').read()