import cv2
import torch
from yolov5.detect import run
import warnings

warnings.filterwarnings('ignore')

def run_detection(source):
    print("DETECTANDO......")
    results = run(
        weights='best.pt',
        source=source,
        imgsz=[640,640],
        conf_thres=0.5,
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )
    return results

if __name__ == "__main__":
    tipoDetection = input("Informe 1 para detectar objeto cortante em IMAGEM ou 2 para VIDEO: ")
    nameFile = input("Informe o nome do arquivo: ")
    
    if tipoDetection == '1': # Para imagem
        run_detection(f'./data/images/{nameFile}') #img-teste-faca.jpg
    elif tipoDetection == '2': #Para vídeo
        cap = cv2.VideoCapture(f'./data/videos/{nameFile}') #video2.mp4
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = run_detection(frame)
            # Processar resultados
        cap.release()
    else:
        print(f'Parâmetros incorretos: tipo: {tipoDetection} - arquivo: {nameFile}')