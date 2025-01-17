import os
import time

import cv2

from config import CLASSES_LABELS


def crop_bbox(image, boxes, crop_dir):
    for box in boxes:
        xyxy = box.xyxy[0].cpu().numpy().astype(int)
        class_id = int(box.cls[0].cpu().numpy().astype(int))
        conf = box.conf[0].cpu().numpy().astype(float)

        if class_id not in CLASSES_LABELS:
            print(f"crop_bbox: skipped class {class_id}")
            continue

        label = CLASSES_LABELS[class_id]
        timestamp = str(int(time.time() * 1000))

        x_min, y_min, x_max, y_max = xyxy
        cropped_image = image[y_min:y_max, x_min:x_max]

        cv2.imwrite(
            os.path.join(crop_dir, f"{label}_{class_id}_{conf:0.2f}_{timestamp}.jpg"),
            cropped_image,
        )
