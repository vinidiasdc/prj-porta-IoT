import face_recognition as fr

def reconhecerFace(urlfoto):
    foto = fr.load_image_file(urlfoto)
    rostos = fr.face_encodings(foto)

    if(len(rostos) > 0):
        return True, rostos
    else:
        return False, []
    
vinicius = reconhecerFace("vinicius.jpg")

def consultar_rostos():
    rostos_conhecidos = []
    nome_dos_rosotos = []

    if(vinicius[0]):
        rostos_conhecidos.append(vinicius[1][0])
        nome_dos_rosotos.append("Vinicius")

    return rostos_conhecidos, nome_dos_rosotos
