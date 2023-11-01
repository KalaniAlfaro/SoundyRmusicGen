from gradio_client import Client
import streamlit as st


client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'Describe your music' Textbox component
				"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath or URL to file) in 'File' Audio component
				fn_index=0
)
st.write(result)

import numpy as np

audio_file = open(result, 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp4')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)