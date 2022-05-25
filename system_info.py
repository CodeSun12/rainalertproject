import sys
import platform
import datetime as dt

print("System Information")
print(sys.version)
print("Version Information")
print(sys.version_info)
print(platform.python_version())


now = dt.datetime.now()

day = now.day
time = now.time()
date = now.date()

print(f"Current Date is: {date} and Current Time is : {time} and Current Day is : {day}")


r = int(input("Please Enter the value of r : \n"))
pi = 3.14
calculate_area_of_circle = pi * (r**r)
print(calculate_area_of_circle)

values = input("Please enter the values you want to enter \n")
list = values.split(" , ")
tuple = tuple(list)
print(f"List Is: {list}")
print(f"Tuple Is: {tuple}")