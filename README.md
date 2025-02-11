# hackaton
Projeto final Hackaton FIAP

## Modelo YOLOv5
https://github.com/ultralytics/yolov5/

## Datasets e Images
https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F04ctx
https://universe.roboflow.com/ai-zone/weapon-detection-rylag-rtqjy/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true

#### Fontes de pesquisa
https://iaexpert.academy/2020/10/13/deteccao-de-objetos-com-yolo-uma-abordagem-moderna/


### Como executar o projeto
- Python 3.8 ou superior
- git clone https://github.com/motoca/hackaton.git
- cd yolov5
- pip install -r requirements.txt
- python detect.py

### Tempo de execução do treinamento
- 100 epochs completed in 14.262 hours.
- Optimizer stripped from mps_train/exp7/weights/last.pt, 14.5MB
- Optimizer stripped from mps_train/exp7/weights/best.pt, 14.5MB

Validating mps_train/exp7/weights/best.pt...
Fusing layers... 
Model summary: 157 layers, 7023610 parameters, 0 gradients, 15.8 GFLOPs
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100%|██████████| 5/5 [00:29<00:00, 
                   all        158         76     0.0849      0.105     0.0434     0.0112
                 knife        158         76     0.0849      0.105     0.0434     0.0112