from nltk.corpus import stopwords
import re
import string
import qalsadi.lemmatizer

punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ''' + string.punctuation

# Arabic stop words with nltk
stop_words = stopwords.words("arabic")
stop_words.append("و")

arabic_diacritics = re.compile("""
                             ّ    | # Shadda
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)

def preprocess(text):
    
    '''
    text is an arabic string input
    
    the preprocessed text is returned
    '''
    
    #remove punctuations
    translator = str.maketrans('', '', punctuations)
    text = text.translate(translator)
    
    # remove Tashkeel
    text = re.sub(arabic_diacritics, '', text)
    
    #remove longation
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)

    text = ' '.join(word for word in text.split() if word not in stop_words)

    lemmer = qalsadi.lemmatizer.Lemmatizer()
    lemmetized = lemmer.lemmatize_text(text)

    return lemmetized

def preprocess_all(text_list):
    preprocessed_texts = []
    for index,text in enumerate(text_list):
        preprocessed_text = preprocess(text)
        if index % 2 == 0:
            preprocessed_texts.append(','.join(preprocessed_text)
        else:
            preprocessed_texts.append('؛'.join(preprocessed_text))
    return preprocessed_texts
        