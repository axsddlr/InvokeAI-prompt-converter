import re


def extract_numbers_from_text(text):
    numbers = re.findall(r'\d+\.\d+', text)
    return numbers


def convert_range(value):
    """
    It converts a value from one range to another

    :param value: The value to be converted
    """
    if value >= 1.0:
        plus_string = "+" * min(int((value - 1) * 10 + 1), 4)
    elif value >= 0.9:
        plus_string = "+"
    elif value < 0.89:
        plus_string = "-" * min(int((0.89 - value) * 10 + 1), 2)
    return plus_string


def convert_file(file_name):
    """
    It reads in a file, extracts the numbers from the text, converts the numbers to a string, and writes the new text to a
    new file

    :param file_name: the name of the file you want to convert
    """
    with open(file_name) as f:
        lines = f.readlines()
    with open("converted_prompts.txt", "w") as f:
        for line in lines:
            numbers = extract_numbers_from_text(line)
            for number in numbers:
                value = float(number)
                plus_string = convert_range(value)
                line = line.replace(number + ")", plus_string)
                line = line.replace(":", ")")
            f.write(line)


convert_file("prompt.txt")
