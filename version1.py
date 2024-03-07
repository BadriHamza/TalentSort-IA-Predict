# streamlit_app.py

import streamlit as st
import joblib
import pandas as pd
import pickle
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords
import numpy as np


# Charger le modèle TF-IDF
model_path = "models/tf_idf_model.joblib"
#with open(model_path, 'rb') as model_file:
    #tfidf_model = pickle.load(model_file)
tfidf_model = joblib.load('models/tf_idf_model.joblib')


def predict_category(text):
    # Prétraitement du texte (assurez-vous que c'est le même que celui utilisé pour l'entraînement)
    # ...

    # Utiliser le modèle TF-IDF pour la prédiction
    # ...

    return prediction
# Fonction pour effectuer la prédiction
#st.markdown("""# This is a header
## This is a sub header
#This is text""")

#df = pd.DataFrame({
#    'first column': list(range(1, 11)),
#    'second column': np.arange(10, 101, 10)
#})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
#line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
#head_df = df.head(line_count)

#head_df

# Interface utilisateur Streamlit
def main():
    st.title("CV Category Prediction")

    # Zone de texte pour entrer le CV
    user_input = st.text_area("Entrez le CV ici:", "")

    # Bouton de prédiction
    if st.button("Prédire la catégorie"):
        # Appeler la fonction de prédiction
        prediction = predict_category(user_input)

        # Afficher le résultat
        st.success(f"Catégorie prédite: {prediction}")

if __name__ == "__main__":
    main()
