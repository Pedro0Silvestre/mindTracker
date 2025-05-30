peso_emocoes_por_sintoma = {
    "anxiety" : {
        "fear" : 1.0,
        "sadness" : 0.5,
        "anger": 0.3,
        "disgust": 0.2,
        "surprise": 0.1,
        "neutral": 0.0,
        "joy": -0.5
    },
    "depression": {
        "sadness": 1.0,
        "disgust": 0.5,
        "anger": 0.4,
        "fear": 0.3,
        "neutral": 0.0,
        "surprise": 0.0,
        "joy": -0.7
    },
    "burnout": {
        "anger": 1.0,
        "disgust": 1.0,
        "fear": 0.7,
        "sadness": 0.5,
        "neutral": 0.0,
        "surprise": 0.0,
        "joy": -0.4
    }
}

def calcular_pontuacao_por_sintoma(emocoes_perguntas):
    """
    Recebe lista de listas: emoções detectadas para cada pergunta.
    Calcula a média final de score para cada emoção somando todas perguntas.
    Depois calcula o risco por sintoma com base nessas médias finais.
    """

    soma_scores = {}
    count_scores = {}

    # Agrega todas emoções de todas perguntas para calcular médias finais
    for emocoes in emocoes_perguntas:
        for emo in emocoes:
            label = emo["label"]
            score = emo["score"]
            soma_scores[label] = soma_scores.get(label, 0) + score
            count_scores[label] = count_scores.get(label, 0) + 1

    # Calcula a média final para cada emoção
    medias_finais = {}
    for label in soma_scores:
        medias_finais[label] = soma_scores[label] / count_scores[label]

    # Calcula risco para cada sintoma usando médias finais * pesos
    risco_por_sintoma = {}
    for sintoma, pesos in peso_emocoes_por_sintoma.items():
        risco = 0
        for emo_label, media_score in medias_finais.items():
            peso = pesos.get(emo_label, 0)
            risco += media_score * peso
        risco_por_sintoma[sintoma] = max(risco, 0)  # evita negativo

    # Ordena emoções por média final para top 3
    top_3_emocoes = sorted(medias_finais.items(), key=lambda x: x[1], reverse=True)[:3]

    return {
        "risco_por_sintoma": risco_por_sintoma,
        "top_3_emocoes": top_3_emocoes
    } 

# --- Exemplo com 5 perguntas simuladas ---

emocoes_perguntas = [
    [
        {"label": "fear", "score": 0.6},
        {"label": "sadness", "score": 0.4},
        {"label": "anger", "score": 0.3},
        {"label": "joy", "score": 0.1},
        {"label": "neutral", "score": 0.2}
    ],
    [
        {"label": "sadness", "score": 0.7},
        {"label": "disgust", "score": 0.2},
        {"label": "joy", "score": 0.0},
        {"label": "neutral", "score": 0.1},
        {"label": "surprise", "score": 0.1}
    ],
    [
        {"label": "anger", "score": 0.8},
        {"label": "disgust", "score": 0.5},
        {"label": "fear", "score": 0.2},
        {"label": "joy", "score": 0.1}
    ],
    [
        {"label": "joy", "score": 0.9},
        {"label": "neutral", "score": 0.5},
        {"label": "surprise", "score": 0.4}
    ],
    [
        {"label": "fear", "score": 0.3},
        {"label": "sadness", "score": 0.5},
        {"label": "anger", "score": 0.1},
        {"label": "disgust", "score": 0.2}
    ]
]

resultado_final = calcular_pontuacao_por_sintoma(emocoes_perguntas)

print("Risco por sintoma (média final das emoções):")
for sintoma, valor in resultado_final["risco_por_sintoma"].items():
    print(f"  {sintoma}: {valor:.2f}")

print("\nTop 3 emoções médias finais:")
for emo, media in resultado_final["top_3_emocoes"]:
    print(f"  {emo}: {media:.2f}")
