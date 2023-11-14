


###################################################################
from gradio_client import Client
import streamlit as st
import os
st.write("Hello, World!")

from gradio_client import Client
import streamlit as st



params = st.experimental_get_query_params()
# Obtém o valor do parâmetro 'variavel' da URL
palavraChave = params.get('palavrachave', ['cavalo'])[0]

# Mostra o valor recebido na interface do Streamlit
st.write("Valor da variável via GET:", palavraChave)

from gradio_client import Client

client = Client("https://facebook-musicgen.hf.space/")
result = client.predict(
				"Howdy!",	# str  in 'parameter_16' Dataset component
				fn_index=2
)
print(result)



