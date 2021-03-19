# Namd Entity Recognition
link to the app : https://named-entity-recognition1.herokuapp.com/

1. Create a [streamlit] (https://www.streamlit.io/) application.
2. install **spacy_streamlit** and **wikipedia** library using: 
    ..* `pip install spacy streamlit`
    ..* `pip install wikipedia`
3. Also install en_core_web_sn model using `python -m spacy download en_core_web_sm` from spacy models. This model is used for named-entity recognition.
4. Scrape data from wikipedia to perform **NER**.
5. Perform Named Entity Recognition on scrapped data and extract entities like **city, person, organisation, Date, Geographical Entity, Product** etc.
6. Display annotated text in Streamlit App.
7. Run thi streamlit app using `streamlit run NER.py`.
8. Inline-style: 
![alt text](https://github.com/yuvrajthakare/NER/blob/main/image1.png "input")
Inline-style: 
![alt text](https://github.com/yuvrajthakare/NER/blob/main/image2.png "output")
