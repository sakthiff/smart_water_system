#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import serial
import requests
import json

# Configuration for the IoT sensor's serial connection
ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with your serial port
ser.timeout = 2  # Set a timeout for reading data

# Configuration for the data-sharing platform
platform_api_url = 'https://your-platform-api-url.com/data-endpoint'
api_key = 'your-api-key'

# Main loop for reading and sending data
while True:
    try:
        # Read data from the IoT sensor (adjust this based on your sensor's protocol)
        data = ser.readline().strip().decode('utf-8')

        # Create a data payload in JSON format
        payload = {
            'water_consumption': float(data)  # Assuming the sensor provides consumption in liters
        }

        # Add any additional data to the payload if needed

        # Send data to the data-sharing platform
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        response = requests.post(platform_api_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            print(f"Data sent successfully: {data}")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Close the serial connection when done
ser.close()

