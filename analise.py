import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.seasonal import seasonal_decompose

# Manipulando os dados
resultados = pd.read_csv('vendas_por_dia.csv')
resultados['dia'] = pd.to_datetime(resultados['dia'])
resultados['aumento'] = resultados['vendas'].diff()
resultados['aceleracao'] = resultados['aumento'].diff()
resultados['dia_da_semana'] = resultados['dia'].dt.day_name()
resultados.groupby('dia_da_semana').mean().round()

# Função para criação das tabelas
def plotando(y, title, ylabel, line):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    ax = sns.lineplot(x='dia', y=y, data=newsletter, ax=axes[line])
    ax.set_title(title, fontsize=14)
    ax.set_xlabel('DIA', fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax = ax

# plotando os gráficos
fig, axes = plt.subplots(3, figsize=(14,15))
plotando('vendas', 'Vendas no mês', 'VENDAS', 0)
plotando('aumento', 'Aumento no mês', 'AUMENTO', 1)
plotando('aceleracao', 'Aceleração no mês', 'ACELERAÇÃO', 2)

# Correlação
autocorrelation_plot(resultados['vendas'])
autocorrelation_plot(resultados['aumento'][1:])
autocorrelation_plot(resultados['aceleracao'][2:])

# Sazonalidade
t = seasonal_decompose(resultados['vendas'], period=2)
ax = t.plot()

# Média móvel
resultados['media_movel'] = resultados['vendas'].rolling(7).mean()
resultados.head(7)
