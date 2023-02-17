#CRIAR WORDCLOUDS DE UM TEXTO
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import string

#nltk.download('stopwords')

text = open('texto.txt', mode = 'r', encoding = 'utf8').read()
text = text.lower() #deixando o texto todo minúsculo

#removendo pontos
text_sem_pontuacao = "".join([p for p in text if p not in string.punctuation])
#print(text_sem_pontuacao)

#tokenizando o texto
tokenizacao_palavras = nltk.word_tokenize(text_sem_pontuacao)
#print(tokenizacao_palavras)

#removendo stopwords
stopwords = stopwords.words('portuguese')
palavras_sem_stop = [p for p in tokenizacao_palavras if p not in stopwords]
#print(palavras_sem_stop)

#verificando frequência
freq = FreqDist(palavras_sem_stop)
freq = freq.most_common(10)
#print(freq)

#wordcloud
nuvem_palavras = WordCloud(
                            background_color = 'white',
                            stopwords = stopwords,
                            height = 1080,
                            width = 1080,
                            max_words = 100
                            )
nuvem_palavras.generate(text)
nuvem_palavras.to_file('nuvem_de_palavras.png')
