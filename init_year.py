import os

year = "2023"
path = os.path.join(os.getcwd(), year)

try:
    os.mkdir(path)
except FileExistsError:
    print(f"\nFolder '{year}' already exists.\n")

for day in range(1, 26):
    day_folder_name = f"{day:02}"
    day_folder_path = os.path.join(path, day_folder_name)
    os.mkdir(day_folder_path)
    
    input_file_path = os.path.join(day_folder_path, f"input_{day_folder_name}.txt")
    with open(input_file_path, "w") as f:  
        f.write("Input for day " + day_folder_name + ". Have fun!")

    solution1_file_path = os.path.join(day_folder_path, f"solution_{day_folder_name}.1.py")
    with open(solution1_file_path, "w") as f:  
        f.write("Day " + day_folder_name + " Part 1. Good Luck :)")

    solution2_file_path = os.path.join(day_folder_path, f"solution_{day_folder_name}.2.py")
    with open(solution2_file_path, "w") as f:  
        f.write("Day " + day_folder_name + " Part 2. Good Luck :)")

print(f"\nInitiated '{year}', code away. :)\n")
