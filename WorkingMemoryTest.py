import random
import time
import numpy as np
import matplotlib.pyplot as plt
from inputimeout import inputimeout, TimeoutOccurred
import pandas as pd
import os
from functions import free_recall, save_data, serial_recall

data_file_name = "Kasper/eksperiment2_WorkingMemoryTrue.csv"

waits, corrects, userInputs = free_recall(length=20, wait=1, workingMemory=True, pause=15)
print(waits, corrects, userInputs)

save_data(waits, corrects, userInputs, data_file_name_input = data_file_name)
print("Done")