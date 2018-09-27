import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import  WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

import spacy


class NlpRecognizer:

    def __init__(self):

        self.myText = "Create an array of 10 numbers. Initialize the elements to 0"

        #self.nltkTest()
        self.spacyTest()

    def nltkTest(self):    
        myText = self.myText.lower()

        sentences  = sent_tokenize(myText)

        lem = WordNetLemmatizer()
        stemmer = PorterStemmer()


        stop_words = set(stopwords.words('english'))

        for sentence in sentences:

            words = word_tokenize(sentence)
            print(words)

            filtered_sentence = [w for w in words if w not in stop_words]

            print(filtered_sentence)

            lemmed_sentence = [lem.lemmatize(w) for w in filtered_sentence]
            print(lemmed_sentence)

            stemmed_sentence = [stemmer.stem(w) for w in filtered_sentence]
            print(stemmed_sentence)

            tags = nltk.pos_tag(words)
            print(tags)

            # namedEnt = nltk.ne_chunk(tags, binary=False)
            # namedEnt.draw() 

            print("++++++++++")
    

    def spacyTest(self):
        
        nlp = spacy.load('en')
        #nlp = spacy.load('custom_ner_model')
        # nlp = spacy.load('en_core_web_sm')
        doc  = nlp(u'apple')

        for token in doc:
            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
                token.shape_, token.is_alpha, token.is_stop)
    
        
        spacy.displacy.render(doc, style='dep', page=True)





def main():
    _ = NlpRecognizer()

if __name__ == '__main__':
    main()