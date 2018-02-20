import cv2


class Recorder:
    def __init__(self, output, camera_url, fps):
        self.stream = cv2.VideoCapture(camera_url)
        width = self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.recorder = cv2.VideoWriter(output, cv2.VideoWriter_fourcc(*'XVID'), fps, (int(width), int(height)))

    def record(self):
        ret, frame = self.stream.read()
        self.recorder.write(frame)
