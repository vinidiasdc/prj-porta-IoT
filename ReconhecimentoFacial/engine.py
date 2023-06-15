import face_recognition as fr
import datetime
import cv2
from conexao import CriarImagensPessoasAutorizadas, SalvarImagemNoBanco
    
def ConsultarRostosConhecidos():
    qtdImagens = CriarImagensPessoasAutorizadas()
    rostos_conhecidos = []

    for i in qtdImagens:
        arquivo_imagem = f"imagem_user_{i}.jpg"
        
        foto = fr.load_image_file(arquivo_imagem)
        encodeRosto = fr.face_encodings(foto)

        if(len(encodeRosto) > 0):
            rostos_conhecidos.append(encodeRosto[0])
    
    return rostos_conhecidos

def CadastrarRostoAutorizado():
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    while True:
        ret, frame = webcam.read()

        cv2.imshow("camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"imagem_{timestamp}.jpg"

    cv2.imwrite(nome_arquivo, frame)

    SalvarImagemNoBanco(nome_arquivo)

    webcam.release()
    cv2.destroyAllWindows()


