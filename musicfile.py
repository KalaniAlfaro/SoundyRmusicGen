

###################################################################

##OLD VERSION  
from gradio_client import Client
import streamlit as st



params = st.experimental_get_query_params()
# Obtém o valor do parâmetro 'variavel' da URL
palavraChave = params.get('palavrachave', ['cavalo'])[0]

# Mostra o valor recebido na interface do Streamlit
##st.write("Valor da variável via GET:", palavraChave)
st.write("Por favor, aguarde sua música ser gerada!")

client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
				palavraChave,	# str  in 'Describe your music' Textbox component
				"https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath or URL to file) in 'File' Audio component
				fn_index=0
)
#nome e PATH do mp4
##st.write(result[0])


audio_file = open(result[0], 'rb')
audio_bytes = audio_file.read()

#player de audio sem autoplay
##st.audio(audio_bytes, format='audio/mp4')

def autoplay_audio(file_path: str):
    import base64

    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true" controls class="stAudio" style="width:100%">
            <source src="data:audio/mp4;base64,{b64}" type="audio/mp4">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


#st.write("# Auto-playing Audio!")

autoplay_audio(result[0])