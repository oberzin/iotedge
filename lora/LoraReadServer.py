import json

import socket
from time import sleep

import requests

import cgi
import random
import time
import sys


def run():

    TCP_IP = '0.0.0.0'
    TCP_PORT = 50005
    BUFFER_SIZE = 500  # Normally 1024, but we want fast response

    # LOC_SRV = "172.23.66.10"
    # LOC_SRV_PORT = 30808
    # device_name = "192.0.2.1"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((TCP_IP, TCP_PORT))

    # sock.listen(1)
    # conn, addr = sock.accept()

    while 1:
        sock.listen(1)
        print ( "Listening" )
        conn, addr = sock.accept()
        print ( 'Connection address:', addr )
        data = conn.recv(BUFFER_SIZE)
        # if not data: return
        print ( "received data:", data )
        jData = json.loads(data)
        print ( jData )
        appData =jData["pdu"]
        print ( appData )
        tempData = appData[12:16]
        print ( tempData )
        tempDataDec = int(tempData, 16 ) /10
        tempDataDecF = tempDataDec * 1.8 + 32

        humidData = appData[20:22]
        print ( humidData )
        humidDataDec = int(humidData, 16 ) /2

        pressData = appData[4:8]
        print ( pressData )
        pressDataDec = int(pressData, 16 ) /10
        device_eui = jData["devEui"]
        txtime = jData["txtime"]
        # print "\nAppData: %s" % appData
        # print "\nTemperature in Celsius: %s" % tempDataDec
        # print "\nTemperature in Fahrenheit: %s" % tempDataDecF
        # print "\nHUMIDITY Percents: %s" % humidDataDec
        # print "\nBAROMETRIC PRESSURE in Millibars: %s" % pressDataDec
        # print "\nDevice EUI: %s" % device_eui

        # payld = json.dumps({'Device EUI': device_eui, 'Temperature': tempDataDecF, \
        #                     'Humidity': humidDataDec, 'Pressure': pressDataDec, 'Count': LORA_READ_COUNT})


    #     location = get_location(LOC_SRV, LOC_SRV_PORT, device_name)
    #
    #     print location["userInfo"]["locationInfo"]
    #
    # lat = location["userInfo"]["locationInfo"]["latitude"]
    # lon = location["userInfo"]["locationInfo"]["longitude"]
    # alt = location["userInfo"]["locationInfo"]["altitude"]

    # packet = json.dumps({'TIMESTAMP': txtime, 'Device EUI': device_eui, 'Temperature': tempDataDecF, \
    #                      'Humidity': humidDataDec, 'Pressure': pressDataDec, \
    #                      'Latitude': lat, 'Longitude': lon, 'Altitude': alt})

        packet = json.dumps({'TIMESTAMP': txtime, 'Device EUI': device_eui, 'Temperature': tempDataDecF, \
                  'Humidity': humidDataDec, 'Pressure': pressDataDec})

        print ( packet )

# iot_hub_message = IoTHubMessage(packet)
# # iot_hub_message = IoTHubMessage(json.dumps(packet))
# hub_manager.forward_event_to_output("output1", iot_hub_message, 0)
# print('sent!')

# conn.close()

if __name__ == "__main__":
    run()
