import csv
import re
import nltk
import spacy
#import natasha
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from spacy.lang.ru.examples import sentences



with open('test_data - Copy.csv', 'r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)
    regExpCompl = re.compile ('[^a-zA-Zа-яА-Я ]')


    for row in reader:
        cleaned_review = regExpCompl.sub('', ', '.join(row).lower())
        tokens = nltk.word_tokenize(cleaned_review)
        if row[2] == 'manager' and ('здравствуйте' in tokens or ('добрый' and 'день') in tokens or 'привет' in tokens):
          print (', '.join(row))


with open('test_data - Copy.csv', 'r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)
    regExpCompl = re.compile ('[^a-zA-Zа-яА-Я ]')
    for row in reader:
        cleaned_review = regExpCompl.sub('', ', '.join(row).lower())
        tokens = nltk.word_tokenize(cleaned_review)        
        if row[2] == 'manager' and 'зовут' in tokens:
            print (', '.join(row))

# with open('test_data - Copy.csv', 'r', encoding="utf8") as csv_file:
#    reader = csv.reader(csv_file)
 #   morph_vocab = MorphVocab()
  #  for row in reader:
  #      print(row[3])
  #      doc = Doc(row[3])
  #      doc.segment(Segmenter())
  #      emb = NewsEmbedding()
  #      doc.tag_morph(NewsMorphTagger(emb))
  #      doc.tag_ner(NewsNERTagger(emb))
  #      names_extractor = NamesExtractor(morph_vocab)
  #      for span in doc.spans:
  #          if span.type == PER:
  #              span.extract_fact(names_extractor)
#
 #       print([_.fact.as_dict for _ in doc.spans if _.type == PER])


with open('test_data - Copy.csv', 'r', encoding="utf8") as csv_file:
    reader = csv.reader(csv_file)
    regExpCompl = re.compile ('[^a-zA-Zа-яА-Я ]')
    for row in reader:
        nlp = spacy.load('ru_core_news_sm')
        my_stopwords = ['Ага', 'Угу', 'эм', 'эр']
        doc = nlp(row[3])
        cleaned_review = regExpCompl.sub('', ', '.join(row).lower())
        tokens = nltk.word_tokenize(cleaned_review)    
        for token in doc:    
            if row[2] == 'manager' and 'зовут' in tokens and token.pos_ in ['PROPN']:
                print (token.text, token.pos_)



#with open('test_data - Copy.csv', 'r', encoding="utf8") as csv_file:
#    reader = csv.reader(csv_file)
#    for row in reader:
#        nlp = spacy.load('ru_core_news_sm')
#        my_stopwords = ['Ага', 'Угу', 'эм', 'эр']
#        doc = nlp(row[3])
#        for token in doc:
#            if token.pos_ in ['PROPN'] and row[2] == 'manager' and token.text not in my_stopwords:
#                print(token.text, token.pos_)


        
    






