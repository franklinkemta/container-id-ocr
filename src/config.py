import os

CLASSES_LABELS = {6: "train", 7: "container", 72: "refrigerator"}


class Config:
    MODEL_PATH = os.environ.get("MODEL_PATH", "yolov8m.pt")  # yolov8m
    MODEL_TASK = os.environ.get("MODEL_TASK", "predict")
    MODEL_CONF = float(os.environ.get("MODEL_CONF", 0.50))  # conf threshold
    SAVE_CROP = bool(os.environ.get("SAVE_CROP", True))
    CROP_DIR = os.environ.get("CROP_DIR", "runs")
    INPUT_PATH = os.environ.get(
        "INPUT_PATH",
        os.path.abspath(os.path.join(os.path.dirname(__file__), "inputs")),
    )
    SHOW_OUTPUT = bool(os.environ.get("SHOW_OUTPUT", False))

    def get_classes(labels_path="labels.txt") -> list[str]:
        labels = []
        with open(labels_path) as f:
            labels = f.read().splitlines()

        classes = [key for key, label in CLASSES_LABELS.items() if label in labels]

        return classes

    def create_path(path_to_create: str) -> None:
        os.makedirs(path_to_create, exist_ok=True)

    def load_images(path_to_load: str, skip_dirs=[]) -> list[str]:
        files_paths = []
        files_extensions = (".jpg", ".jpeg", ".webp", ".png")

        directories = [d for d in os.walk(path_to_load) if d not in skip_dirs]

        for root, _, files in directories:
            for file in files:
                if file.lower().endswith(files_extensions):
                    files_paths.append(os.path.join(root, file))

        return files_paths
