#!/usr/bin/env python3

# __author__      = "Saulius Lukse"
# __copyright__   = "Copyright 2019, Kurokesu"
# __license__     = "MIT"

import serial



def send_command(ser, cmd, echo=True):
    ser.write(bytes(cmd+"\n", 'utf8'))
    data_in = ser.readline().decode('utf-8').strip()
    if echo:
        print("")
        print("> "+cmd)
        print("< "+data_in)
    return data_in


ser = serial.Serial()
ser.port = '/dev/ttyACM0'              # Controller com port
ser.baudrate = 115200           # BAUD rate when connected over CDC USB is not important
ser.timeout = 5                 # max timeout to wait for command response

ser.open()
ser.flushInput()
ser.flushOutput()


# Read controller version strings
send_command(ser, "$S")

# Initialize controller
#send_command(ser, "$B2")
send_command(ser, "G91")

# Set limit switch
# send_command(ser, "M232 B1242 F2483")   # Focus
send_command(ser, "M232 A2000 B2000 C2000 E3000 F3000 G3000")   

# move zoom back, wait 0.5s, move forward and wait 0.5 again
# send_command(ser, "G0 A5000")
# send_command(ser, "G4 P500")
# send_command(ser, "G0 A5000")
# send_command(ser, "G4 P500")

# move focus back, wait 0.5s, move forward and wait 0.5 again
# send_command(ser, "G0 B5000")   # + = backwards, - = forwards
# send_command(ser, "G4 P5000")
# send_command(ser, "G0 B10000")
# send_command(ser, "G4 P5000")

send_command(ser, "!1")

# move iris back, wait 0.5s, move forward and wait 0.5 again
# send_command(ser, "G0 C-1000")
# send_command(ser, "G4 P500")
# send_command(ser, "G0 C1000")
# send_command(ser, "G4 P500")

# Set Day/Night fiter IR+VIS, wait 0.5s, move to VIS, wait 0.5s again
# send_command(ser, "M8")
# send_command(ser, "G4 P5000")
# send_command(ser, "M7")
# send_command(ser, "G4 P5000")
