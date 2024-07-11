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
        print(text)
    print(" ")
    print("Full Generated Text:", text)



def model_testing_char(text, number_of_chars, char_index, pad_sequences, model, max_length, index_char, text_to_sequence_char, all_chars, char_sequence_to_text):
    for _ in range(number_of_chars): 
        token_list = text_to_sequence_char(char_index, text)
        token_list = list(list(itertools.chain.from_iterable(token_list)))
        token_list = pad_sequences(padding='post', input_sequence=[token_list], max_length=max_length-1)
        predicted_probs = model.predict(token_list, verbose=0) 
        index = np.argmax(predicted_probs)
        text += "" + char_sequence_to_text(index_char, [index], all_chars)
        print(text)
    print(" ")
    print("Full Generated Text:", text)


