# HEB_code_challenge
This is a repository for my HEB code challenge due 11/26

## Requirements
In order to run the "Histogrammar" you must have [python (3.x)](https://www.python.org/downloads/) installed, along with the libraries: "re", and "argparse" (which should be builtins).

## Usage
```
usage: histogrammar.py [-h] [-i [INPUT_FILENAME]] [-o [OUTPUT_FILENAME]]

Generate a histogram based on an imput text document.

optional arguments:
  -h, --help            show this help message and exit
  -i [INPUT_FILENAME], --input_filename [INPUT_FILENAME]
                        The input filename, can be the absolute path if it is not local. If not provided, defaults to input.txt if not provided.
  -o [OUTPUT_FILENAME], --output_filename [OUTPUT_FILENAME]
                        The output filename, can be the absolute path, if you don't want it to be generated locally, defaults to output.txt if not provided.
```
Above is the help message provided by the program itself (the result of: `python histogrammar.py -h`). Neither the `-i` nor the `-o` arguments are necesarry, as the program will fall back to `input.txt` and `output.txt` as the default filenames, and they will be written to the local folder. As a side-note, if `output.txt`, or whatever you chose to name the output file, already exists it **will** be overwritten by the new output.
