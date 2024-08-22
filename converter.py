import sys
import markdown

# command line example:
    # python3 converter.py markdown input/markdown.md output/markdown.html

def convertMarkToHtml(inputFile, outputFile):
    with open(inputFile, 'r') as file:
        data = file.read()
        html = markdown.markdown(data)
        with open(outputFile, 'w') as file:
            file.write(html)
            print("File converted successfully")

inputFormat = sys.argv[1]
inputFile = sys.argv[2]
outputFile = sys.argv[3]

match inputFormat:
    case "markdown":
        convertMarkToHtml(inputFile, outputFile)
    case _:
        print("Input format not supported")
        sys.exit(1)
