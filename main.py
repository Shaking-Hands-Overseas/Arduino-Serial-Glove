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
SERIAL_PORT = "COM6"

# API URL FOR SENDING DATA
URL = 'https://xlbi6e.deta.dev/servo'

# ARDUINO SERIAL BAUDRATE
BAUDRATE = 9600


def arduino_read():
    """
    Reads data from arduino
    :return: String
    """
    ser.write(bytes("A", 'utf-8'))
    return ser.readline() 


def split_data(raw_data: str):
    """
    Splits data into a list
    :param raw_data: String
    :return: List
    """
    return raw_data.split()


def arduino_connect():
    """
    Initializes the connection with the arduino, you will need to chose your serial port
    :return: Serial
    """
    return Serial(SERIAL_PORT, BAUDRATE)


def post_req(url, req):
    return post(url=url, json=req)


try:
    ser = arduino_connect()

except:
    raise Exception(f"[ERROR] Arduino not connected to Serial port {SERIAL_PORT}")

sleep(0.5) 
while True:
    try:
        """
        Reads the data from the arduino
        """
        data = split_data(arduino_read())
        print(data)
    except:
        print(f"[ERROR] Arduino not connected to port {SERIAL_PORT}")
        ser = arduino_connect()
    try:
        post_request = {"s1": int(data[0]), "s2": int(data[1]), "s3": int(data[2]), "s4": int(data[3]),"s5": int(data[4])}
    except:
        pass
    try:
        """
        Sends the data to our API and prints the answser. If the response is 200, it means the deta was sent succesfullq
        """
        Req_Response = post_req(url=URL, req=post_request)
        print(Req_Response)
    except:
        print(f"[ERROR] Server {URL} not responding to request")
