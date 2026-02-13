import cv2
from ultralytics import YOLO
import torch

VIDEO_INDEX=0
MODEL_PATH="yolo26n.pt"
MODEL_CONF=0.70

def get_best_device():
    if torch.cuda.is_available():
        print("Using CUDA device")
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        print("Using MPS device")
        return torch.device("mps")
    print("Using CPU device")
    return torch.device("cpu")


cap = cv2.VideoCapture(VIDEO_INDEX)
model = YOLO(MODEL_PATH)
device = get_best_device()
model = model.to(device)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=MODEL_CONF, verbose=False)[0]
    annotated_frame = results.plot()

    cv2.imshow("YOLO Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
