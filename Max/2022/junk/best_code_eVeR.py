import random
import time
from threading import Thread, active_count, enumerate

def average(list):
    return (sum(list) / len(list))

def shuffle_and_sort():
    shuffles = 0
    start = time.time()

    # create an incremented list
    number_list = list(range(8))
    # shuffle the list
    random.shuffle(number_list)
    print(number_list)
    # shuffle the list until it is sorted
    while True:
        random.shuffle(number_list) # randomize the list of numbers
        shuffles += 1 # count shuffles
        if (sorted(number_list) == number_list): # sort the number list to check if the randomizer sorted the list
            break

    print(number_list)

    end = time.time()
    total_time = end - start
    list_times.append(total_time)
    average_time = average(list_times)

    list_shuffles.append(shuffles)

    print("Time in seconds: {}".format(total_time))
    print("Current average: {}".format(average_time))
    print("Minimum time: {}".format(min(list_times)))
    print("Maximum time: {}".format(max(list_times)))
    print("Shuffles taken: {}".format(shuffles))
    print("Minimum of shuffles: {}".format(min(list_shuffles)))
    print("Maximum of shuffles: {}".format(max(list_shuffles)))
    print("-----")

def breakout():
    # wait for all threads to finish
    for thread in enumerate():
        thread.join()

list_times = []
list_shuffles = []
average_time = 0

# create a thread for each iteration of the for-loop
for i in range(300):
    thread = Thread(target=shuffle_and_sort)
    thread.start()

# wait for user input
input("Press Enter to cancel all threads and exit the script")

# cancel all threads and exit the script
breakout()
