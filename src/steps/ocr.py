import easyocr

from config import Config
from util import validate_asset_id


class OCR:
    def __init__(self, languages=["en"]):
        self.reader = easyocr.Reader(languages)
        self.valid_results = {}
        self.invalid_results = []

    def read(self, image_path: str):
        value = self.reader.readtext(image_path)

        for xyxy, text, conf in value:
            _value = {"xyxy": xyxy, "conf": conf, "file": image_path}

            if validate_asset_id(text):
                self.valid_results[text] = _value
            else:
                self.invalid_results.append(_value)

    def read_all(self, images_path: list[str]):
        self.valid_results = {}

        for image_path in images_path:
            self.read(image_path)

        return self.valid_results.copy()
