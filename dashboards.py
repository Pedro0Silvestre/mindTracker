import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


emotions = pd.read_json("C:\Projetos_py\mindTracker\json.json")
emotions_normalizado = pd.json_normalize(emotions['emotions'])
df = emotions_normalizado

peso_alto = 0.5
peso_medio = 0.2
peso_baixo = 0.1

df['depressao'] = peso_alto * df['sadness'] + peso_medio * df['disgust'] + peso_baixo * df['anger'] + peso_medio * (1 - df['joy'])
df['ansiedade'] = peso_alto * df['fear'] + 0.15 * df['anger'] + 0.15 * df['surprise'] + peso_baixo * df['sadness'] + peso_baixo * (1 - df['joy'])
df['estresse'] = peso_medio * df['anger'] + peso_medio * df['disgust'] + peso_medio * df['sadness'] + peso_medio * df['fear'] + peso_medio * (1 - df['joy'])
df
def grafico_depressao():
    fig, ax = plt.subplots(figsize=(10,6))  # cria figura e eixo

    sns.lineplot(x='data', y='depressao', hue='curso', data=df, marker='o', linewidth=2.5, ax=ax)

    # você pode personalizar o gráfico aqui se quiser
    ax.set_title('Risco de depressão por Curso ao Longo do Tempo')
    ax.set_xlabel('Data')
    ax.set_ylabel('Risco de Depressão')
    ax.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', borderaxespad=0)
    ax.legend(title='Curso')

    return fig
def grafico_ansiedade():
    fig, ax = plt.subplots(figsize=(10,6)) 
    
    sns.lineplot(x='data', y='ansiedade', hue='curso', data=df, marker='o', linewidth=2.5, ax=ax)
    ax.set_title('Risco de Ansiedade por Curso ao Longo do Tempo')
    ax.set_xlabel('Data')
    ax.set_ylabel('Ansiedade')
    ax.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', borderaxespad=0)
    ax.legend(title='Curso')
    
    return fig
def grafico_estresse():
    fig, ax = plt.subplots(figsize=(10,6)) 
    
    sns.lineplot(x='data', y='estresse', hue='curso', data=df, marker='o', linewidth=2.5, ax=ax)
    ax.set_title('Risco de Estresse por Curso ao Longo do Tempo')
    ax.set_xlabel('Data')
    ax.set_ylabel('Estresse')
    ax.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', borderaxespad=0)
    ax.legend(title='Curso')
    
    return fig