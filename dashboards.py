import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.cm as cm
import numpy as np
import matplotlib.animation as animation
import plotly.express as px
from datetime import datetime

emotions = pd.read_json("/content/db.json")
emotions_normalizado = pd.json_normalize(emotions['emotions'])
df = emotions_normalizado

peso_alto = 0.5
peso_medio = 0.2
peso_baixo = 0.1

df['depressao'] = peso_alto * df['sadness'] + peso_medio * df['disgust'] + peso_baixo * df['anger'] + peso_medio * (1 - df['joy'])
df['ansiedade'] = peso_alto * df['fear'] + 0.15 * df['anger'] + 0.15 * df['surprise'] + peso_baixo * df['sadness'] + peso_baixo * (1 - df['joy'])
df['estresse'] = peso_medio * df['anger'] + peso_medio * df['disgust'] + peso_medio * df['sadness'] + peso_medio * df['fear'] + peso_medio * (1 - df['joy'])
df

sns.lineplot(x=df['data'], y=df['depressao'], hue=df['curso'], data=df, marker='o', linewidth=2.5)
plt.show()

sns.lineplot(x=df['data'], y=df['ansiedade'], hue=df['curso'], data=df, marker='o', linewidth=2.5)
plt.show()

sns.lineplot(x=df['data'], y=df['estresse'], hue=df['curso'], data=df, marker='o', linewidth=2.5)
plt.show()