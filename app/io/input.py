import pandas as pd

def input_text_from_console():
    """
    Function to input text from console.

    :return: text from console.
    :rtype: str
    """
    return input("Enter a text for input: ")

def read_text_from_file(filename):
    """
    Function to read text from file with Python.

    :param filename: path to file.
    :type filename: str

    :return: read text from file.
    :rtype: str
    """
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File with name {filename} not found.")

def read_text_from_file_pd(filename):
    """
    Function for read text from file with library pandas.

    :param filename: path to file.
    :type filename: str

    :return: read text from file.
    :rtype: str
    """
    try:
        data = pd.read_csv(filename)
        return data.to_string(index=False)
    except FileNotFoundError:
        print(f"Error: File with name {filename} not found.")
