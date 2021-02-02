import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

#Função para plotar gráficos
def plotando(y, title, y_title, line, colune):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    ax = sns.lineplot(x='mes', y=y, data=alucar, ax=axes[line][colune])
    ax.set_title(title, fontsize=10)
    ax.set_xlabel('MÊS', fontsize=10)
    ax.set_ylabel(y_title, fontsize=10)
    ax.figure.set_size_inches(12, 12)

# Tratando os dados
alucar = pd.read_csv('data_sets/alucar.csv')
alucar['mes'] = pd.to_datetime(alucar['mes'])
alucar['crescimento'] = alucar['vendas'].diff()
alucar['aceleracao'] = alucar['crescimento'].diff()

fig, axes = plt.subplots(2, 2, figsize=(20, 20))
#Plotando o gráfico de vendas no mês
plotando('vendas', 'VENDAS NO MÊS', 'VENDAS', 0, 0)

#Plotando o gráfico de aumento das vendas no mês
plotando('crescimento', 'CRESCIMENTO DAS VENDAS NO MÊS', 'CRESCIMENTO', 0, 1)

#Plotando o gráfico da aceleração das vendas no mês
plotando('aceleracao', 'ACELERAÇÃO DAS VENDAS NO MÊS', 'ACELERAÇÃO', 1, 0)

# CORRELAÇÃO
autocorrelation_plot(alucar['vendas'])
plt.show()




