
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
import string
import nltk
#from patsy import dmatrices
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.tokenize import sent_tokenize, word_tokenize
import re
import csv
from gensim import corpora
import gensim

df = pd.read_csv('data_scraped.csv', encoding="iso-8859-1")
df.text = df.text.astype(str)
#stop = set(stopwords.words('english'))
# stop.update(['apple','Apple','lot','employee','job', 'company', 'cramer', 'said', 'money', 'nvdia', 'facebook', \
#             'dont', 'percent', 'nvidia', 'starbucks'])
punc = string.punctuation

# def clean_tokenize(s):
#         s = re.sub(r'[^\w\s]', '',s.lower())
#         return([word for word in word_tokenize(s) if word not in stop if word not in punc])

def reveal_topics(datafrm, custom_stopwords ,tickername = 'AAPL',  num_topics=5, NUM_WORDS=4):
    li = custom_stopwords
    stop = set(stopwords.words('english'))
    stop.update(li)
    def clean_tokenize(s):
        s = re.sub(r'[^\w\s]', '',s.lower())
        return([word for word in word_tokenize(s) if word not in stop if word not in punc])
    datafrm['tokens'] = datafrm.text.map(clean_tokenize)
    df = datafrm[datafrm['tick'] == tickername]
    dictionary = corpora.Dictionary(df['tokens'])
    corpus = [dictionary.doc2bow(text) for text in df['tokens']]
    NUM_TOPICS = num_topics
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    topics_pros = ldamodel.print_topics(num_words=NUM_WORDS)
    print(" For ",tickername, "5 topics are defined as follows: ")
    for topic in topics_pros:
        print(topic)
    
    return topics_pros

# =============wordcloud=============
def make_wordcloud(datafrm, tickername, custom_stopwords):
    #print(df.head())
    df2 = datafrm[datafrm['tick'] == tickername]
    #print(df2.head())
    df2['text'] = df2['text'].apply(lambda x:re.sub(r'[^\w\s]', ' ', x.lower()))
    df2['text'] = df2['text'].apply(lambda x:re.sub(r'(\\n+)', ' ', x))
    reviews = str(df2['text'].sum())
    stop = set(STOPWORDS)
    stop.update(custom_stopwords)
    wordcloud = WordCloud(stopwords=stop, max_font_size=75, max_words=100, background_color="white").generate(reviews)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wordcloud.to_file(tickername + ".png")
    return "Wordcloud saved"

def main():
    #apple topics
    li = []
    appl_stp = ['apple','Apple','lot','employee','job', 'company', 'cramer', 'said', 'money', \
             'dont', 'percent']
    t_appl = reveal_topics(df, appl_stp)
    for i in range(len(t_appl)):
        li.append(('AAPL',t_appl[i][1]))


    #Fb topics

    fb_stp = ['lot','employee','job', 'company', 'cramer', 'said', 'money', 'facebook', \
             'dont', 'percent']
    t_fb = reveal_topics(df, fb_stp, 'FB')
    for i in range(len(t_fb)):
        li.append(('FB',t_fb[i][1]))

    jnj_stp = ['lot','employee','job', 'company', 'cramer', 'said', 'money', 'johnson', \
             'dont', 'percent']

    t_jnj = reveal_topics(df, jnj_stp, 'JNJ')
    for i in range(len(t_jnj)):
        li.append(('JNJ',t_jnj[i][1]))

    mo_stp = ['lot','employee','job', 'company', 'cramer', 'said', 'money',  \
             'dont', 'percent', 'nan']

    t_mo = reveal_topics(df, jnj_stp, 'MO')
    for i in range(len(t_mo)):
        li.append(('MO',t_mo[i][1]))


    nvda_stp = ['lot','employee','job', 'company', 'cramer', 'said', 'money', 'nvdia',  \
             'dont', 'percent', 'think']

    t_nvda = reveal_topics(df, jnj_stp, 'NVDA')
    for i in range(len(t_nvda)):
        li.append(('NVDA',t_nvda[i][1]))

    sbux_stp = ['lot','employee','job', 'company', 'cramer', 'said', 'money',  \
             'dont', 'percent', 'nvidia', 'starbucks']

    t_sbux = reveal_topics(df, jnj_stp, 'SBUX')
    for i in range(len(t_sbux)):
        li.append(('SBUX',t_sbux[i][1]))
    
    with open('topics.csv', 'w', ) as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,delimiter='\n')
        wr.writerow(li)

    ## Printing wordcloud
    make_wordcloud(df, 'AAPL', appl_stp)
    make_wordcloud(df, 'FB', fb_stp)
    make_wordcloud(df, 'JNJ', jnj_stp)
    make_wordcloud(df, 'MO', mo_stp)
    make_wordcloud(df, 'NVDA', nvda_stp)
    make_wordcloud(df, 'SBUX', sbux_stp)



if __name__ == '__main__':
    main()
