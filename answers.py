def readfiles(file1, file2):
    try:
        # Read content from the input file
        with open(file1, "r") as file:
            data = file.read()
        
        # Write content to the output file
        with open(file2, "w") as output:
            output.write(data)
        print(f"Content from '{file1}' has been written to '{file2}' successfully!")
    
    except FileNotFoundError:
        print(f"Error: The file '{file1}' was not found. Please check the file name and try again.")
    except IOError as e:
        print(f"Error: Unable to process the files. Details: {e}")

# Get filenames from the user
file1 = input("Enter the name of the file to read from: ")
file2 = input("Enter the name of the file to write to: ")

# Call the function
readfiles(file1, file2)


