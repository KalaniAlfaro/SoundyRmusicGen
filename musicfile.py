


###################################################################
from gradio_client import Client
import streamlit as st
import os

# ... Restante do seu código ...

params = st.experimental_get_query_params()
palavraChave = params.get('palavrachave', ['cavalo'])[0]

client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
    palavraChave,
    "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
    fn_index=0
)

# Depuração: Imprimir informações sobre result
print("Tipo de result:", type(result))
print("Conteúdo de result:", result)

# Verificar o tipo e conteúdo de result antes de tentar abri-lo
if isinstance(result, str):
    if os.path.exists(result):
        audio_file = open(result, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp4', start_time=0)
    else:
        st.error(f"O resultado da previsão não é um caminho de arquivo válido: {result}")
else:
    st.error(f"O resultado da previsão não é do tipo esperado (str): {result}")