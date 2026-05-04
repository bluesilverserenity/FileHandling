import time
import datetime

mydates = []
for i in range(5):
    mydates.append(datetime.datetime.now())
    time.sleep(2)  # Sleep for 2 seconds to create a delay between each datetime entry
    print(mydates[i]) # Print the current datetime entry after the delay
print("\n")

for i in mydates:  # Print the current datetime entries stored after the delay
    print(i)
