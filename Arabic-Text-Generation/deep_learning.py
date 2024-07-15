import tensorflow as tf 
import matplotlib.pyplot as plt

def nlp_model_word(input_dim, output_dim, input_length, unit, model):
    model = tf.keras.models.Sequential([
                tf.keras.layers.Embedding(input_dim=input_dim, output_dim=output_dim, input_length=input_length-1),
                model,
                tf.keras.layers.Dense(unit, activation='softmax')
                ])   
    return model

def nlp_model_char(input_dim, output_dim, unit, model, input_length):
    model = tf.keras.models.Sequential([
                tf.keras.layers.Embedding(input_dim=input_dim, output_dim=output_dim, input_length=input_length),
                model,
                tf.keras.layers.Dense(unit, activation='softmax')
                ])   
    return model

def model_compile_word(model, optimizer, loss, metrics):
    return model.compile(optimizer=optimizer,
                         loss=loss,
                         metrics=metrics)

def model_compile_char(model, optimizer, loss):
    return model.compile(optimizer=optimizer,
                         loss=loss)
    
def model_fit(model, Data, Label, epochs, early_stop, checkpoint,batch_size):       
    history = model.fit(Data, Label,
                        epochs=epochs,
                        batch_size=batch_size,
                        callbacks=[early_stop, checkpoint])
    return history

def plot_word_model_change(history):
    accuracy = history.history['accuracy']
    loss = history.history['loss'] 
    plt.plot(accuracy, label='Accuracy')
    plt.plot(loss, label='Loss')
    plt.legend()
    return plt.show() 

def plot_char_model_change(history):
    loss = history.history['loss'] 
    plt.plot(loss, label='Loss')
    plt.legend()
    return plt.show() 
