# Hackaton - Detecção de Materiais Cortantes
Projeto final FIAP - IA PARA DEVS


****
### Grupo 12
#### Componentes
* Silas Pereira Costa - RM355822
* Wesley Gomes Santos - RM355677


## Modelo pré treinado utilizado - YOLOv5x
https://github.com/ultralytics/yolov5/

## Fluxo utilizado para o desenvolvimento da solução
1 - Seleção das imagens e preparação do DATASET no formado to YOLO
*     - dataset
        - weapons
           - images
              - train
              - test
              - val
          - labels
              - train
              _ test
              _ val
  
2 - Iniciamos o projeto com o modelo YOLOv5s e posteriormente mudamos para o YOLOv5x, que se mostrou mais performático

3 - Configurar os arquivos de execução do YOLO para personalizar a execução de acordo com as necessidades do projeto

4 - Realizar o treinamento do modelo utilizando o DATASET selecionado

5 - Executar a detecção de objetos cortantes utilizando o novo modelo treinado com as imagens do DATASET
     ***/yolov5/runs/train/weapon_detection/weights***

6 - Realizar testes com imagens e videos

7 - Implementar a notificação quando um objeto for identificado e encaminhar por e-mail

8 - Gerar a pasta de resultados com o arquivo de saída.

9 - Video de apresentação do projeto (https://youtu.be/qztjWx1qC34)

## Datasets e Images
https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F04ctx

https://universe.roboflow.com/ai-zone/weapon-detection-rylag-rtqjy/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true


#### Fontes de pesquisa
https://iaexpert.academy/2020/10/13/deteccao-de-objetos-com-yolo-uma-abordagem-moderna/


### Como executar o projeto
Usar o arquivo hachaton-final.ipynb no Google Collab

### Tempo de execução do treinamento
with torch.cuda.amp.autocast(amp):
     99/99      16.2G    0.02122   0.005528  7.294e-05         13        640: 100% 493/493 [01:45<00:00,  4.67it/s]
                Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 5/5 [00:01<00:00,  4.46it/s]
                  all        158         76       0.92      0.604       0.68      0.437

100 epochs completed in 3.049 hours.
Optimizer stripped from runs/train/exp/weights/last.pt, 173.2MB
Optimizer stripped from runs/train/exp/weights/best.pt, 173.2MB

Validating runs/train/exp/weights/best.pt...
Fusing layers... 
Model summary: 322 layers, 86200330 parameters, 0 gradients, 203.8 GFLOPs
                 Class     Images  Instances          P          R      mAP50   mAP50-95: 100% 5/5 [00:01<00:00,  3.17it/s]
                   all        158         76      0.868      0.603      0.702      0.443
                 knife        158         76      0.868      0.603      0.702      0.443
Results saved to runs/train/exp
