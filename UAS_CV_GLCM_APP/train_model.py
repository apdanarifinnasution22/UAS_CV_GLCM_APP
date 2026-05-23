import os
import cv2
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from collections import Counter
from glcm_feature import extract_glcm_features

def train_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(BASE_DIR, "dataset")

    X, y = [], []

    for label in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, label)
        if os.path.isdir(class_path):
            for file in os.listdir(class_path):
                if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                    img_path = os.path.join(class_path, file)
                    image = cv2.imread(img_path)
                    if image is not None:
                        features = extract_glcm_features(image)
                        X.append(features)
                        y.append(label)

    if len(X) == 0:
        raise ValueError("Dataset kosong atau tidak ditemukan gambar yang valid.")

    counts = Counter(y)
    use_stratify = all(v >= 2 for v in counts.values())

    if use_stratify:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
    else:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

    model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))

    return model, acc, len(X)
