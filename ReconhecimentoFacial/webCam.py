import numpy as np
import requests
import face_recognition as fr
import cv2
from engine import ConsultarRostosConhecidos

endereco_ip_webserver = '192.168.100.31'
porta = 80

def IniciarVigilancia():
    rostos_conhecidos = ConsultarRostosConhecidos()
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    
    while True:
        ret, frame = webcam.read()

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        localizacao_dos_rostos = fr.face_locations(rgb_frame)
        rosto_desconhecidos = fr.face_encodings(rgb_frame, localizacao_dos_rostos)

        for(top, right, bottom, left), rosto_desconhecido in zip(localizacao_dos_rostos, rosto_desconhecidos):
            
            resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
            print(resultados)

            if any(resultados):
                print("Acesso liberado")
                response = requests.get(f'http://{endereco_ip_webserver}:{porta}', 'servo=abrir')
                if response.status_code == 200:
                    print("Solicitação bem-sucedida!")
                else:
                    print("Algo falhou!")

            else:
                response = requests.get(f'http://{endereco_ip_webserver}:{porta}', 'servo=fechar')


        cv2.imshow("camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webcam.release()
    cv2.destroyAllWindows()