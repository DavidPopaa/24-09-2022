import serial.tools.list_ports

ports= serial.tools.list_ports.comports()
serialInst=serial.Serial()
portsList=[]

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val=input("select port: COM")

for x in range(0, len(portsList)):
    if portsList[x].startswith("COM"+str(val)):
        portVar="COM"+str(val)
        print(portsList[x])
serialInst.baudrate=9600
serialInst.port=portVar
serialInst.open()
i = 0
dist = []
while i <= 3:
    if serialInst.in_waiting:
        packet=serialInst.readline()
        print(packet.decode("utf-8"))
        data = packet.decode("utf-8")
        for s in data.split():
            try:
                dist.append(float(s))
            except ValueError:
                pass 
        i = i + 1

print(dist)