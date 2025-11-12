import streamlit as st 
import gtts as gtts 
from gtts import gTTS

st.set_page_config(page_title=None, page_icon=":statue_of_liberty:", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.title("Welcome!")
st.subheader("Módulo básico de inglês: A1-A2")

col_txt, col_options = st.columns(2)
with col_txt:
    st.write("""
    Bem-vindo ao seu ambiente de estudos!  
    Escolha qual aula quer fazer agora!
    """)
with col_options:
    #st.download_button("Download Livro") 
    #Pix (QR Code)
    st.button("Teste Final")
    

col1, col2, col3, col4, col5 = st.columns(5, gap="small")

with col1:
    aulaA = st.radio("",
             ["Introdução","Aula 1","Aula 2","Aula 3"],
             index=None)
with col2:
    aulaB = st.radio("",
             ["Aula 4","Aula 5","Aula 6","Aula 7"],
             index=None)
with col3:
    aulaC = st.radio("",
             ["Aula 8","Aula 9","Aula 10","Aula 11"],
             index=None)
with col4:
    aulaD = st.radio("",
             ["Aula 12","Aula 13","Aula 14","Aula 15"],
             index=None)

@st.cache_data
def audio_generator(audio_file):
    audio_list = []
    if audio_file in text_dic:
        text_to_audio = audio_file
        text_value = text_dic[audio_file]
        speech_name = text_value + '.mp3'
        speech = gTTS(text=text_to_audio, lang='en', slow=False)
        speech.save(speech_name)
        st.audio(speech_name, format="audio/mpeg", loop=False)
        audio_list.append(speech)
        return audio_list
    
if aulaA == "Introdução":
    st.write("Video aula")
    st.write("Listening and pronunciation")
    col_values, col_audio=st.columns(2, gap='large')

col_values, col_audio = st.columns(2, gap="small")

with col_values:
    audio_file = st.radio(
        "Escolha uma opção para ouvir o áudio:", 
        ["Good morning",
         "Good afternoon",
         "Good evening",
         "Good night",
         "Excuse me",
         "I beg your pardon",
         "I'm sorry",
         "Thank you",
         "Thank's",
         "You’re welcome",
         "Goodbye",
         "See you later"], 
        index=None)

    text_dic={"Good morning":"good_morning",
              "Good afternoon":"good_afternoon",
              "Good evening": "good_evening",
              "Good night":"good_night",
              "Excuse me":"excuse_me",
              "I beg your pardon":"beg_pardon",
              "I'm sorry":"im_sorry",
              "Thank you":"thank_you",
              "Thank's":"thanks",
              "You’re welcome":"you_welcome",
              "Goodbye":"good_bye",
              "See you later":"see_later"}
    with col_audio:
        if audio_file in text_dic:
            audio_generator(audio_file)
            #######
            st.write("Repita em voz alta, para treinar sua pronúncia e escreva em um papel, para treinar a escrita.")
            audio_value = st.audio_input("Grave aqui sua pronúncia:")
            #if audio_value is not None:
                #st.audio(audio_value)