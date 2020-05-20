
import string
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
punctuation = string.punctuation


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    opened_file = open(file)
    text = opened_file.read()
    no_punctuation = ""
    for punc in text:
        if punc not in punctuation:
            no_punctuation = no_punctuation + punc
    text_lower = no_punctuation.lower()
    print(text_lower)


##don't worry about this stuff##
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
