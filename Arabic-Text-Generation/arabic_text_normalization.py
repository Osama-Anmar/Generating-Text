import re
def remove_arabic_tatweel(text):
                text = re.sub('ـ', '', text)
                return text

def remove_punctuations(text):     
        Punctuation  = '''“`؛،؟.,-!"\'(),-./:;?[–]^_`{}\\”'''
        for punctuation in Punctuation:
                text = text.replace(punctuation, ' ')
        return text

def remove_unicode_and_special_character(text):            
        Pattern = r'[\u2460-\u24FF\u2070-\u218F\u0024\u00A2-\u00A5\u20BA\u2022-\u221E\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u003C-\u003E\u00AE\u00A9\u00AE\u2117\u2120\u005E\u007C\u002A\u0040\u007E\u002B]'
        text = re.sub(Pattern, ' ', text)
        text = re.sub('["«»"]', '', text)
        return text

def text_normalization(text):
        text = re.sub("\x7f", "", text)
        text = remove_unicode_and_special_character(text)
        text = remove_arabic_tatweel(text)
        text = re.sub('[a-zA-Z]', '', text)
        text = remove_punctuations(text)
        text = re.sub('[\u200b\u200c\u200f]', '', text)
        text = re.sub(' +', ' ', text)
        text = text.strip()
        return text