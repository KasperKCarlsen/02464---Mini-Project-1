import random
import time
import numpy as np
import matplotlib.pyplot as plt
from inputimeout import inputimeout, TimeoutOccurred
import pandas as pd
import os


def serial_recall(length=15, wait=1, n=1, chunking=False):
    print("\n" * 40)
    print("LOOK HERE")
    print("\n" * 10)
    time.sleep(5)
    # proportions = []
    # counts = np.zeros(length)
    all_correct_answers = []
    all_user_answers = []
    for i in range(n):
        print("\n" * 40)
        print("LOOK HERE")
        print("\n" * 10)
        time.sleep(1)
        if chunking:
            choices = [
                "for",
                "fra",
                "far",
                "mor",
                "hun",
                "han",
                "den",
                "det",
                "har",
                "som",
                "med",
                "dig",
                "mig",
                "sig",
                "var",
                "vil",
                "kan",
                "man",
                "ned",
                "ind",
                "til",
                "lys",
                "hus",
                "mus",
                "kat",
                "ged",
                "gul",
                "rød",
                "blå",
                "her",
                "der",
                "vor",
                "jeg",
                "top",
                "arm",
                "ben",
                "øje",
                "fod",
                "gæs",
                "and",
                "træ",
                "bus",
                "bil",
                "bog",
                "pen",
                "dør",
                "tag",
                "vej",
                "sti",
                "sol",
            ]
        else:
            choices = [chr(i) for i in range(ord("A"), ord("Z") + 1)]

        sequence = [random.choice(choices) for i in range(length)]
        all_correct_answers.append(sequence.copy())

        for idx, letter in enumerate(sequence):
            print("\n" * 25)
            print(f"idx #: {idx + 1}")
            print(letter)
            print("\n" * 10)
            time.sleep(wait)

        print("\n" * 50)

        time.sleep(1)
        print("You should now enter the sequence:")
        answer = [input("Enter sequence:  ") for letter in sequence]
        all_user_answers.append(np.char.upper(answer.copy()))
        # sum_ = 0
        # for i, x in enumerate(zip(answer,serial_recall)):
        #     if x[0] == x[1]:
        #         sum_ += 1
        #         counts[i] += 1

        # proportion = sum_ / len(answer)
        # proportions.append(proportion)

    # plt.plot(range(1, length + 1), counts)
    # plt.show()
    return (
        np.array([wait] * n),
        np.array(all_correct_answers),
        np.array(all_user_answers),
    )


def free_recall(length=20, wait=1, n=1, workingMemory=False, pause=0):
    # proportions = []
    # counts = np.zeros(length)
    # all_correct_counts = []
    # all_incorrect_counts = []
    all_correct_answers = []
    all_user_answers = []
    print("\n" * 40)
    print("LOOK HERE")
    print("\n" * 10)
    time.sleep(5)
    for trial in range(n):
        print("\n" * 40)
        print("LOOK HERE")
        print("\n" * 10)
        time.sleep(1)

        numbers = [str(i) for i in range(10, 100)]
        # Create the study list (ensure no duplicates for free recall)
        correct_answers = random.sample(numbers, length)
        ###### csv.write(correct_answers + ":")
        all_correct_answers.append(correct_answers.copy())
        # Present items one by one
        for idx, letter in enumerate(correct_answers):
            print("\n" * 25)
            print("index #: ", idx)
            print(letter)
            print("\n" * 10)
            time.sleep(wait)

        print("\n" * 50)

        if workingMemory:
            t_end = time.time() + pause
            while time.time() < t_end:
                print(t_end - time.time())
                try:
                    inputimeout(
                        f"{random.choice(range(100))} + {random.choice(range(100))} = ",
                        t_end - time.time(),
                    )
                except TimeoutOccurred:
                    print(
                        "\n............................................................."
                    )

        else:
            print(f"Wait for {pause} seconds")
            time.sleep(pause)

        time.sleep(1)
        print("You should now recall as many items as you can (in any order):")
        print(f"Enter up to {length} items. Press Enter twice when finished.")

        # Collect free recall responses
        recalled_items = []
        for i in range(length):
            response = (
                input(f"Enter item {i+1}/{length} (or press Enter to finish early): ")
                .strip()
                .upper()
            )
            if response == "":
                break
            recalled_items.append(response)
        all_user_answers.append(recalled_items.copy())
        # Remove duplicates while preserving order
    #     unique_recalled = []
    #     for item in recalled_items:
    #         if item not in unique_recalled:
    #             unique_recalled.append(item)
    #     ####### csv.write(unique_recalled + "\n")

    #     # Calculate correct and incorrect recalls
    #     correct_recalls = [item for item in unique_recalled if item in correct_answers]
    #     incorrect_recalls = [item for item in unique_recalled if item not in correct_answers]

    #     # Update counts
    #     correct_count = len(correct_recalls)
    #     incorrect_count = len(incorrect_recalls)

    #     all_correct_counts.append(correct_count)
    #     all_incorrect_counts.append(incorrect_count)

    #     # Count correct recalls by serial position
    #     for position, item in enumerate(correct_answers):
    #         if item in correct_recalls:
    #             counts[position] += 1

    #     proportion = correct_count / length
    #     proportions.append(proportion)

    #     print(f"\nTrial {trial + 1} Results:")
    #     print(f"Correct: {correct_count}/{length}")
    #     print(f"Incorrect: {incorrect_count}")
    #     print(f"Missed: {length - correct_count}")
    #     print("-" * 40)

    # # Calculate averages across trials
    # avg_correct = np.mean(all_correct_counts)
    # avg_incorrect = np.mean(all_incorrect_counts)
    # avg_missed = length - avg_correct

    # # Plot serial position curve
    # plt.figure(figsize=(12, 6))
    # plt.subplot(1, 2, 1)
    # plt.plot(range(1, length + 1), counts/n)  # Convert to proportion
    # plt.xlabel('Serial Position')
    # plt.ylabel('Proportion Recalled')
    # plt.title('Serial Position Curve')
    # plt.grid(True)

    # # Plot overall performance
    # plt.subplot(1, 2, 2)
    # categories = ['Correct', 'Incorrect', 'Missed']
    # values = [avg_correct, avg_incorrect, avg_missed]
    # colors = ['green', 'red', 'orange']

    # bars = plt.bar(categories, values, color=colors)
    # plt.ylabel('Average Count')
    # plt.title('Recall Performance Summary')

    # # Add value labels on bars
    # for bar, value in zip(bars, values):
    #     plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
    #             f'{value:.1f}', ha='center', va='bottom')

    # plt.tight_layout()
    # plt.show()

    # return proportions, counts, all_correct_counts, all_incorrect_counts
    return (
        np.array([wait] * n),
        np.array(all_correct_answers),
        np.array(all_user_answers, dtype=object),
    )


# Example usage:


def save_data(waits, corrects, userInputs, data_file_name_input="data.csv"):

    # numOfObs = (matrixx.shape[1] - 1) // 2

    dataDf = pd.DataFrame(
        [waits, corrects, userInputs],
    ).T
    dataDf.columns = ["wait", "correctSequence", "userInput"]

    if os.path.isfile(data_file_name_input):
        openDf = pd.read_csv(data_file_name_input)

        newDataDf = pd.concat([openDf, dataDf], ignore_index=True)
        newDataDf.columns = ["wait", "correctSequence", "userInput"]
        newDataDf.to_csv(data_file_name_input, index=False)
    else:
        dataDf.to_csv(data_file_name_input, index=False)


def loadDataFrame(path, convertToInt=False):

    df = pd.read_csv(path)

    df["correctSequence"] = df["correctSequence"].apply(
        lambda x: np.array(
            x.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace("\n", "")
            .split(" ")
        )
    )
    df["userInput"] = df["userInput"].apply(
        lambda x: np.array(
            x.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace("\n", "")
            .split(" ")
        )
    )

    if convertToInt:
        df["correctSequence"] = df["correctSequence"].apply(lambda x: x.astype(int))
        df["userInput"] = df["userInput"].apply(lambda x: x.astype(int))

    return df
