from app.io.output import output_text_to_console, write_text_to_file
from app.io.input import input_text_from_console, read_text_from_file, read_text_from_file_pd

filename_to_read = "./data/input.txt"
filename_to_read_pd = "./data/input.csv"

filename_to_write = "./data/output.txt"

def main():
    # Functions from input package
    text_from_console = input_text_from_console()
    text_from_file = read_text_from_file(filename_to_read)
    text_from_pd_file = read_text_from_file_pd(filename_to_read_pd)

    # Functions from output package
    output_text_to_console(text_from_console)
    output_text_to_console(text_from_file)
    output_text_to_console(text_from_pd_file)

    # Write an outputs to file
    text_to_write = "Text from console: " + text_from_console + "\nText from file: "\
                    + text_from_file + "\nText from file with pandas: " + text_from_pd_file
    write_text_to_file(text_to_write, filename_to_write)


if __name__ == "__main__":
    main()
