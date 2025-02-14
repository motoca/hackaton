# Hackaton - Detecção de materiais cortantes
Projeto final FIAP - IA PARA DEVS


****
### Grupo 12
#### Componentes
* Silas Pereira Costa - RM355822
* Wesley Gomes Santos - RM355677


## Modelo pré treinado utilizado - YOLOv5x
https://github.com/ultralytics/yolov5/

## Fluxo utilizado para o desenvolvimento da solução
*1 - Seleção das imagens e preparação do DATASET no formado to YOLO
     - dataset
        - weapons
           - images
              - train
              - test
              - val
          - labels
              - train
              _ test
              _ val
  
*2 - Iniciamos o projeto com o modelo YOLOv5s e posteriormente mudamos para o YOLOv5x, que se mostrou mais performático

*3 - Configurar os arquivos de execução do YOLO para personalizar a execução de acordo com as necessidades do projeto
*4 - Realizar o treinamento do modelo utilizando o DATASET selecionado
*5 - Executar a detecção de objetos cortantes utilizando o novo modelo treinado com as imagens do DATASET
     ***/yolov5/runs/train/weapon_detection/weights***
*6 - Realizar testes com imagens e videos
*7 - Implementar a notificação quando um objeto for identificado e encaminhar por e-mail
*8 - Exportar o modelo e publicar no Huggingface

## Datasets e Images
https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F04ctx
https://universe.roboflow.com/ai-zone/weapon-detection-rylag-rtqjy/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true


#### Fontes de pesquisa
https://iaexpert.academy/2020/10/13/deteccao-de-objetos-com-yolo-uma-abordagem-moderna/


### Como executar o projeto
- Python 3.8 ou superior
- git clone https://github.com/motoca/hackaton.git
- cd white_weapon_detection
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
