import random
import time
import numpy as np
import matplotlib.pyplot as plt
from inputimeout import inputimeout, TimeoutOccurred


def serial_recall(length=20, wait=1, n=1, WorkingMemory=0, Pause=0):
    proportions = []
    counts = np.zeros(length)

    for i in range(n):
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        serial_recall = [random.choice(alphabet) for i in range(length)]

        for letter in serial_recall:
            print("\n" * 25)
            print(letter)
            print("\n" * 10)
            time.sleep(wait)

        print("\n"*50)

        if WorkingMemory > 0:
            t_end = time.time() + WorkingMemory
            while time.time() < t_end:
                print(t_end - time.time())
                try:
                    inputimeout(f"{random.choice(range(100))} + {random.choice(range(100))} = ", t_end - time.time())
                except TimeoutOccurred:
                    print("\n.............................................................")

        if Pause > 0:
            print(f"Wait for {Pause} seconds")
            time.sleep(Pause)

        time.sleep(1)
        print("You should now enter the sequence:")
        answer = [input("Enter sequence:  ") for letter in serial_recall]

        sum_ = 0
        for i, x in enumerate(zip(answer,serial_recall)):
            if x[0] == x[1]:
                sum_ += 1
                counts[i] += 1

        proportion = sum_ / len(answer)
        proportions.append(proportion)

    plt.plot(range(1, length + 1), counts)
    plt.show()
    return proportions, counts




# print(serial_recall(length=5, n=1, wait=1, WorkingMemory=True))
print(serial_recall(length=5, n=1, wait=1, Pause=15))
