import cv2 # Importando biblioteca 
import numpy as np

webcam = cv2.VideoCapture(0) #Inicia a captura de vídeo 

while True: #Inicia loop para a captação dos frames 
    ret, frame = webcam.read()

    range_start = np.array([100, 0, 0]) #Faixa que determina os tons de azul a serem detectados
    range_end = np.array([255, 255, 100])

    mask_blue = cv2.inRange(frame, range_start, range_end)
    mask_blue = cv2.medianBlur(mask_blue, 5) 

    frame[np.where(mask_blue > 0)] = [0, 0, 255] #Substitui a cor azul pela vermelha

    cv2.imshow("capture", frame) #Exibindo o frame modificado
    
    key = cv2.waitKey(1)
    
    if(key == ord('q')): 
        break
        
webcam.release() #Encerra a captura de vídeo
cv2.destroyAllWindows()