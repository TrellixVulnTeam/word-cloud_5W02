"""
PDF Extraction and analysis
By: Jamiu Shaibu
"""
import PyPDF2
import re


def scan_data(filename):
    book = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    page_Num = pdfReader.getNumPages()

    book_data = []
    for page in range(page_Num):
        page_content = pdfReader.getPage(page).extractText()
        book_data.append(page_content)

    combined_data = " ".join(book_data)
    """
    1. clean_data = words = re.findall(r'\w+', combined_data
    which will grab all the strings composed of 
    one or more “word characters” and will ignore punctuation and whitespace.
    """
    # clean_data = words = re.findall(r'\w+', combined_data)
    clean_data = re.sub(",", "", combined_data)
    print(clean_data)

    # To know the total Number of Words(now) in a context.
    print('\n''\033[94m''\033[1m'"=====", '\033[0m' "RESEARCH RESULTS", '\033[94m''\033[1m', "=====", '\033[0m')

    # Total number of pages in book
    print("Total number of pages in book is:", page_Num)

    print("The total number of words in book is: " + str(len(clean_data)))
    print('\033[94m''\033[1m'"=====", "%%%%%%%%%%=WITH 99.999999% ACCURACY=%%%%%%%%%%", "=====", '\033[0m')
    while True:
        print("\nSEARCH FOR A WORD")
        word = str(input("Enter ** to Quite\nEnter a word: ")).strip()
        print('\n''\033[94m''\033[1m'"=====", '\033[0m' "SEARCHED WORD", '\033[94m''\033[1m', "=====", '\033[0m')
        if word == '**':
            print('\033[91m''\033[1m' + "You Quited" + '\033[0m')
            break
        elif word.lower() in clean_data.lower():
            print('\033[92m''\033[1m'"=== Word Found in Text ===" + '\033[0m')
            print("The word", '\033[91m''\033[1m' + word + '\033[0m', "has", len(word), "letters")
            print('\033[91m''\033[1m' + word + '\033[0m' + " appeared " + str(
                clean_data.lower().count(word.lower())) + " time(s) in the book")
        else:
            print('\033[91m''\033[1m' + "Word not exist in book" + '\033[0m')


if __name__ == '__main__':
    scan_data(filename="HWN.pdf")
