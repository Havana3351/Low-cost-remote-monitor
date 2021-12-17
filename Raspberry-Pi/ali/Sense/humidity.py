from sense_hat import SenseHat

sense = SenseHat()

humidity = sense.get_humidity()

print("Humidity:%s %%rH"% humidity)

sense.show_message(str(sense.humidity))