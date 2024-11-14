Projeto de Extração e Análise de Dados do SteamDB
Resumo
Este projeto tem como objetivo a extração, estruturação e análise de dados de promoções de jogos no SteamDB, visando criar uma base de dados organizada para análise futura. Utilizamos Python, Selenium para scraping, Pandas para limpeza e estruturação dos dados, e Google BigQuery para armazenar e consultar os dados, além de integração com Google Sheets para visualização.

Etapas do Projeto
Extração de Dados:

Usamos Selenium para acessar a página de promoções do SteamDB e extrair informações brutas de jogos, incluindo título, preço, desconto, avaliação, data de lançamento e status especial.
Os dados brutos foram inicialmente salvos em formato JSON para facilitar o armazenamento e garantir a captura completa das informações.
Estruturação e Limpeza dos Dados:

Com a biblioteca Pandas, organizamos os dados em um formato tabular, separando campos como "Título", "Desconto", "Preço Atual", "Rating", "Data de Lançamento" e outras informações adicionais.
Realizamos a padronização de formatos (ex.: remoção de símbolos de moeda e porcentagem, conversão de preços e avaliações para float) e removemos redundâncias para garantir que os dados estivessem prontos para análise.
Armazenamento e Visualização:

Os dados estruturados foram carregados no Google BigQuery para facilitar consultas avançadas e análises, com uma conexão direta ao Google Sheets para visualização dinâmica.
Também foi feita uma integração com o Excel para permitir análises e visualizações adicionais.
Análises e Visualizações:

Com os dados no BigQuery e no Google Sheets, realizamos análises para identificar tendências de desconto, avaliar jogos com melhor custo-benefício, e explorar correlações entre preço e avaliação.
Visualizações foram criadas para destacar insights, como jogos com os maiores descontos, jogos mais bem avaliados e a distribuição de lançamentos ao longo do tempo.
Como Rodar o Projeto
Clone este repositório:

bash
Copiar código
git clone https://github.com/seuusuario/seurepositorio.git
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configure o arquivo de variáveis de ambiente (.env) para incluir suas credenciais e configurações do Google BigQuery e Google Sheets.

Execute o script de extração de dados:

bash
Copiar código
python scripts/extrair_dados.py
Execute o script de estruturação de dados:

bash
Copiar código
python scripts/estruturar_dados.py
Carregue o arquivo CSV final no BigQuery para consultas e visualize no Google Sheets ou Excel.

Estrutura do Repositório
scripts/: Contém os scripts para extração e estruturação de dados.
dados/brutos/: Armazena os dados extraídos do SteamDB em formato bruto (JSON).
dados/refinados/: Contém os dados estruturados e prontos para análise em formato CSV.
README.md: Documentação do projeto (este arquivo).
.gitignore: Arquivos e pastas ignorados pelo Git para evitar vazamento de informações sensíveis.
requirements.txt: Lista de pacotes e dependências necessários para o projeto.
Tecnologias Utilizadas
Python: Principal linguagem de programação para extração e processamento de dados.
Selenium: Biblioteca para web scraping.
Pandas: Biblioteca para manipulação e análise de dados.
Google BigQuery: Plataforma para armazenamento e consulta de grandes volumes de dados.
Google Sheets e Excel: Ferramentas para visualização e análise de dados.
Considerações sobre Segurança e Privacidade
Todos os dados sensíveis, como credenciais e informações de configuração pessoal, foram removidos do repositório para garantir a privacidade. Recomenda-se que o arquivo .env ou qualquer outro arquivo de configuração com credenciais seja mantido fora do repositório.

Próximos Passos
Melhorar a automação do processo de análise e visualização.
Adicionar mais análises e visualizações interativas.
Explorar integrações com outras plataformas de dados.