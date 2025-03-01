with open("test_1.txt", 'r') as file:
    lines=file.readlines()

    count=len(lines)

print(f"Number of lines in the file: {count}")