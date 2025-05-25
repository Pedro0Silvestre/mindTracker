from deep_translator import GoogleTranslator

#funcao para tradução do texto de ptbr para eng
def translate(texto_pt):
    try:
        return GoogleTranslator(source='pt', target='en').translate(texto_pt)#chama classe googletranslator com a fonte em pt e alvo de traducao eng
    
    except Exception as e: # caso haja um erro de traducao exibe o erro e retorna o texto original
        print(f"Erro na tradução {e}")
        return texto_pt #retonar texto original