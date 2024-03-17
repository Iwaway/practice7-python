import pandas as pd

def output_text_to_console(text):
    """
    Function to output text to console.

    :param text: text to output to console.
    :type text: str
    """
    print(text)

def write_text_to_file(text, filename):
    """
    Function to write text to file with Python.

    :param text: text to write to file.
    :type text: str

    :param filename: path to file.
    :type filename: str
    """
    try:
        with open(filename, "w") as file:
            file.write(text)
        print(f"Text successfully wrote to file {filename}")
    except FileNotFoundError:
        print(f"Error: File with name {filename} not found.")
