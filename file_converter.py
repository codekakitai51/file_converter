import sys
import markdown

if len(sys.argv) != 4:
    print("Usage: file_converter.py <command> <input_file> <output_file>")
    sys.exit(1)

command = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]

def executeCommand(command, input_file, output_file):
    try:
        if output_file[-4:] != "html":
            print("set <html> as file extension of output file")
            sys.exit(1)

        if command == "markdown":
            with open(input_file, 'r') as f:
                text = f.read()
            with open(output_file, 'w') as f:
                f.write(markdown.markdown(text))
    except FileNotFoundError:
        print("set <md> as file extension of input file")
        sys.exit(1)

executeCommand(command, input_file, output_file)
