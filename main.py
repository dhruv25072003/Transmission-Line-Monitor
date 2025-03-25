import time
import random
import requests

# ThingSpeak settings
API_KEY = "2PZ622HI7XND111T"  # Replace with your ThingSpeak Write API Key
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def send_to_thingspeak(voltage, current):
    url = f"{THINGSPEAK_URL}?api_key={API_KEY}&field1={voltage}&field2={current}"
    try:
        response = requests.get(url)
        print("Data sent to ThingSpeak! Response:", response.text)
    except Exception as e:
        print("Error sending data:", e)

# Main loop
print("Starting Transmission Line Monitoring...")
while True:
    voltage = random.uniform(200, 240)  # Simulated voltage (200–240V)
    current = random.uniform(5, 15)     # Simulated current (5–15A)
    print(f"Voltage: {voltage:.2f} V, Current: {current:.2f} A")
    send_to_thingspeak(voltage, current)
    time.sleep(20)  # Wait 20 seconds