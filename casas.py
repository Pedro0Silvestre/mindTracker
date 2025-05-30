import streamlit as st
from dashboards import grafico_depressao 
from dashboards import grafico_ansiedade
from dashboards import grafico_estresse# importa a função correta

st.title("Relatórios de Saúde mental")

fig = grafico_depressao()  # chama a função para gerar a figura
st.pyplot(fig)  # mostra o gráfico no Streamlit

fig_ansiedade = grafico_ansiedade() 
st.pyplot(fig_ansiedade) 
fig_estresse = grafico_estresse()
st.pyplot(fig_estresse)  


