import os
import time

import cv2
import pandas as pd

from config import CLASSES_LABELS, Config


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


def validate_asset_id(id: str):
    if len(id) != 10:
        return False
    if not id[:4].isupper() or not id[:4].isalpha():
        return False
    if not id[4:].isdigit():
        return False
    return True


def create_inventory_list(ocr_results: dict[str, dict]):
    data = [
        {"asset_id": asset_id, "metadata": metadata}
        for asset_id, metadata in ocr_results.items()
    ]

    df = pd.DataFrame(data)
    df.to_csv(Config.INVENTORY_LIST_PATH, index=False)


def load_inventory_list(dir: str = Config.INVENTORY_LIST_PATH):
    if not os.path.exists(dir):
        print(f"load_inventory_list: {dir} does not exist.")
        return None

    df = pd.read_csv(dir)
    return df


def compare_inventory(inventory: pd.DataFrame, ocr_results: dict[str, dict]):
    missing_data = []

    for asset_id, metadata in ocr_results.items():
        if asset_id not in inventory["asset_id"].values:
            missing_data.append({"asset_id": asset_id, "metadata": metadata})

    missing_inventory = pd.DataFrame(missing_data)
    return missing_inventory
