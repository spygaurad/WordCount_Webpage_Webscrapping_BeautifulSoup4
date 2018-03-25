import requests
from bs4 import BeautifulSoup
import operator


def site_to_words(url):
    word_list = []
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    for text in soup.findAll('div', {'class':'the_review'}):
        sentences = text.string
        words = sentences.lower().split()
        for word in words:
            #print(word)
            word_list.append(word)
    clean_unrequired_symbols(word_list)


def clean_unrequired_symbols(word_list):

    clean_word_list = []
    for words in word_list:
        symbols = "~!@#$%^&*()_+=-|}{:\"?><[]\;',./'`"
        for i in range(1,len(symbols)):
            words = words.replace(symbols[i], "")
        if len(words) > 0 :                     #dont add blank after removing :)
            #print(words)
            clean_word_list.append(words)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count_dicitonary = {}

    for word in clean_word_list:

        if word in word_count_dicitonary:
            word_count_dicitonary[word] += 1
        else:
            word_count_dicitonary[word] = 1

    for key, value in sorted(word_count_dicitonary.items(), key=operator.itemgetter(0)):    # 0means key 1 means value
        print(key, value)

site_to_words(r'https://www.rottentomatoes.com/m/padmaavat/reviews/')