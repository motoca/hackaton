import torch
from yolov5 import train, val
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
    
# Configurações
config = {
    'epochs': 30,
    'batch-size': 32,
    'img-size': 640,
    'data': 'weapons.yaml',
    'cfg': 'yolov5x.yaml',
    'weights': 'yolov5x.pt',
    'name': 'white-weapon_detection'
}

if __name__ == '__main__':
    train.run(**config)