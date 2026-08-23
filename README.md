# 🤖 CorpAI — Assistente Corporativo com RAG

O **CorpAI** é um assistente corporativo baseado em Inteligência Artificial, desenvolvido como projeto do challenge **Alura Agentes**.

A aplicação permite que colaboradores façam perguntas em linguagem natural e recebam respostas baseadas em documentos internos da empresa, utilizando uma arquitetura de **RAG (Retrieval-Augmented Generation)**.

---

## 🎯 Objetivo

O objetivo do projeto é criar uma base de conhecimento conversacional capaz de:

* consultar documentos corporativos;
* localizar informações semanticamente relevantes;
* gerar respostas com Inteligência Artificial;
* indicar as fontes utilizadas;
* evitar respostas inventadas quando a informação não estiver disponível.

---

## 🧠 Como funciona

O fluxo simplificado da aplicação é:

```text
Documentos corporativos
        ↓
Extração de conteúdo
        ↓
Divisão em trechos
        ↓
Geração de embeddings
        ↓
Busca por similaridade semântica
        ↓
Recuperação dos trechos relevantes
        ↓
Gemini
        ↓
Resposta + fontes
```

Quando o colaborador envia uma pergunta, o sistema transforma essa pergunta em uma representação vetorial e compara com os documentos disponíveis.

Os trechos mais relacionados são enviados como contexto para o modelo de linguagem, que gera uma resposta utilizando somente as informações recuperadas.

---

## 📚 Documentos utilizados

Para demonstrar o funcionamento do agente, foram utilizados documentos fictícios de uma empresa chamada **CorpTech**.

A base contém informações relacionadas a:

* política de férias;
* benefícios;
* política de despesas;
* contatos das áreas internas.

Os documentos utilizados no MVP estão nos formatos:

* Markdown;
* CSV;
* JSON.

A arquitetura pode ser expandida para outros formatos, como PDF, Word, Excel, PowerPoint e HTML.

---

## 🛠 Tecnologias

* Python
* Streamlit
* Sentence Transformers
* Scikit-learn
* Pandas
* Google Gemini API
* Git
* GitHub
* Streamlit Community Cloud

---

## 🔎 Busca semântica

O projeto utiliza o modelo:

```text
all-MiniLM-L6-v2
```

da biblioteca `sentence-transformers`.

Os documentos são convertidos em embeddings e comparados com o embedding da pergunta utilizando **similaridade de cosseno**.

Os trechos mais relevantes são recuperados e enviados para o modelo de linguagem como contexto.

---

## 🤖 Geração de respostas

A geração das respostas é realizada utilizando a API do **Google Gemini**.

O prompt instrui o modelo a:

* utilizar somente os documentos recuperados;
* não utilizar conhecimento externo;
* não inventar informações;
* informar quando a resposta não estiver disponível;
* indicar os documentos utilizados como fonte.

---

## 🛡 Controle de alucinação

Quando não existe informação suficiente nos documentos disponíveis, o agente deve responder:

> Não encontrei essa informação nos documentos disponíveis.

Esse comportamento reduz o risco de geração de respostas sem respaldo na base corporativa.

---

## 💬 Interface

A aplicação possui uma interface web simples criada com **Streamlit**.

O usuário pode:

* digitar uma pergunta;
* receber uma resposta gerada por IA;
* visualizar as fontes utilizadas;
* consultar os trechos recuperados pelo mecanismo de busca.

---

## ☁️ Deploy

A aplicação foi publicada utilizando o **Streamlit Community Cloud**.

O deploy permite que o agente seja acessado através de uma URL pública, sem necessidade de execução local.

### Aplicação online

Adicione aqui o link da aplicação:

```text
https://corp-ai-alura-jx5dzr9m3pboncsezezcwl.streamlit.app/
```

---

## 📸 Demonstração

Adicione abaixo uma captura de tela da aplicação executando em nuvem.

```markdown
![Demonstração do CorpAI](images/demo.png)
```

---

## 🚀 Executando localmente

Clone o repositório:

```bash
git clone https://github.com/rogondev/corp-ai-alura
```

Entre na pasta:

```bash
cd corp-ai-alura
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo:

```text
.streamlit/secrets.toml
```

E adicione sua chave da API:

```toml
GEMINI_API_KEY = "SUA_CHAVE"
```

Execute:

```bash
streamlit run app.py
```

A aplicação ficará disponível normalmente em:

```text
http://localhost:8501
```

---

## 📁 Estrutura do projeto

```text
corp-ai-alura/
│
├── documents/
│   ├── politica_ferias.md
│   ├── beneficios.md
│   ├── despesas.csv
│   └── contatos.json
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧪 Exemplos de perguntas

Algumas perguntas utilizadas para validar o agente:

```text
Quantos dias de férias os colaboradores têm direito?

Qual é o valor do vale-refeição oferecido pela empresa?

A empresa oferece auxílio academia?
```

As duas primeiras perguntas possuem respostas na base documental.

A terceira foi utilizada para testar o comportamento do agente quando a informação solicitada não está disponível.

---

## ⚠️ Limitações do MVP

Este projeto foi desenvolvido como uma prova de conceito.

A versão atual possui algumas simplificações:

* base documental pequena;
* documentos fictícios;
* chunking simples por tamanho;
* busca vetorial realizada em memória;
* ausência de reranking;
* ausência de autenticação;
* atualização manual dos documentos;
* suporte limitado a alguns formatos.

---

## 🔮 Melhorias futuras

Uma evolução do projeto poderia incluir:

* suporte completo a PDF, Word, Excel, PowerPoint e HTML;
* armazenamento dos documentos em Object Storage;
* banco vetorial persistente;
* reranking dos resultados;
* pipeline automático de ingestão;
* filtros por metadados;
* histórico de conversas;
* autenticação corporativa;
* feedback positivo e negativo das respostas;
* monitoramento e observabilidade;
* atualização automática dos documentos;
* integração com Slack ou Microsoft Teams.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte do challenge **Alura Agentes**, com o objetivo de explorar a aplicação prática de Inteligência Artificial generativa, embeddings, busca semântica e RAG em um cenário corporativo.
