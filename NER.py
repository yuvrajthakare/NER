#importing necessary libraries
import wikipedia    #wikipedia library for searching query.
import spacy_streamlit  #spacy_streamlit for NER and Visualization.
import streamlit as st  #stramlit application.

def home():
    #set title for stramlit application
    st.title("Named Entity Recognition")
    
    #This is the default text which will be searched in wikipedia by default and the result of NER will be displayed.
    DEFAULT_TEXT = """ Narendra Modi """

    #space has different nlp models we are using en_core_web_sm for Named-entity recognition.
    spacy_model = "en_core_web_sm"

    #input query is given to wikipedia and the result of that query given to the vaiable text.
    text = st.text_input("Wikipedia search", DEFAULT_TEXT)
    
    #exception handling in case of failure in the searched query.
    try:
        text = wikipedia.summary(text)
    except:
        pass

    #pocessing of the text and display using visualize_ner.    
    doc = spacy_streamlit.process_text(spacy_model, text)

    spacy_streamlit.visualize_ner(
        doc,
        labels=["PERSON", "DATE", "GPE", "ORG", "NORP"],
        show_table=False,
        title="Persons, dates and locations",
    )
    return st.text(f"Analyzed using spaCy model {spacy_model}")

#initializing application.
if __name__ == "__main__":
    home()
