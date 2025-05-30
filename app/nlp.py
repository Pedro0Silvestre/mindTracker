from transformers import pipeline
from utils.translate import translate

# Cria uma pipeline de classificação de texto usando o modelo passado e retorna as 3 principais chaves do dicionario
classifier = pipeline("text-classification",model="j-hartmann/emotion-english-distilroberta-base",top_k = 3)


#detecta as seguintes emocoes num texto: 'anger', 'disgust','fear', 'joy', 'neutral', 'sadness', 'surprise'
def analisar_emocoes(texto_pt):
    
    texto_eng = translate(texto_pt) #traduz o texto para ingles
    
    #valida se o texto recebido foi de fato uma string ou se teve algum erro no retorno
    if not isinstance(texto_eng, str) or texto_eng.strip() == "":
        print("[ERRO] Texto traduzido inválido:", texto_eng)
        return []
    
    #caso o texto tenha sido traduzido corretamente armazena as emocoes detectadas e retorna os 3 maiores indices
    try:
        resultado = classifier(texto_eng)
        return resultado
    
    except Exception as e:
        print(f"ERRO NA ANALISE: {e}")
        return []