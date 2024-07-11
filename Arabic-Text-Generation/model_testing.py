import numpy as np
import tensorflow as tf
import random
import itertools
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

def model_testing_word(text, number_of_words, text_normalization, text_to_sequence, words_index, pad_sequences, model, max_length, index_to_words, word_sequence_to_text, all_words):
    for _ in range(number_of_words): 
        text = text_normalization(text)
        token_list = text_to_sequence(words_index , text)
        token_list = pad_sequences(padding='pre', input_sequence=[token_list], max_length=max_length-1)
        predicted_probs = model.predict(token_list, verbose=0) 
        index = np.argmax(predicted_probs)
        text += " " + word_sequence_to_text(index_to_words, [index], all_words)
    return text



def model_testing_char(text, number_of_chars, char_index, pad_sequences, model, max_length, index_char, text_to_sequence_char, all_chars, char_sequence_to_text):
    encoded_text = text_to_sequence_char(char_index, text)
    encoded_text = list(list(itertools.chain.from_iterable(encoded_text)))
    padded_text = pad_sequences(padding='post', input_sequence=[encoded_text], max_length=max_length-1)
    for _ in range(number_of_chars):
        predicted_probs = model.predict(padded_text, verbose=0)
        index = np.argmax(predicted_probs)
        text += char_sequence_to_text(index_char, [index], all_chars)
        padded_text = np.append(padded_text, index)
        padded_text = pad_sequences(padding='post', input_sequence=[padded_text], max_length=max_length-1)
    return text
