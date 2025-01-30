import cv2
import torch
from yolov5.detect import detect

def run_detection(source):
    print("DETECTANDO......")
    results = detect(
        weights='best.pt',
        source=source,
        imgsz=640,
        conf_thres=0.5,
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )
    return results

# Para imagem
run_detection('input_image.jpg')

# Para vídeo
cap = cv2.VideoCapture('input_video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = run_detection(frame)
    # Processar resultados
cap.release()