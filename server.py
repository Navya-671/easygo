import socket
import json

UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP server started")

cell = {}

while True:
    data, addr = sock.recvfrom(1024)
    json_data = json.loads(data.decode())
    print("Received JSON data from {}: {}".format(addr, json_data))
    
    # Parse JSON data and store it in the 'cell' variable based on type
    sensor_type = json_data.get("sensor", None)
    if sensor_type:
        if sensor_type not in cell:
            cell[sensor_type] = json_data.get("ppm", None)
        else:
            # Update existing value for the sensor type
            cell[sensor_type] = json_data.get("ppm", None)
    
    # Access 'cell' dictionary as needed, e.g., cell["temperature"], cell["pressure"]
