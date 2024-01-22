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

def start_fastapi():
    cmd = "uvicorn api.app:app --host 0.0.0.0 --port 8080 --reload"
    subprocess.Popen(cmd, shell=True)

start_fastapi()
main()