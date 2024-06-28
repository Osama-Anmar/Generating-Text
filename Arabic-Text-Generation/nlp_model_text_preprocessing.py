import pandas as pd
import numpy as np

def index_the_words(Corpus):
    df = pd.DataFrame(Corpus) 
    words = set()
    for word in df[0].str.split(): 
        words.update(word) 
    words = sorted(words)
    all_words = len(words) 
    words_to_index = {word:index for index, word in enumerate(words)}
    index_to_word = {word:index for word, index in enumerate(words)}
    words_to_index['OOV'] = all_words
    index_to_word[all_words] = "OOV"
    return all_words, words_to_index, index_to_word


def text_to_sequence(word_index, text):
    sequence_text = [word_index[word] if word in word_index else word_index["OOV"] for word in text.split()]
    return sequence_text


def pad_sequences(padding = 'pre', input_sequence = None, max_length = None, truncating = 'pre'):
    for i in range(0, len(input_sequence)):
        while len(input_sequence[i]) < max_length:
            if padding == "post":
               input_sequence[i].insert(len(input_sequence[i]), 0)
            if padding == 'pre':
                input_sequence[i].insert(0, 0)
        if truncating == 'pre':
             input_sequence[i] =  input_sequence[i][-max_length:]
        if truncating == 'post':
             input_sequence[i] =  input_sequence[i][:max_length]
    return  np.array(input_sequence)

def one_hot_encoding(labels, all_words):
     label = np.zeros((len(labels), all_words))
     for i, j in enumerate(labels):
            label[i, j] = 1
     return label

def index_the_char(Corpus):
    chars = set()
    for char in Corpus:
        chars.update(char)
    chars = sorted(chars)
    all_chars = len(chars) 
    chars_index = {char:index for index, char in enumerate(chars)}
    index_chars = {char:index for char, index in enumerate(chars)}
    chars_index['OOV'] = all_chars
    index_chars[all_chars] = "OOV"
    return all_chars, chars_index, index_chars

def text_to_sequence_char(chars_index, text):
     sequence_text_char = [[chars_index[char] for char in sentences] for sentences in text]
     return sequence_text_char
