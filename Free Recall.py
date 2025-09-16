import random
import time
import numpy as np
import matplotlib.pyplot as plt
from inputimeout import inputimeout, TimeoutOccurred

def free_recall(length=20, wait=1, n=1, WorkingMemory=0, Pause=0):
    proportions = []
    counts = np.zeros(length)
    all_correct_counts = []
    all_incorrect_counts = []

    for trial in range(n):
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        # Create the study list (ensure no duplicates for free recall)
        study_list = random.sample(alphabet, length)
        
        # Present items one by one
        for letter in study_list:
            print("\n" * 25)
            print(letter)
            print("\n" * 10)
            time.sleep(wait)

        print("\n"*50)

        if WorkingMemory > 0:
            t_end = time.time() + WorkingMemory
            while time.time() < t_end:
                remaining = t_end - time.time()
                print(f"Time remaining: {remaining:.1f} seconds")
                try:
                    inputimeout(f"{random.choice(range(100))} + {random.choice(range(100))} = ", remaining)
                except TimeoutOccurred:
                    print("\n.............................................................")

        if Pause > 0:
            print(f"Wait for {Pause} seconds")
            time.sleep(Pause)

        time.sleep(1)
        print("You should now recall as many items as you can (in any order):")
        print(f"Enter up to {length} items. Press Enter twice when finished.")
        
        # Collect free recall responses
        recalled_items = []
        for i in range(length):
            response = input(f"Enter item {i+1}/{length} (or press Enter to finish early): ").strip().upper()
            if response == "":
                break
            recalled_items.append(response)
        
        # Remove duplicates while preserving order
        unique_recalled = []
        for item in recalled_items:
            if item not in unique_recalled:
                unique_recalled.append(item)
        
        # Calculate correct and incorrect recalls
        correct_recalls = [item for item in unique_recalled if item in study_list]
        incorrect_recalls = [item for item in unique_recalled if item not in study_list]
        
        # Update counts
        correct_count = len(correct_recalls)
        incorrect_count = len(incorrect_recalls)
        
        all_correct_counts.append(correct_count)
        all_incorrect_counts.append(incorrect_count)
        
        # Count correct recalls by serial position
        for position, item in enumerate(study_list):
            if item in correct_recalls:
                counts[position] += 1
        
        proportion = correct_count / length
        proportions.append(proportion)
        
        print(f"\nTrial {trial + 1} Results:")
        print(f"Correct: {correct_count}/{length}")
        print(f"Incorrect: {incorrect_count}")
        print(f"Missed: {length - correct_count}")
        print("-" * 40)

    # Calculate averages across trials
    avg_correct = np.mean(all_correct_counts)
    avg_incorrect = np.mean(all_incorrect_counts)
    avg_missed = length - avg_correct

    # Plot serial position curve
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, length + 1), counts/n)  # Convert to proportion
    plt.xlabel('Serial Position')
    plt.ylabel('Proportion Recalled')
    plt.title('Serial Position Curve')
    plt.grid(True)
    
    # Plot overall performance
    plt.subplot(1, 2, 2)
    categories = ['Correct', 'Incorrect', 'Missed']
    values = [avg_correct, avg_incorrect, avg_missed]
    colors = ['green', 'red', 'orange']
    
    bars = plt.bar(categories, values, color=colors)
    plt.ylabel('Average Count')
    plt.title('Recall Performance Summary')
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{value:.1f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    return proportions, counts, all_correct_counts, all_incorrect_counts

# Example usage:
proportions, counts, correct, incorrect = free_recall(length=10, wait=1, n=1)