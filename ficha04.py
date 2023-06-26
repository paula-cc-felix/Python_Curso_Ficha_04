# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:56:23 2023

@author: paula
"""

# Objetivo
# Usar a biblioteca Pandas para analisar um conjunto de dados sobre o consumo de energia
# elétrica de vários países, e calcular a variação percentual no consumo de energia elétrica em
# Portugal entre 1990 e 2000

import pandas as pd  #importar a biblioteca Pandas

# Importar os Dados do Excel
dados =pd.read_excel('consumo_energia_electrica.xlsx', sheet_name='Data')

# Selecionar as colunas de interesse (País, Ano e Consumo de Energia)
dados = dados[['Country Name', '1990 [YR1990]', '2000 [YR2000]']]

# # Renomear as colunas a tratar
dados=dados.rename(columns={'Country Name':'País'})
dados=dados.rename(columns={'1990 [YR1990]':'consumo_1990'})
dados=dados.rename(columns={'2000 [YR2000]':'consumo_2000'})

# Filtrar os dados para o Portugal
dados_portugal = dados[dados['País'] == 'Portugal']
print("\n",dados_portugal)

# Calcular a variação percentual
def calcular_variacao_percentual(consumo_inicial, consumo_final):
    return (consumo_final - consumo_inicial) / consumo_inicial * 100
   
# Extrair os valores para o Portugal
consumo_1990 = dados_portugal['consumo_1990'].values[0]
consumo_2000 = dados_portugal['consumo_2000'].values[0]

# Calcular e imprimir a variação percentual
variacao_percentual = calcular_variacao_percentual(consumo_1990, consumo_2000)
print(f'\nVariação percentual no consumo de energia elétrica em Portugal, entre 1990 e 2000: {variacao_percentual:.2f}%')