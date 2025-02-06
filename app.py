#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import os
import time
import glob
import os


from gtts import gTTS
from googletrans import Translator

try:
    os.mkdir("temp")
except:
    pass
st.title("Text to speech in different languages with proper listening voice")
st.image("text-to-speech-converter.png")
translator = Translator()

text = st.text_input("Enter text")
in_lang = st.selectbox(
    "Select your input language",
    ("English", "Hindi","Urdu", "Bengali","Marathi","Kannada","Gujrati","Malyalam","Tamil","Nepali","French","German","Greek","Russian","korean", "Chinese", "Japanese"),
)

if in_lang == "English":
    input_language = "en"
elif in_lang == "Hindi":
    input_language = "hi"
elif in_lang == "Urdu":
    input_language = "ur"           
elif in_lang == "Bengali":
    input_language = "bn"    
elif in_lang == "Marathi":
    input_language = "mr"
elif in_lang == "Kannada":
    input_language = "kn"
elif in_lang == "Gujrati":
    input_language = "gu"
elif in_lang == "Malyalam":
    input_language = "ml" 
elif in_lang == "Tamil":
    input_language = "ta"    
elif in_lang == "Nepali":
    input_language = "ne"
elif in_lang == "French":
    input_language = "fr" 
elif in_lang == "German":
    input_language = "de" 
elif in_lang == "Greek":
    input_language = "el" 
elif in_lang == "Russian":
    input_language = "ru"
elif in_lang == "korean":
    input_language = "ko"
elif in_lang == "Chinese":
    input_language = "zh-cn"
elif in_lang == "Japanese":
    input_language = "ja" 
    
    
    

out_lang = st.selectbox(
    "Select your output language",
   ("English", "Hindi","Urdu", "Bengali","Marathi","Kannada","Gujrati","Malyalam","Tamil","Nepali","French","German","Greek","Russian","korean", "Chinese", "Japanese"),
)
if out_lang == "English":
    output_language = "en"
elif out_lang == "Hindi":
    output_language = "hi"
elif out_lang == "Urdu":
    output_language = "ur"       
elif out_lang == "Bengali":
    output_language = "bn"
elif out_lang == "Marathi":
    output_language = "mr"
elif out_lang == "Kannada":
    output_language = "kn"
elif out_lang == "Gujrati":
   output_language = "gu"
elif out_lang == "Malyalam":
    output_language = "ml" 
elif out_lang == "Tamil":
    output_language = "ta" 
elif out_lang == "Nepali":
    output_language = "ne"
elif out_lang == "French":
    output_language = "fr" 
elif out_lang == "German":
    output_language = "de" 
elif out_lang == "Greek":
    output_language = "el" 
elif out_lang == "Russian":
    output_language = "ru"
elif out_lang == "korean":
    output_language = "ko"
elif out_lang == "Chinese":
    output_language = "zh-cn"
elif out_lang == "Japanese":
    output_language = "ja"

english_accent = st.selectbox(
    "Select your english accent",
    (
        "Default",
        "India",
        "United Kingdom",
        "United States",
        "Canada",
        "Australia",
        "Ireland",
        "South Africa",
    ),
)

if english_accent == "Default":
    tld = "com"
elif english_accent == "India":
    tld = "co.in"

elif english_accent == "United Kingdom":
    tld = "co.uk"
elif english_accent == "United States":
    tld = "com"
elif english_accent == "Canada":
    tld = "ca"
elif english_accent == "Australia":
    tld = "com.au"
elif english_accent == "Ireland":
    tld = "ie"
elif english_accent == "South Africa":
    tld = "co.za"


def text_to_speech(input_language, output_language, text, tld):
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts = gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:500]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


display_output_text = st.checkbox("Display output text")

if st.button("convert"):
    result, output_text = text_to_speech(input_language, output_language, text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown(f"## Output text:")
        st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(10)

