from time import time


class Camera(object):
    def __init__(self):
        ext = '.jpg'
        self.frames = [open(f + ext, 'rb').read() for f in ['1', '2', '3']]

    def get_frame(self):
        return self.frames[int(time()) % len(self.frames)]
