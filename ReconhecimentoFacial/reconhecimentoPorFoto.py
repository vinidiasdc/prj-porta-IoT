import face_recognition as fr
from engine import reconhecerFace, consultar_rostos

desconhecido = reconhecerFace("vinicius2.jpg")

if(desconhecido[0]):
    rosto_desconhecido = desconhecido[1][0]
    rostos_conhecidos, nome_dos_rostos = consultar_rostos()

    resultados = fr.compare_faces(rostos_conhecidos, rosto_desconhecido)
    print(resultados)

else:
    print("Nenhum rosto foi encontrado!!")