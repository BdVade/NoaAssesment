import argparse
import time
import sys
import click


# parser = argparse.ArgumentParser()
# parser.add_argument("input_file", help="Enter the path to the file with the uncompressed sequence", )
# parser.add_argument("output_file", help="Enter the path to the file to write the Compressed sequence")
# parser.add_argument("--verbose", help="Display compression stats", action="store_true")
# args = parser.parse_args()
# verbose = args.verbose
#

@click.command()
@click.option('--verbose', default=False, help="Output A detailed report of the compression")
@click.argument('input_path', required=1)
@click.argument('output', required=1)
def compression(verbose, input_path, output):
    """
    Read a sequence of bytes from a file, compress and write to an output file
    """

    def compress(s):
        """
        This solution used the double pointer method to achieve a runtime of O(n).
        n being the length of the string passed
        """
        # Initialize the variables i, j to act as pointers
        i = 0
        j = 0
        # appending ! to act as a delimiter so the correct length is calculated for the last group of characters
        # This operation takes O(n + 1)
        s += b'!'
        # Using a list to keep the counts to avoid Appending strings in the loop(O(n)(O(n) == O(n^2))
        result = []
        # This loop is an O(n) operation
        while j < len(s):
            # continue moving the second pointer if it's on the same group of characters as the 1st.
            if s[j] == s[i]:
                j += 1
                continue
            # else:
            elif s[j] != s[i]:
                # The difference in the pointers is the length of this group of characters.
                # This put in the required format and appended into the results list
                diff = j - i
                diff_string = s[i:i + 1] + str(diff).encode() if diff > 2 else s[i:j]

                # Appending to a list in python is O(1)
                result.append(diff_string)
                # move the 1st pointer to the start of the next group of Characters and advance the next pointer.
                i = j
                j += 1
        return result

        # The total of non_constant operations gives O(n) + O(n) + O(n) .
        # The highest factor is O(n) so the complexity is O(n)

    try:
        with open(input_path, 'rb') as file:
            uncompressed_bytes = file.read()
    except FileNotFoundError:
        print("Input file not found")
        sys.exit()
    stats = []
    if verbose:
        start_time = time.time()
        compressed_bytes_array = compress(uncompressed_bytes)
        stats.append(f"\n Execution time --- {time.time() - start_time} seconds ---")
        stats.append(f"\n Length of Uncompressed Array: {len(uncompressed_bytes)}")
        stats.append(f"\n Length of Compressed Array: {len(compressed_bytes_array)}")
    else:
        compressed_bytes_array = compress(uncompressed_bytes)
    with open(output, "wb") as f:
        for section in compressed_bytes_array:
            f.write(section)
    with open(output, "a") as f:
        for stat in stats:
            f.write(stat)

    print(f"\n Compressed String written to {output}")


if __name__ == "__main__":
    compression()
