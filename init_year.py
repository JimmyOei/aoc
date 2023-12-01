import os

year = "2023"
path = os.path.join(os.getcwd(), year)

try:
    os.mkdir(path)
except FileExistsError:
    print(f"\nFolder '{year}' already exists.\n")

for day in range(1, 32):
    day_folder_name = f"{day:02}"
    day_folder_path = os.path.join(path, day_folder_name)
    os.mkdir(day_folder_path)
    
    input_file_path = os.path.join(day_folder_path, f"input_{day_folder_name}.txt")
    with open(input_file_path, "w") as f:  
        f.write("Replace this with the input for day " + day_folder_name + " and embrace yourself to get your brain cracked with these lines ;)")

    solution1_file_path = os.path.join(day_folder_path, f"solution_{day_folder_name}.1.txt")
    with open(solution1_file_path, "w") as f:  
        f.write("Well, well, well... we gonna code in txt now, huh?\nReplace this nonsense with your superior language...")

    solution2_file_path = os.path.join(day_folder_path, f"solution_{day_folder_name}.2.txt")
    with open(solution2_file_path, "w") as f:  
        f.write("Well, well, well... we gonna code in txt now, huh?\nReplace this nonsense with your superior language...")  

print(f"\nInitiated '{year}', code away. :)\n")
