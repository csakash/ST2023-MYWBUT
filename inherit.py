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

sensor = Sensor(name="Private Sensor", record_date="2023-07-12")
sensor2 = Sensor(name="Gyroscope", record_date="2023-04-05")
print(sensor.name, sensor.record_date)
# print(sensor.__location)
sensor.get_location()
sensor.set_location(new_location="Hyderabad")
# class Accelerometer(Sensor):
#     def __init__(self, name, location, record_date, brand):
#         super().__init__(name, location, record_date)
#         self.brand = brand


#     def show_sensor_type(self):
#         print("I am an Accelerometer")

import numpy as np

# sensor1 = Sensor(name='sensor1', location='Berkeley', record_date='2019-01-01')
# data = np.random.randint(-5, 5, 20)
# time = np.arange(20)

# for i in range(len(data)):
#     print(time[i], "---------> ", data[i])


# sensor1.add_data(time=time, data=data)
# print(sensor1.data)

# acc = Accelerometer(name='accelerometer', location='Mumbai', record_date='2023-07-11', brand="Quectel")
# print(acc.name, acc.location, acc.record_date, acc.brand)

# data = np.random.randint(-5, 5, 20)
# time = np.arange(20)

# acc.add_data(time=time, data=data)
# print(acc.data)
# acc.show_sensor_type()


# sensor1.clear_data()
# print(sensor1.data)

"""
1. Take a superior class called DepartmentCandidate
2. Create common fields of individual students as instance attributes
    (name, roll_no, department_name)
3. Create a child class named Student
4. Add a new instance attribute called skilled and use super()
5. Skill should be a list which will hold all the skills of a student
"""

# class DepartmentStudent():
#     # this is our master or superior class
#     def __init__(self, student_name, roll_no, department_name):
#         self.student_name = student_name
#         self.roll_no = roll_no
#         self.department_name = department_name

#     def get_student_details(self):
#         print(self.student_name, self.roll_no, self.department_name)

# class Student(DepartmentStudent):
#     def __init__(self, student_name, roll_no, department_name, skills):
#         super().__init__(student_name, roll_no, department_name)
#         self.skills = skills

# student1 = Student(
#     student_name="Rahul Mondal",
#     roll_no="139",
#     department_name="CSE",
#     skills=["Python", "MySQL", "Data Analysis"]

# )

# student1.get_student_details()
# print(student1.skills)