'''
This Program reads an input file line by line and writes the
length of each line to an output file.

Usage: countlines.py <input> [<output>]
       if <output> is missing it defaults to <input>.out.txt
'''

import sys
import os.path

def main():
    '''called at program start
    responsible for getting the arguments, opening the files
    and writing the usage and error messages.
    '''
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: countlines.py <input> [<output>]')
        print('       if <output> is missing it defaults to <input>.out.txt')
        return

    inputfilename = sys.argv[1]
    if len(sys.argv) == 3:
        outputfilename = sys.argv[2]
    else:
        outputfilename = get_outputfilename(inputfilename)

    if os.path.exists(outputfilename):
        print(f'ERROR: the ouputfile "{outputfilename}" already exists. Aborted.')
        return

    try:
        with open(inputfilename) as f_in, open(outputfilename, 'w') as f_out:
            number_of_lines = write_line_lengths(f_in, f_out)
    except OSError as error:
        print(f'ERROR: {error}')
        return

    print(f'{number_of_lines} lines processed.')


def get_outputfilename(inputfilename):
    '''return the name of the outputfile
    used in case the program was called with one argument.

    the name of the inputfile without extension followed by .out.txt
    '''
    root, ext = os.path.splitext(inputfilename)
    return root + '.out.txt'


def write_line_lengths(inputfile, outputfile):
    '''reads each line in the inputfile
and writes its length to the outputfile.
    '''
    count = 0
    for line in inputfile:
        outputfile.write(f'{len(line)-1}\n')
        count += 1
    return count


if __name__ == '__main__':
    main()
