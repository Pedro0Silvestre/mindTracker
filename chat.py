import streamlit as st
from app.risk import calcular_pontuacao_por_sintoma
from app.nlp import analisar_emocoes

st.set_page_config(page_title="MindTrack IA", layout="centered")

# Inicialização do session_state — só 1 vez no topo do script
if 'started' not in st.session_state:
    st.session_state.started = False
if 'indice_pergunta' not in st.session_state:
    st.session_state.indice_pergunta = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = []
if 'input_resposta' not in st.session_state:
    st.session_state.input_resposta = ""

# --- CSS customizado ---
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 2rem 3rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333333;
    }
    h1 {
        color: #4a90e2;
        font-weight: 700;
        font-size: 2.8rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    .pergunta {
        background-color: #e1f0ff;
        padding: 15px 20px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-weight: 600;
        color: #004a99;
        font-size: 1.15rem;
    }
    .resposta {
        background-color: #dff0d8;
        padding: 15px 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        font-size: 1.1rem;
        color: #3c763d;
    }
    div.stButton > button {
        background-color: #4a90e2;
        color: white;
        font-weight: 600;
        padding: 0.5rem 2rem;
        border-radius: 8px;
        transition: background-color 0.3s ease;
        margin-top: 10px;
    }
    div.stButton > button:hover {
        background-color: #357abd;
        color: #fff;
    }
    .resultado {
        background-color: #fff3cd;
        border-left: 8px solid #ffecb5;
        padding: 15px 20px;
        border-radius: 8px;
        margin-top: 20px;
        font-size: 1.2rem;
        font-weight: 600;
        color: #856404;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>🧠 Mind Tracker IA</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# Dados das perguntas
perguntas = [
    {"texto": "O que você aprendeu sobre você nos últimos 12 meses?"},
    {"texto": "Como foram suas amizades ao longo da vida?"},
    {"texto": "O que teve ocupado mais espaço na sua cabeça atualmente e como isso faz você se sentir?"},
    {"texto": "Qual a última situação que você se sentiu desafiado? Como lidou com isso?"},
    {"texto": "O que teve ocupado mais espaço na sua cabeça atualmente e como isso faz você se sentir?"},
]

# Funções auxiliares

def gerar_mensagem_mock(risco_total):
    if risco_total < 2:
        return "Baixo", "Você parece estável emocionalmente. Continue cuidando de si!"
    elif risco_total < 5:
        return "Moderado", "Alguns sinais de estresse foram detectados. Que tal fazer uma pausa?"
    else:
        return "Alto", "Sinais intensos de estresse. Considere procurar apoio profissional."

def nivel_risco(score):
    if score < 0.4:
        return "Baixo"
    elif score < 0.8:
        return "Moderado"
    else:
        return "Alto"

def enviar_resposta_callback():
    resposta = st.session_state.input_resposta.strip()
    if not resposta:
        st.warning("Por favor, responda antes de enviar.")
        return
    p = perguntas[st.session_state.indice_pergunta]

    with st.spinner("Analisando emoções..."):
        emocoes = analisar_emocoes(resposta)[0]

    st.session_state.respostas.append({
        "pergunta": p['texto'],
        "resposta": resposta,
        "emocoes": emocoes,
    })
    st.session_state.indice_pergunta += 1
    st.session_state.input_resposta = ""

# MOSTRAR TELA INICIAL ATÉ INICIAR QUESTIONÁRIO
if not st.session_state.started:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #6b3fa0 0%, #9f6bc0 100%);
        color: white;
        padding: 2rem 2rem;
        border-radius: 12px;
        margin-bottom: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <h2 style="text-align:center;">Bem-vindo ao Mind Tracker IA</h2>
        <p style="font-size:1.1rem; line-height:1.5;">
            Bem vindo ao assistente inteligente que ajuda você a entender seu estado emocional,
            analisando suas respostas a perguntas reflexivas sobre seu bem-estar.
        </p>
        <p style="font-size:1.1rem; line-height:1.5;">
            Nosso objetivo é detectar sinais precoces de ansiedade, depressão e burnout, oferecendo um feedback
            ético e respeitoso. Importante alertar que este sistema é apenas um indicativo e não substitui avaliação profissional.
        </p>
        <p style="font-size:1.1rem; line-height:1.5;">
            Para começar, clique no botão abaixo e responda as perguntas com sinceridade.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)


    # Centralizar o botão usando colunas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Iniciar Questionário"):
            st.session_state.started = True
            st.session_state.indice_pergunta = 0
            st.session_state.respostas = []
            st.session_state.input_resposta = ""

else:
    # Questionário
    if st.session_state.indice_pergunta < len(perguntas):
        pergunta_atual = perguntas[st.session_state.indice_pergunta]['texto']
        st.markdown(f'<div class="pergunta">🤖 {pergunta_atual}</div>', unsafe_allow_html=True)
        st.text_area("", key='input_resposta', value=st.session_state.input_resposta)
        st.button("Enviar resposta", on_click=enviar_resposta_callback)

    else:
        # Resultados
        emocoes_por_pergunta = []
        for resp in st.session_state.respostas:
            emocoes_resp = resp.get('emocoes', [])
            if isinstance(emocoes_resp, list) and all(isinstance(e, dict) and "label" in e and "score" in e for e in emocoes_resp):
                emocoes_por_pergunta.append(emocoes_resp)

        resultado = calcular_pontuacao_por_sintoma(emocoes_por_pergunta)
        risco = resultado["risco_por_sintoma"]
        top_emocoes = resultado["top_3_emocoes"]

        st.markdown("## Resultado final da triagem emocional")

        st.markdown("### Níveis de risco:")
        for sintoma, score in risco.items():
            st.markdown(f"- **{sintoma.capitalize()}**: {nivel_risco(score)} ({score:.2f})")

        st.markdown("### Top 3 emoções detectadas na triagem:")
        for emo, media in top_emocoes:
            st.markdown(f"- {emo.capitalize()}: {media:.2f}")

        st.markdown("### Respostas e emoções detectadas:")
        for idx, entry in enumerate(st.session_state.respostas):
            st.markdown(f"**Pergunta {idx+1}:** {entry['pergunta']}")
            st.markdown(f"**Resposta:** {entry['resposta']}")
            st.markdown("Emoções detectadas:")
            for emo in entry['emocoes']:
                score = emo.get('score', 0)
                try:
                    score_str = f"{float(score):.2f}"
                except (ValueError, TypeError):
                    score_str = "0.00"
                label = emo.get('label', 'unknown')
                st.write(f"- {label} ({score_str})")

            st.markdown("---")

        if st.button("Obrigado por participar"):
            st.session_state.started = False
            st.session_state.indice_pergunta = 0
            st.session_state.respostas = []
            st.session_state.input_resposta = ""
