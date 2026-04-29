with open('name.txt', 'w+') as file:  # Open the file in write and read mode
    file.write('Good morning')
    file.write('\nMy name is John')
    file.seek(0)  # Move the file pointer back to the beginning of the file
    now = file.readline()  # It is best to use readline() in a loop to read the file line by line, as it allows you to process each line individually and handle large files without loading the entire content into memory at once.
    while now:
        print(now.strip())  # Print the content of the file, stripping any leading/trailing whitespace
        now = file.readline()  # Read the next line of the file

print(now)
