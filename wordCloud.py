import PyPDF2
from wordcloud import WordCloud, STOPWORDS
import re
import time


def clean_file_data():
    with open("HWN.pdf", 'rb') as book:
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
            clean_data = re.sub(",", "", combined_data)
        return clean_data


def generate_a_wordcloud():
    clean_data = clean_file_data()
    asq = input("Enter 'Y' to see data in text or 'N' to continue: ")
    if asq.lower() == "y":
        print(clean_data)

    new_text = clean_data.lower().split()

    # Function to read the frequency of text in a dictionary
    def count_freq(data):
        word_frq = {}
        for item in data:
            if item.isalpha():
                word_frq[item] = data.count(item)
        return word_frq

    asq2 = input("Enter 'Y' to data frequency in a dictionary or 'N' to quiet: ")
    if asq2.lower() == "y":
        print("This might take few time to complete.\nPlease wait...")
        print(count_freq(new_text))

    # Stop unimportant words eg; is, a, on, of etc
    stopwords = STOPWORDS
    wc = WordCloud(
        background_color="white",
        stopwords=stopwords,
        height=600,
        width=400
    )

    # Generate a word cloud using file content
    wc.generate(clean_data)
    wc.to_file('wordcloud_img.png')  # Save word cloud in png extension

    print("'\n'Generating word cloud...")
    time.sleep(1)
    print('\033[94m''\033[1m'"=====", '\033[0m' "Word Cloud Generated Successfully", '\033[94m''\033[1m', "=====",
          '\033[0m')


if __name__ == '__main__':
    generate_a_wordcloud()
