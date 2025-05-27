from app.nlp import analisar_emocoes

valores = [
    ["anger", 0],
    ["disgust", 0],
    ["fear", 0],
    ["joy", 0],
    ["neutral", 0],
    ["sadness", 0],
    ["surprise", 0]
]
numeroDeRespostas = 0

while True:
    texto_pt = input("Insira sua resposta:")
    if (texto_pt == ""):
        break

    emocoes = analisar_emocoes(texto_pt)[0]

    #emocoes detectaveis: print(classifier.model.config.id2label)

    print("emocoes detectadas:")

    for emocao in emocoes:
        print(f"- {emocao['label']} ({100 * emocao['score']:.2f}%)")
        for valor in valores:
            if valor[0] == emocao['label']:
                valor[1] += emocao['score']



    numeroDeRespostas += 1

    #emocoes detectadas: {0: 'anger', 1: 'disgust', 2: 'fear', 3: 'joy', 4: 'neutral', 5: 'sadness', 6: 'surprise'}

print(f"\nValor total por emoção: ")
for valor in valores:
    print(f"{valor[0]}: {valor[1]:.2f}")

print(f"\nMédia de emoções nas respostas")
for valor in valores:
    print(f"{valor[0]}: {(valor[1]/numeroDeRespostas)*100:.2f}%")

#Nota a quem for mecher, e possívelmente para avisos posteriores
#O sentimento de estar sobrecarregado é comumente descrito pelo sistema através do alto valor de "surprise"
#nota-se também que "ansioso" é traduzido para excited, podendo causar uma perca de sentido na frase.
#trocar por apreensivo ou outro sinônimo costuma ser mais eficaz


"""
Código original do Pedro

texto_pt = "Estou me sentindo aflito sobre o resultado das provas."

emocoes = analisar_emocoes(texto_pt)[0]

#emocoes detectaveis: print(classifier.model.config.id2label)

print("emocoes detectadas:")

for emocao in emocoes:
    print(f"- {emocao['label']} ({emocao['score']:.2f})")

#emocoes detectadas: {0: 'anger', 1: 'disgust', 2: 'fear', 3: 'joy', 4: 'neutral', 5: 'sadness', 6: 'surprise'}

"""