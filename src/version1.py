# Name: Daniel Yan
# Email: daniel.yan@vanderbilt.edu
# Description: Quick python script to calculate some results for scientific computing model involving
# oxidation and temperature.

# Imports
from math import exp
import os

# Constants
DATA_DIR = "../data/" # Directory for data
OUTPUT = "../results/output.csv" # File to write outputs.

def read_lines_decimal(read_file):
    """
    Read all lines of a file that are decimal values into a list.
    :param read_file: File handler for the file to read.
    :return: List of decimal values.
    """
    # Read all lines with decimal values into list.
    data_list = []
    for line in read_file:
        # Strip whitespace from line
        value = str.strip(line)
        # Try converting to floating point. If successful, add to list of numbers.
        try:
            data_list.append(float(value))
        # Do nothing if line is not decimal
        except ValueError:
            pass
    return data_list

def process_file(filename, write_file):
    """
    Process a file with mathematical model and write down the result to file
    :param filename: Name of file to process
    :param write_file: File to write output to
    :return: None
    """
    # For each file, first open the file.
    with open(DATA_DIR + filename, 'r') as read_file:
        # Get list of decimal values from the file
        data_list = read_lines_decimal(read_file)
        # Create running sum of calculations from the file
        sum = 0
        # Apply modeling equation to all files in the list and add to the sum
        for value in data_list:
            sum += 1.922 * exp(-23242 / (273.15 + float(value)))
        # Write the name of the file without the .txt ending and the sum separated by a tab
        write_file.write(filename[:-4] + "," + str(sum) + "\n")

def main():
    # Open output file to write to
    with open(OUTPUT, "w") as write_file:
        # Open each of the text files in the data directory and process the file.
        for filename in os.listdir(DATA_DIR):
            process_file(filename, write_file)

if __name__ == '__main__':
    main()