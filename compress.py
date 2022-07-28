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
    s += "!"
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
            diff_string = f"{s[i]}{diff}" if diff > 2 else f"{s[i:j]}"
            # Appending to a list in python is O(1)
            result.append(diff_string)
            # move the 1st pointer to the start of the next group of Characters and advance the next pointer.
            i = j
            j += 1
    # Join the strings in the array and return that. This has a complexity of 0(n)
    return "".join(result)

    # The total of non_constant operations gives O(n) + O(n) + O(n) .
    # The highest factor is O(n) so the complexity is O(n)


if __name__ == "__main__":
    try:
        with open(args.input_file, 'r') as file:
            uncompressed_string = "".join(file.read().split())
    except FileNotFoundError:
        print("Input file not found")
        sys.exit()
    if verbose:
        start_time = time.time()
        compressed_string = compress(uncompressed_string)
        print(f"Execution time --- {time.time() - start_time} seconds ---")
        print(f"Length of Uncompressed String: {len(uncompressed_string)}")
        print(f"Length of Compressed String: {len(compressed_string)}")
        print(f"Uncompressed String: {uncompressed_string}\n")
    else:
        compressed_string = compress(uncompressed_string)
    print(f"Compressed String: {compressed_string}")
    f = open(args.output_file, "w")
    f.write(compressed_string)
    print(f"\n Compressed String written to {args.output_file}")
