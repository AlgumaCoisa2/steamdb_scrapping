import pandas as pd
import re

# Caminho do arquivo de entrada e de saída
arquivo_entrada = r"C:\Francisco\Encontrar Emprego\Desafio Tecnico\beanalytics\dados\brutos\dados_brutos_100.json"
arquivo_saida = r"C:\Francisco\Encontrar Emprego\Desafio Tecnico\beanalytics\dados\refinados\dados_estruturados_final.csv"

# Carregar o arquivo estruturado
data = pd.read_json(arquivo_entrada)

# Função para extrair campos específicos
def extrair_campos(linha):
    # Extrações de exemplo; ajuste as expressões conforme necessário
    titulo = linha.split('\n')[0] if linha else ""
    desconto = re.search(r"-\d+%", linha)
    preco = re.search(r"R\$\s*\d+,\d+", linha)
    rating = re.search(r"\d+\.\d+%", linha)
    data_lancamento = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b \d{4}", linha)
    informacao_extra = re.findall(r"(Top Seller|Introductory Offer|new historical low)", linha)
    
    # Retornar como um dicionário
    return {
        "Título": titulo,
        "Desconto": desconto.group(0) if desconto else "",
        "Preço Atual": preco.group(0) if preco else "",
        "Rating": rating.group(0) if rating else "",
        "Data de Lançamento": data_lancamento.group(0) if data_lancamento else "",
        "Informação Extra": " | ".join(informacao_extra) if informacao_extra else ""
    }

# Aplicar a função de extração em cada linha de dados brutos
dados_estruturados = data['Dados Brutos'].apply(extrair_campos).apply(pd.Series)

# Limpar e padronizar formatos
dados_estruturados['Preço Atual'] = (
    dados_estruturados['Preço Atual']
    .str.replace(r'R\$', '', regex=True)  # Remover "R$" com regex
    .str.replace(',', '.')  # Trocar vírgula por ponto
    .astype(float)  # Converter para float
)

dados_estruturados['Desconto'] = (
    dados_estruturados['Desconto']
    .str.replace('%', '')  # Remover "%"
    .astype(float)  # Converter para float
)

dados_estruturados['Rating'] = (
    dados_estruturados['Rating']
    .str.replace('%', '')  # Remover "%"
    .astype(float)  # Converter para float
)

# Combinar com o DataFrame original e remover colunas redundantes
data = pd.concat([data, dados_estruturados], axis=1).drop(columns=['Dados Brutos'])

# Salvar o DataFrame estruturado e limpo
data.to_csv(arquivo_saida, index=False)
print("Dados estruturados e salvos com sucesso.")
