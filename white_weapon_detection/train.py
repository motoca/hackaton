import torch
from yolov5 import train, val

# Configurações
config = {
    'epochs': 100,
    'batch-size': 16,
    'img-size': 640,
    'data': 'weapons.yaml',
    'cfg': 'yolov5s.yaml',
    'weights': 'yolov5s.pt',
    'name': 'weapon_detection'
}

if __name__ == '__main__':
    train.run(**config)