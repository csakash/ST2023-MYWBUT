from models.sensors import Sensor, Accelerometer

sensor = Sensor(name="Private Sensor", record_date="2023-07-12")
sensor2 = Sensor(name="Gyroscope", record_date="2023-04-05")
print(sensor.name, sensor.record_date)
# print(sensor.__location)
sensor.get_location()
sensor.set_location(new_location="Hyderabad")