import datetime

now = datetime.datetime.now()
print(now)

print(now.year)  # Accessing the year attribute of the datetime object

tomorrow = datetime.datetime(2026, 5, 5, 12, 0, 0) # Creating a datetime object for May 5, 2026 at 12:00 PM
rtime = tomorrow - now  # Calculating the time difference between tomorrow and now
print(rtime)  # Printing the time difference

print(rtime.days)  # Printing the number of days in the time difference

#Creating a file named with the current date and time in its name

filename = datetime.datetime.now()
def create_file():
    with open(filename.strftime("%Y-%m-%d"), 'w') as file:  # Using strftime to format the filename with the current date and time
        file.write("This file was created on May 5th, 2026 ")  # Writing a message to the file with the current date and time

create_file()

def create_file():
    with open(filename.strftime("%Y-%m-%d") + ".txt", 'w') as file: # Adding a .txt extension to the filename for better file recognition
        file.write("This file was created on May 5th, 2026 ")  # Writing a message to the file with the current date and time

create_file()
