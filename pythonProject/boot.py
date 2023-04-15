from machine import Pin
import network, esp, gc

gc.collect()
esp.osdebug(None)

ssid = "WANESSA OI FIBRA 2.4G"
password = "wanejunior"
password = "wanejunior"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Conexão bem-sucedida")
print(station.ifconfig())



