"""
Author : Joel Garcia (@Newtoniano20 / Newtoniano#1173 on discord)
This code was created for the Project Shaking Hands Overseas with the purpouse of moving a hand from the other side
of the ocean. Any questions feel free to ask.
"""

from requests.models import Response
from serial import Serial
from requests import post
from time import sleep

# SERIAL PORT: Windows = COM1, COM2, ... / Linux = /dev/ttyACM0, /dev/ttyACM1,...
SERIAL_PORT = "COM3"

# API URL FOR SENDING DATA
URL = 'https://lqinkt.deta.dev/servo'

#ARDUINO SERIAL BAUDRATE
BAUDRATE = 9600

def arduino_read():
    ser.write(bytes("A", 'utf-8'))
    return ser.readline() 

def split_data(data):
    return data.split()

def arduino_connect():
    return Serial( SERIAL_PORT , BAUDRATE) #Initializes the connection with the arduino, you will need to chose your serial port

def Post_req(URL, post_request):
    return post(url=URL, json=post_request)

try:
    ser = arduino_connect()
except:
    raise Exception(f"[ERROR] Arduino not connected to Serial port {SERIAL_PORT}")

sleep(0.5) 
while True:
    try:
        #reads the data from the arduino
        data = split_data(arduino_read())
        print(data)
    except:
        print(f"[ERROR] Arduino not connected to port {SERIAL_PORT}")
        ser = arduino_connect()
    post_request = { "s1": int(data[0]), "s2": int(data[1]), "s3": int(data[2]), "s4": int(data[3]),"s5": int(data[4]) }
    #sends the data to our API and prints the answser. If the response is 200, it means the deta was sent succesfull
    try:
        Req_Response = Post_req(URL=URL, post_request=post_request)
        print(Req_Response)
    except:
        print(f"[ERROR] Server {URL} not responding to request")
