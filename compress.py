import argparse
import time
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Enter the path to the file with the uncompressed sequence", )
parser.add_argument("output_file", help="Enter the path to the file to write the Compressed sequence")
parser.add_argument("--verbose", help="Display compression stats", action="store_true")
args = parser.parse_args()
verbose = args.verbose


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


if __name__ == "__main__":
    try:
        with open(args.input_file, 'rb') as file:
            uncompressed_bytes = file.read()
            print(uncompressed_bytes)
    except FileNotFoundError:
        print("Input file not found")
        sys.exit()
    stats = []
    if verbose:
        start_time = time.time()
        compressed_bytes_array = compress(uncompressed_bytes)
        stats.append(f"\n Execution time --- {time.time() - start_time} seconds ---")
        stats.append(f"\n Length of Uncompressed String: {len(uncompressed_bytes)}")
        stats.append(f"\n Length of Compressed Array: {len(compressed_bytes_array)}")
    else:
        compressed_bytes_array = compress(uncompressed_string)
    with open(args.output_file, "wb") as f:
        for i in compressed_bytes_array:
            f.write(i)
    with open(args.output_file, "a") as f:
        for i in stats:
            f.write(i)


    print(f"\n Compressed String written to {args.output_file}")
