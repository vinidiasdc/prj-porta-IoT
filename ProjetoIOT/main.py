from machine import Pin
import usocket as socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#Interagir com o ESP8266
led = Pin(4, Pin.OUT)

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

    #Requisição do LED
    if "GET /?led=on" in request:
        led.value(1)
    if "GET /?led=off" in request:
        led.value(0)
    led_status = ("OFF", "ON")[led.value()==1]
    response = web_page() % led_status

    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Content-type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()