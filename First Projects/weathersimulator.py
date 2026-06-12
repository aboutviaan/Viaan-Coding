import random
import time

def generate_weather():
    temperature = random.randint(40, 100)
    humidity = random.randint(20, 100)
    wind_speed = random.randint(0, 30)

    if temperature > 85:
        status = "Hot"
    elif temperature >= 70:
        status = "Warm"
    else:
        status = "Cool"

    print("--------------------")
    print("Weather Report")
    print("--------------------")
    print("Temperature:", temperature, "°F")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "mph")
    print("Status:", status)

    if temperature > 95:
        print("WARNING: Extreme Heat!")

    if wind_speed > 25:
        print("WARNING: High Winds!")

    print()

print("Raspberry Pi Weather Station")
print("Starting sensors...")
print()

time.sleep(2)

for reading in range(1, 6):
    print("Reading #", reading)
    generate_weather()
    time.sleep(2)

print("Weather monitoring complete!")