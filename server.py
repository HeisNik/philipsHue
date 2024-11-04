import socket



# Tässä voisi olla Hue-luokan määritys, mutta se puuttuu alkuperäisestä koodista
from hue import HueHue

connections = []
# Luo verkkopalvelimen

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0',8001))
server.listen(5)

print("palvelin on nyt käynnistetty")
print("saat palvelimeen yhteyden telnetillä 'telnet localhost 8001'")

# Käsittelee yhteyksiä
def handle_client(client_socket):
    client_socket.settimeout(60)  # Aseta aikakatkaisu 60 sekuntiin
    client_socket.send("Commands are: HELP, ON, OFF\r\n".encode())  # Lähetä aloitusviesti

    while True:
        data = client_socket.recv(4096).decode()  # Vastaanota dataa yhteydeltä
        if not data:
            break
        
        print("received data", data)
        command = data.strip().split(" ")  # Pilko saatu data komponentteihin
        
        if command[0] == 'HELP':
            client_socket.send("Commands are: HELP, ON, OFF\r\n".encode())  # Lähetä avustusviesti
        elif command[0] == 'OFF':
            # Luo Hue-olio ja sammuta valot
            hue = HueHue()
            hue.lightsOff()
        elif command[0] == 'ON':
            # Luo Hue-olio ja laita valot päälle
            #aikaisemmin hue = Hue() ja hue = hue.HueHue näillä ei  toiminut
            hue = HueHue()
            hue.lightsOn()
        else:
            print("command not implemented")  # Tulosta viesti, jos komentoa ei ole määritelty
    
    client_socket.close()

while True:
    client_sock, addr = server.accept()  # Odota uutta yhteyttä
    print("user connected")
    connections.append(client_sock)
    handle_client(client_sock)  # Käsittele yhteyttä
    print("user disconnected")  # Tulosta viesti, kun käyttäjä katkaisee yhteyden
