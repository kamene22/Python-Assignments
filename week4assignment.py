def read_and_write_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File read successfully!")

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"📝 Modified content saved in: {new_filename}")

    except FileNotFoundError:
        print("Error: That file does not exist.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


read_and_write_file()
