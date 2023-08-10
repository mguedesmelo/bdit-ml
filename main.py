import pandas as pd

# lendo toda a tabela de seccionadores
seccionadores = pd.read_csv('dados/seccionador.csv', sep=",", encoding='ISO-8859-1')

print("Quantidade de seccionadores: %.2f" % len(seccionadores))

# eliminando colunas que nao serao trabalhadas
# axis = 0 --> remove linhas
# axis = 1 --> remove colunas
data = seccionadores.drop(["Transmissora_SIGET", "Concessao_SIGET"], axis=1)

# eliminando outliers - colunas que nao serao trabalhadas


# eliminando missings - linhas em branco das colunas a serem classificaads
#data = data.dropna()


print(seccionadores.describe())
print(data.describe())
print(data.head())

