import PyPDF2

from wordcloud import WordCloud, STOPWORDS


book = open('file_name', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.getPage
page_Num = pdfReader.getNumPages()

for pages in range(page_Num):
    text = pdfReader.getPage(pages).extractText()
    print(text)

    new_text = text.lower().split()
    print(new_text)

# Function to read the frequency of text in a dictionary
def count_freq(n):
    word_frq = {}
    for item in n:
        if item.isalpha():
            word_frq[item] = n.count(item)
    return word_frq


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
wc.generate(text)
wc.to_file('wordcloud.png')  # Save word cloud in png extension
