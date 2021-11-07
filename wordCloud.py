import PyPDF2
from wordcloud import WordCloud, STOPWORDS


book = open('HWN.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.getPage
page_Num = pdfReader.getNumPages()

for pages in range(page_Num):
    Text = pdfReader.getPage(pages).extractText()
    print(Text)

    new_text = Text.lower().split()
    print(new_text)


def count_freq(n):
    word_frq = {}
    for item in n:
        if item.isalpha():
            word_frq[item] = n.count(item)
    return word_frq


print(count_freq(new_text))

stopwords = STOPWORDS
wc = WordCloud(
    background_color="white",
    stopwords=stopwords,
    height=600,
    width=400
)
wc.generate(Text)
wc.to_file('my_word_cloud_test411200.png')
