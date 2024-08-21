# Generating-Text
This repository contains a project focused on text generation using deep learning models. The primary goal is to generate coherent and contextually relevant text based on a given input.

# Files
* deep_learning.py
* english_text_normalization.py
* generate_train_label.py
* model_checkpoint.py
* model_testing.py
* nlp_model_text_preprocessing.py
* read_data.py
* transformers.py

# Overview
The project leverages sequence models like LSTMs (Long Short-Term Memory networks), or Transformers to generate text. These models are trained on a large corpus of text data to learn the patterns and structures of language.

# Preprocessing
Preprocessing steps include:

* Tokenization: Splitting text into tokens or words.
* Text Normalization: Converting text to lowercase, removing special characters, etc.
* Sequence Padding: Ensuring that all input sequences are of the same length.
 
# Model
Several models have been explored for text generation, including:

* LSTM (Long Short-Term Memory)
* GRU (Gated Recurrent Unit)
* Transformer

# Training
The model is trained on the preprocessed text data using a sequence-to-sequence approach. The training process involves tuning hyperparameters such as learning rate, batch size, and the number of epochs to achieve the best performance.

# Installation
```bash
git clone https://github.com/Osama-Anmar/Generating-Text.git
cd Generating-Text
pip install -r requirements.txt
```
# Usage
To generate text using the trained model, follow these steps:

* 1-Load the trained model.
* 2-Provide a starting sequence or prompt.
* 3-Generate text based on the input sequence.

```bash
from model_testing import model_testing_word
model_testing_word(text = 'The only things', number_of_words = 50, text_normalization = text_normalization, text_to_sequence = text_to_sequence, words_index = words_index, pad_sequences = pad_sequences, checkpoint_filepath='English_GRU1_model_checkpoint.h5', max_length = max_length_word, index_to_words = index_to_words, word_sequence_to_text = word_sequence_to_text, all_words=all_words)
```
# Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or improvements.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

