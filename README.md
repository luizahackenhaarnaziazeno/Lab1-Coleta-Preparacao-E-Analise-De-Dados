<div align="center">

## Laboratório 1: Web Scraping - Coleta, Preparação e Análise de Dados 🕷️

Este repositório contém a resolução do **Laboratório 1** da disciplina de Coleta, Preparação e Análise de Dados da PUCRS, ministrada pela Professora Katherine Bianchini Esper. O projeto foca na aplicação de técnicas de *web scraping* para a extração de dados em dois cenários distintos.

## 🎯 Objetivos do Projeto

O projeto é dividido em duas tarefas principais:

1. **Ambiente Controlado (Wikipédia):** Criação de um *crawler* para explorar links e conexões entre artigos, partindo da página inicial sobre *Ada Lovelace*.
2. **Ambiente Real (IMDb):** Extração de dados estruturados dos 250 filmes com a maior avaliação no site IMDb (Top 250), lidando com paginação e elementos dinâmicos.
---

## 📂 Estrutura de Arquivos

* 📓 `Laboratorio1coleta.ipynb`: Notebook Jupyter contendo a resolução da **Tarefa 1** (Wikipédia). Utiliza `requests` e `BeautifulSoup` para navegar no HTML estático e gerar os arquivos CSV com os dados coletados.
* 📓 `Laboratorio1_Tarefa2_IMDb.ipynb`: Notebook Jupyter responsável pela **Tarefa 2** (IMDb). Utiliza `Selenium` para navegar nas páginas de forma dinâmica, extraindo detalhes dos filmes de forma a não sobrecarregar os servidores.
* 🗄️ `imdb_top250.json`: Arquivo gerado pela Tarefa 2 contendo todos os dados extraídos dos 250 filmes, incluindo os bytes das imagens dos pôsteres convertidos para o formato `Base64`.
* 🗄️ `imdb_top250_sem_imagens.json`: Versão mais leve do arquivo de resultados, contendo apenas os dados textuais (título, ano, nota, gêneros, direção, url), omitindo os dados em base64 das imagens.

---

## 🛠️ Tecnologias e Dependências

Para executar os notebooks deste projeto, você precisará do Python 3 instalado e das seguintes bibliotecas:

* `requests`
* `beautifulsoup4`
* `selenium`

Você pode instalar as dependências rodando o comando abaixo:
```bash
pip install requests beautifulsoup4 selenium
```

# 👥 Autoras:

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/142232479?v=4" width=115><br><sub>Luiza Hackenhaar Naziazeno</sub>](https://github.com/luizahackenhaarnaziazeno) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/142234602?v=4" width=115><br><sub>Gabrielle Guarani Da Silva</sub>](https://github.com/gguarani) |
| :---: | :---: |
