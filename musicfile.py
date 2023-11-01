from gradio_client import Client
import streamlit as st


client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'Describe your music' Textbox component
				"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath or URL to file) in 'File' Audio component
				fn_index=0
)
st.write(result)

from base64 import b64encode
from pathlib import Path
from streamlit_player import st_player

def local_video(path, mime="video/mp4"):
    data = b64encode(Path(path).read_bytes()).decode()
    return [{"type": mime, "src": f"data:{mime};base64,{data}"}]

st_player(local_video(result))



st_player(result)