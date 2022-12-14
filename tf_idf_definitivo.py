'''1. Sua tarefa será gerar a matriz termo-documento usando TF-IDF por meio da aplicação das 
fórmulas  TF-IDF  na  matriz  termo-documento  criada  com  a  utilização  do  algoritmo  Bag of 
Words. Sobre o Corpus que recuperamos anteriormente. O entregável desta tarefa é uma 
matriz termo-documento onde a primeira linha são os termos e as linhas subsequentes são 
os vetores calculados com o TF-IDF. 

    2. Sua tarefa será gerar uma matriz de distância, computando o cosseno do ângulo entre todos 
os vetores que encontramos usando o tf-idf. Para isso use a seguinte fórmula para o cálculo 
do  cosseno  use  a  fórmula  apresentada  em  Word2Vector  (frankalcantara.com) 
(https://frankalcantara.com/Aulas/Nlp/out/Aula4.html#/0/4/2)  e  apresentada  na  figura  a 
seguir:  
    
    O resultado deste trabalho será uma matriz que relaciona cada um dos vetores já calculados 
com todos os outros vetores disponíveis na matriz termo-documento mostrando a distância 
entre cada um destes vetores.'''

from bs4 import BeautifulSoup
import numpy as num
import requests

# Para pegar textos de 5 websites diferentes e colocar em uma lista de listas (c) e uma lista (lC) 
# com o nome do website de onde o texto foi pego
c = []
lC = []
#url do site
url1 = "https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1"
#fazendo a requisição
h1 = requests.get(url1)
#pegando o nome do site2 
url2 = "https://www.ibm.com/cloud/learn/natural-language-processing"
#fazendo a requisição 
h2 = requests.get(url2)
#pegando o nome do site3
url3 = "https://en.wikipedia.org/wiki/Natural_language_processing"
#fazendo a requisição
h3 = requests.get(url3)
#pegando o nome do site4
url4 = "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"
#fazendo a requisição
h4 = requests.get(url4)
#pegando o nome do site5
url5 = "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"
#fazendo a requisição
h5 = requests.get(url5)

#pegando o conteúdo
sp1 = BeautifulSoup(h1.text,"html.parser")
#pegando o texto
sentensas1 = sp1.find_all("p")
for url1 in sentensas1:
  c.append(url1.get_text())
#pegando o conteúdo
sp2 = BeautifulSoup(h2.text,"html.parser")
#pegando o texto
sentensas2 = sp2.find_all("p")
for url2 in sentensas2:
  c.append(url2.get_text())
#pegando o conteúdo
sp3 = BeautifulSoup(h3.text,"html.parser")
#pegando o texto
sentensas3 = sp3.find_all("p")
for url3 in sentensas3:
  c.append(url3.get_text())
#pegando o conteúdo
sp4 = BeautifulSoup(h4.text,"html.parser")
#pegando o texto
sentensas4 = sp4.find_all("p")
for url4 in sentensas4:
  c.append(url4.get_text())
#pegando o conteúdo
sp5 = BeautifulSoup(h5.text,"html.parser")
#pegando o texto
sentensas5 = sp5.find_all("p")
for url5 in sentensas5:
  c.append(url5.get_text())

lC.append(c)


# Para remover os caracteres especiais e deixar apenas letras e números e 
# colocar em uma lista de listas (c2) e uma lista (lC2) 
T = []
QTDsent = 0
for c in lC:
  for sent in c:
    QTDsent += 1
    for t in sent.split(' '):
      if t not in T:
        T.append(t)
BAG = num.zeros((QTDsent,len(T)))
Sat = 0
for c in lC:
  for sents in c:
    for t in sents.split(' '):
      BAG[Sat][T.index(t)] += 1
    Sat += 1

# Para criar um dataframe com a quantidade de palavras de cada sentença e 
# o nome do website de onde o texto foi pego 
TF = num.zeros((len(BAG),len(BAG[0])))
Sat = 0
for c in lC:
  for sents in c:
    QtdT = len(sents.split(' '))
    for t in sents.split(' '):
      TF[Sat][T.index(t)] = BAG[Sat][T.index(t)] / QtdT
    Sat += 1

print("TF: ")
print(" ")
print(" ")
print(TF)

IDF = []
for t in range(len(T)):
  Tver = 0
  for sentsV in BAG:
    if sentsV[t] > 0: Tver += 1
  IDF.append(num.log10(len(BAG)/Tver))

print(" ")
print(" ")
print("IDF: ")
print(" ")
print(" ")
print(IDF)

TFIDF = num.zeros((len(BAG),len(BAG[0])))
for sents in range(len(BAG)):
    for t in range(len(T)):
        TFIDF[sents][t] = TF[sents][t] * IDF[t]

print(" ")        
print(" ")
print("TFIDF: ")
print(" ")
print(" ")
print(TFIDF)

MD = num.zeros((len(TFIDF),len(TFIDF)))

V = 0

# Para criar uma matriz de distância euclidiana entre as sentenças
for v in TFIDF:
  g = V
  while g < len(TFIDF):
    D = num.dot(v,TFIDF[g])/(num.linalg.norm(v)*num.linalg.norm(TFIDF[g]))
    MD[V][g] = D
    MD[g][V] = D
    V += 1
    g += 1

print(" ")
print(" ")
print("Matriz de Distancia Cosceno: ")
print(" ")
print(" ")
print(MD)
