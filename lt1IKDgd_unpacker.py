import sys

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 3:
    print(f"Usage: python3 {sys.argv[0]} input_file output_file")
    sys.exit(1)

# Get the input and output file paths from command-line arguments
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

try:
    # Open the input file in binary mode for reading
    with open(input_file_path, 'rb') as input_file:
        # Read the binary data from the input file
        binary_data = input_file.read()

    # Perform the XOR operation with 0xd5 on each character
    unpacked = bytes(x ^ 0xd5 for x in binary_data)

    # Open the output file in binary mode for writing
    with open(output_file_path, 'wb') as output_file:
        # Write the XORed data to the output file
        output_file.write(unpacked)

    print(f'File "{input_file_path}" XORed and saved as "{output_file_path}"')
except FileNotFoundError:
    print(f'Error: File "{input_file_path}" not found.')
except Exception as e:
    print(f'An error occurred: {str(e)}')
