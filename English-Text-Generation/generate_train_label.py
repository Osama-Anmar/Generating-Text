def generate_train_label_word(Corpus, text_to_sequence, words_index, pad_sequences):
    input_sequence_ = []
    for line in Corpus:
        seq = text_to_sequence(words_index, line) # Convert Words To Integers
        for i in range(1, len(seq)):
            n_grams = seq[:i+1]
            input_sequence_.append(n_grams)
    max_length_word = max([len(x) for x in input_sequence_])
    input_sequence_ = pad_sequences(input_sequence=input_sequence_, max_length=max_length_word) #Add Zeros To Make All Sequences In Same Length
    train, labels = input_sequence_[:,:-1], input_sequence_[:,-1]
    return max_length_word, train, labels
     
def generate_train_label_char(Corpus, max_length_char):
    Text = " ".join(Corpus)
    Train = []
    Label = []
    for i in range(0, len(Text) - max_length_char):
        Train.append(Text[i: i + max_length_char])
        Label.append(Text[i + max_length_char])
    return Train, Label