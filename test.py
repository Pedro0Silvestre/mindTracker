from app.nlp import analisar_emocoes

texto_pt = "Estou me sentindo muito feliz com as aulas nesse semestre."

emocoes = analisar_emocoes(texto_pt)[0]

#emocoes detectaveis: print(classifier.model.config.id2label)

print("emocoes detectadas:")

for emocao in emocoes:
    print(f"- {emocao['label']} ({emocao['score']:.2f})")
        
                
#emocoes detectadas: {0: 'anger', 1: 'disgust', 2: 'fear', 3: 'joy', 4: 'neutral', 5: 'sadness', 6: 'surprise'}
    