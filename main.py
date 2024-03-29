import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print (str(onePort))

val = 7

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print (portList[x])
# portVar = "com8"
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
packet2 = ""
while True:
    if serialInst.inWaiting():
        packet = serialInst.readline()
        # print(packet.decode('utf').rstrip('\n'))
        packet2 = (packet.decode('utf').rstrip('\n'))
        print(packet2)
        # packet2 = packet.decode('utf')

        if packet2 == '===nothing moves':
            print("no movement found")
        if packet2 == "Motion detected":
            print("Motion is detected")
# def trial():
#     while True:
#         if serialInst.inWaiting():
#             packet = serialInst.readline()
#             return packet
#             # print(packet.decode('utf').rstrip('\n'))

# x = trial()
# if x ==" == = nothing moves":
#     print("this is working")