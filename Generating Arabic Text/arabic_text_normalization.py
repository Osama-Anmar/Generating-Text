import re
def remove_arabic_tatweel(text):
                text = re.sub('ـ', '', text)
                return text

def remove_punctuations(text):     
        Punctuation  = '''“`؛،؟.,-!"\'(),-./:;?[–]^_`{}”'''
        for punctuation in Punctuation:
                text = text.replace(punctuation, ' ')
        return text

def remove_unicode_and_special_character(text):      
        Pattern = r'[\u2460-\u24FF\u2070-\u218F\u2022-\u221E\u0E3F\u00A9\u00AE\u2117\u2120\u03B1-\u03C9\u0391-\u039F\u00BC-\u00BE\u0022-\u0027\u002A\u002B\u002F\u003C-\u003E\u0040\u005C\u005E\u0060\u007C\u007E\u00BC-\u00BE]'+ "»" + "«"
        text = re.sub(Pattern, ' ', text)
        text = re.sub('["«»"]', '', text)
        return text

def text_normalization(text):
        text = remove_unicode_and_special_character(text)
        text = remove_arabic_tatweel(text)
        text = re.sub('[a-zA-Z]', '', text)
        text = remove_punctuations(text)
        text = re.sub('[\u200b\u200c\u200f]', '', text)
        text = re.sub(' +', ' ', text)
        text = text.strip()
        return text
