import numpy as np
import tensorflow as tf
import random
random.seed(42)
np.random.seed(42)
tf.random.set_seed(42)

def model_testing_word(text, number_of_words, text_normalization, text_to_sequence, words_index, pad_sequences, model, max_length, index_to_words):
    for _ in range(number_of_words): 
        text = text_normalization(text)
        token_list = text_to_sequence(words_index , text)
        token_list = pad_sequences(padding='pre', input_sequence=[token_list], max_length=max_length-1)
        predicted_probs = model.predict(token_list, verbose=0) 
        index = np.argmax(predicted_probs)
        text += " " + index_to_words[index]
        print(text)
    print(" ")
    print("Full Generated Text:", text)


def model_testing_char(text, number_of_chars, char_index, pad_sequences, model, max_length, index_char, temperature=1.0):
    for _ in range(number_of_chars):
        token_list = [char_index[char] for char in text if char in char_index]
        token_list = pad_sequences(padding='post', input_sequence=[token_list], max_length=max_length-1)
        predicted_probs = model.predict(token_list, verbose=0)[0]
        
        # Apply temperature scaling
        predicted_probs = np.log(predicted_probs) / temperature
        exp_preds = np.exp(predicted_probs)
        predicted_probs = exp_preds / np.sum(exp_preds)
        index = np.random.choice(len(predicted_probs), p=predicted_probs)
        text += index_char[index]
        print(text.title())
        
    print("Full Generated Text:", text.title())


