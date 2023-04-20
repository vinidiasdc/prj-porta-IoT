from machine import Pin, PWM
import time
import usocket as socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#Interagir com o ESP8266
led = Pin(4, Pin.OUT)
servo = PWM(Pin(5), freq=50)
status = False

def GirarServo(pulso):
    servo.duty(pulso)


def web_page():
    file = open("index.html", "r")
    page = file.read()
    file.close()
    return page

while True:
    conn, addre = s.accept()
    request = conn.recv(1024)
    request = str(request)
    print(request)

    #Requisição do Servo e Led

    if "GET /?servo=on" in request:
        if status == False:
            for i in range(90, 115, 1):
                GirarServo(i)
                time.sleep_ms(10)

        status = True
        GirarServo(0)


    if "GET /?servo=off" in request:
        if status == True:
            for i in range(115, 90, -1):
                GirarServo(i)
                time.sleep_ms(10)

            status = False
        GirarServo(0)

    response = web_page()

    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()