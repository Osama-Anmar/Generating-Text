import numpy as np


def index_the_words(Corpus):
    words = set() 
    for text in Corpus:
        for word in text.split():
            words.add(word)
    words = sorted(words)
    all_words = len(words) 
    words_to_index = {word:index+2 for index, word in enumerate(words)} 
    index_to_word = {word:index+2 for word, index in enumerate(words)}
    words_to_index['UNK'] = 1
    index_to_word[1] = "UNK"
    return all_words + 1, words_to_index, index_to_word


def text_to_sequence(word_index, text):
    sequence_text = [word_index[word] if word in word_index else word_index["UNK"] for word in text.split()]
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
    chars_index = {char:index + 2 for index, char in enumerate(chars)}
    index_chars = {char:index + 2 for char, index in enumerate(chars)}
    chars_index['UNK'] = 1
    index_chars[1] = "UNK"
    return all_chars + 1, chars_index, index_chars

def text_to_sequence_char(chars_index, text):
     sequence_text_char = [[chars_index[char] if char in chars_index else chars_index["UNK"] for char in sentences] for sentences in text]
     return sequence_text_char

def char_sequence_to_text(index_chars, sequence):
     char_seq_to_text_ = [index_chars[index] if index in index_chars else index_chars[1] for index in sequence]
     return "".join(char_seq_to_text_)

def word_sequence_to_text(index_to_words, sequence):
     word_sequence_to_text_ = [index_to_words[index] if index in index_to_words else index_to_words[1] for index in sequence]
     return " ".join(word_sequence_to_text_)