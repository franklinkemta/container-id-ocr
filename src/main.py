import cv2

from config import Config
from steps.detection import Detector
from steps.ocr import OCR


def detect_and_crop():
    detector = Detector()

    skip_dirs = [
        "2",
        "3",
        "4",
        "5",
        "6",
    ]  # my test images inputs folder is sorted this way
    inputs_images = Config.load_images(Config.INPUT_PATH, skip_dirs=skip_dirs)

    i = 0
    while i < len(inputs_images):
        im = cv2.imread(inputs_images[i])

        # core steps
        # detection, remove classes=detector.classes to use coco classes
        res, im = detector.detect(im)

        if Config.SHOW_OUTPUT:
            cv2.imshow(f"image {i} - press (n) for next, (q) to quit", im)
            key = cv2.waitKey(0) & 0xFF
            if key == ord("n"):
                cv2.destroyAllWindows()
            elif key == ord("q"):
                break

        i += 1

    if Config.SHOW_OUTPUT:
        cv2.destroyAllWindows()


def read_ocr():
    ocr_reader = OCR()

    cropped_images = Config.load_images(Config.CROP_DIR)

    results = ocr_reader.read_all(cropped_images)

    # print(results)


if __name__ == "__main__":
    # detect_and_crop()
    read_ocr()
