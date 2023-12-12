def decode(message_file):
    # Read the file and store the content in a dictionary
    with open(message_file, 'r') as file:
        lines = file.readlines()
        word_dict = {int(line.split()[0]): line.split()[1].strip() for line in lines}

    # Generate the pyramid and find the key numbers
    pyramid = []
    row, num = 1, 1
    while num <= max(word_dict.keys()):
        pyramid.append([i for i in range(num, num + row)])
        num += row
        row += 1

    # Extract the message
    message = ' '.join([word_dict[n] for row in pyramid for n in row if n in word_dict])

    return message

def prompt_and_decode():
    # Prompt the user for the file path
    file_path = input("Please enter the path to the message file: ")

    # Decode the message
    try:
        decoded_message = decode(file_path)
        return decoded_message
    except FileNotFoundError:
        return "File not found. Please check the path and try again."
    except Exception as e:
        return f"An error occurred: {e}"

# To use this, call prompt_and_decode()
# Example usage in a Python environment: message = prompt_and_decode()
# The user will be prompted to enter the path to the .txt file in the terminal.
print(prompt_and_decode())
