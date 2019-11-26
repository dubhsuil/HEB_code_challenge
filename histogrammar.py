"""Write histogrames to an output file."""
import argparse
import re


def generate_frequency_dict(filename='input.txt'):
    """Generate a dictionary of words to frequencies, and a total word count.

    uses regex to match words, without punctuation, and considers everything in lowercase,
    as such there is no difference between 'Hickory' and 'hickory'.

    inputs:
        - filename (str): defaults to input.txt, the name of the file to read from.

    returns:
        - dict: a dictionary of words to frequencies
        - int: the number of "words" in the paragraph

    """
    with open(filename, 'r') as paragraph:

        # initialize variables
        word_count = 0
        word_freqs = dict()

        # line by line
        for line in paragraph:
            # loop over all matches found
            for word in re.findall(r'\w+', line):
                word_freqs[word.lower()] = (
                    word_freqs[word.lower()] + 1
                ) if word_freqs.get(word.lower()) else 1

                # increment my word count
                word_count += 1

        return word_freqs, word_count


def write_histogram(freqs: dict, word_count: int, output_filename='output.txt'):
    """Write a dictionary as a histogram to output_filename.

    writes the provided frequency dictionary to output.txt as a histogram in the
    format: "   word | === (3)".

    inputs:
        - freqs (dict): a dictionary of strings to ints representing frequencies
        - word_count (int): the total number of words.

    returns:
        - bool: returns True on success

    """
    with open(output_filename, 'w') as output_file:
        keys_descending_by_value = sorted(freqs, key=freqs.get, reverse=True)
        field_width = greatest_len(keys_descending_by_value)
        # for index, key in enumerate(keys_descending_by_value):
        [
            output_file.write(
                '{:>{width}} | {} ({}){}'.format(
                    key,
                    freqs[key] * '=',
                    freqs[key],
                    '\n' if index < len(keys_descending_by_value) - 1 else '',
                    width=field_width
                )
            )
            for index, key in enumerate(keys_descending_by_value)
        ]


def greatest_len(words: list) -> int:
    """Find the greatest length key (+1) and return it."""
    current_max = -1
    for word in words:
        current_max = len(word) if len(word) > current_max else current_max
    return current_max + 1


if __name__ == '__main__':

    args = argparse.ArgumentParser(
        description='Generate a histogram based on an imput text document.'
    )

    args.add_argument(
        '-i',
        '--input_filename',
        help='The input filename',
        nargs='?',
        type=str,
        default='input.txt'
    )

    args.add_argument(
        '-o',
        '--output_filename',
        help='The output filename.',
        nargs='?',
        type=str,
        default='output.txt'
    )

    found_args = args.parse_args()

    try:
        freqs, count = generate_frequency_dict(
            filename=found_args.input_filename
        )
        write_histogram(
            freqs,
            count,
            output_filename=found_args.output_filename
        )
    except FileNotFoundError:
        print(f'File {found_args.i} found.')
    except IOError as io_error:
        print('Encountered an IO Error while trying to read or write.')
        print(io_error.with_traceback())
