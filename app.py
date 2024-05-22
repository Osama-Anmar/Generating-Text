import tensorflow as tf
import streamlit as st
import pickle
import numpy as np

with open('arabic_tokenizer.pickle', 'rb') as handle:
    Arabic_tokenizer = pickle.load(handle)

with open('english_tokenizer.pickle', 'rb') as handle:
    English_tokenizer = pickle.load(handle)

Arabic_Model = tf.keras.models.load_model('Arabic_GRU.h5')
English_Model = tf.keras.models.load_model('English_LSTM.h5')


st.title('Simple Text Genarating WebApp')

with st.sidebar:
    Input = st.text_input('Insert The Text', value="")
    Number = st.number_input('Insert Number Of Words', min_value=1, max_value=500) 
    Language = st.radio('Language', ['Arabic', 'English'], index=None)
    if Language == 'Arabic':   
        if st.button('Generate Text'):
           for _ in range(Number): 
                    token_list = Arabic_tokenizer.texts_to_sequences([Input])[0] 
                    token_list = tf.keras.utils.pad_sequences([token_list], maxlen=167, padding='pre') 
                    predicted_probs = Arabic_Model.predict(token_list, verbose=0) 
                    word = Arabic_tokenizer.index_word[np.argmax(predicted_probs)] 
                    Input += " " + word 


    if Language == 'English':   
        if st.button('Generate Text'):
           for _ in range(Number): 
                    token_list = English_tokenizer.texts_to_sequences([Input])[0] 
                    token_list = tf.keras.utils.pad_sequences([token_list], maxlen=93, padding='pre') 
                    predicted_probs = English_Model.predict(token_list, verbose=0) 
                    word = English_tokenizer.index_word[np.argmax(predicted_probs)] 
                    Input += " " + word 

st.write(Input)




