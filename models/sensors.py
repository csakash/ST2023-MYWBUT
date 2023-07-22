class Sensor():
    def __init__(self, name, record_date):
        self.name = name
        self.__location = "Kolkata"
        self.record_date = record_date
        self.data = {}

    def get_location(self):
        print("Location of sensor is: ", self.__location)

    def set_location(self, new_location):
        self.__location = new_location
        print("The new location is: ", self.__location)

    def add_data(self, time, data):
        self.data['time'] = time
        self.data['data'] = data
        print(f'We have {len(data)} points saved')

    def clear_data(self):
        self.data = {}
        print('Data cleared!')


class Accelerometer(Sensor):
    def __init__(self, name, location, record_date, brand):
        super().__init__(name, location, record_date)
        self.brand = brand

