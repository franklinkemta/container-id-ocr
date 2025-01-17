from ultralytics import YOLO

from config import Config
from util import crop_bbox


class Detector:
    name = "detection-step"

    def __init__(self, model=Config.MODEL_PATH, **kwargs):
        self.model = YOLO(model=model, task=Config.MODEL_TASK, **kwargs)
        self.conf = {}
        self.classes = Config.get_classes()

        if Config.SAVE_CROP:
            Config.create_path(Config.CROP_DIR)

    def detect(self, image, stream=False, conf=Config.MODEL_CONF, **kwargs):
        results = self.model(image, stream=stream, conf=conf, **kwargs)

        for result in results:
            # label = result[0]
            if Config.SAVE_CROP:
                crop_bbox(image, result.boxes, Config.CROP_DIR)
                # result.save(filename="result_boxes.jpg")
                # result.show()

        return results, image
