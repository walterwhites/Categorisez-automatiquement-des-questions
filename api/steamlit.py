import requests
import streamlit as st
import subprocess

api_url = "https://categorisez-automatiquement-des-questions-5k9epyoc4gkbruabktk8.streamlit.app/models/supervised/predict/"

def main():
    st.title("Votre Application Streamlit")
    title = st.text_input("Titre")
    body = st.text_area("Corps")

    if st.button("Prédire"):
        with st.spinner("En cours de prédiction..."):
            data = {"title": title, "body": body}
            response = requests.post(api_url, json=data)
            prediction = response.json()
            st.write("Prédiction:", prediction)

if __name__ == "__main__":
    main()