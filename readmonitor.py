import serial.tools.list_ports
import tkinter as tk
from tkinter import *
from tkinter import messagebox
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
serialInst.baudrate = 9600
serialInst.port = "COM8"
serialInst.open()

def btnon():
        command = "ON"
        serialInst.write(command.encode('utf-8'))

def btnoff():
    command = "OFF"
    serialInst.write(command.encode('utf-8'))

def sensor():
    command = "sensor mode on"
    serialInst.write(command.encode('utf-8'))

# if serialInst.inWaiting():
#         packet = serialInst.readline()
#         print(packet.decode('utf').rstrip('\n'))

# def light():
#
#     if serialInst.inWaiting():
#         packet = serialInst.readline()
#         # print(packet.decode('utf').rstrip('\n'))
#         return packet
root = Tk()
root.geometry("1920x1080")

on_btn = PhotoImage(file='on1.png')
off_btn = PhotoImage(file='off1.png')
sensor_btn = PhotoImage(file='sensor.png')
Button(root, image=on_btn, command=btnon).pack(pady=10)


Button(root, image=off_btn, command = btnoff).pack(pady = 10)


Button(root, image=sensor_btn, bd = '5', command = sensor).pack(pady = 10)

root.mainloop()
