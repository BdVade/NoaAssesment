# NoaAssesment
A Script to find sections in a Sequence of bytes with more thna 3 consecutive Repititions
## Requirements
- Have Python set up


## Usage
Run the Script with :

2 positional(required) arguments:
- input_file   the path to the file with the uncompressed sequence
- output_file  the path to the file to write the Compressed sequence


optional arguments:
  - -h, --help   Displays information on how to use the Script
  - --verbose    Display compression stats

## Example
```
 python compress.py --verbose=True uncompressed_test compressed_test
```

NOTE: The Arguments have to be in Order. The input file first, Then the output file. 

Using the --verbose flag displays the following information:

- Compressed Array
- Execution time
- Length of Uncompressed sequence
- Length of Compressed sequence

It can be used Like this:
```
python compress.py --verbose=True uncompressed_test compressed_test

```

## Tests
Tests can be Run with 
```
pytest -v tests.py
```

`uncompressed_test` contains the sequence to be compressed when the test is run

`compressed_test` contains the sequence after compression. 

NOTE:  If the Contents of `compressed_test` is changed Line 19 of `tests.py` has to be changed to match the Expected value