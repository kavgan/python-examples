'''

Python example using argparse module

Example:

python ./argparse/parser.py --input argparse/data/ --output argparse/output/

'''

import argparse


def get_args():

    # create description of task
    parser = argparse.ArgumentParser(description='File I/O')

    # add string type argument
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        help="full path to data files",
        required=True)
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help="output path",
        required=True)

    # array for all arguments passed to script
    args = parser.parse_args()

    # assign the args to variables
    input_directory = args.input
    output_path = args.output

    return input_directory, output_path


# Match return values from get_args()and assign to variables
input_, output_ = get_args()

print("Input path: {0}".format(input_))
print("Output path: {0}".format(output_))
