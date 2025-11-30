# multithreading -  used to perform multiple tasks concurrently (multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
# SYNTAX -          threading.Thread(target=my_function)

import threading
import time


def walking_dog(name: str):
    # print("Time for taking dog to walk")
    time.sleep(8)
    print(f"taking {name} to walk")


def take_out_trash():
    time.sleep(3)
    print("taking out trash")


def check_mails():
    # print("started checking mails")
    time.sleep(10)
    print("checking mails")


if __name__ == "__main__":
    start = time.time()
    chore1 = threading.Thread(target=walking_dog, args=("puppy",))
    chore1.start()
    chore2 = threading.Thread(target=take_out_trash)
    chore2.start()
    chore3 = threading.Thread(target=check_mails)
    chore3 .start()

    chore1.join()
    chore2.join()
    chore3.join()

    print("time taken to complete all tasks: ", time.time()-start)
