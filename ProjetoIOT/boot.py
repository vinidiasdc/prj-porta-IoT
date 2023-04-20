import network, esp, gc

gc.collect()
esp.osdebug(None)

ssid = "iPhone de Fabricio"
password = "fabricio"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print("Conexão bem-sucedida")
print(station.ifconfig())