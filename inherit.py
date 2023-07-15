class Sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, time, data):
        self.data['time'] = time
        self.data['data'] = data
        print(f'We have {len(data)} points saved')

    def clear_data(self):
        self.data = {}
        print('Data cleared!')

import numpy as np

sensor1 = Sensor(name='sensor1', location='Berkeley', record_date='2019-01-01')
data = np.random.randint(-5, 5, 20)
print(data)
sensor1.add_data(time=np.arange(100), data=data)
print(sensor1.data)

sensor1.clear_data()
print(sensor1.data)