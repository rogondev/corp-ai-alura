import streamlit as st
from google import genai
from rag import search_documents

st.set_page_config(
    page_title="CorpAI",
    page_icon="🤖",
    layout="centered"
)

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("🤖 CorpAI")
st.subheader("Assististente Corporativo com IA")

st.write(
    "Faça perguntas sobre os documentos internos da empresa."
)

question = st.text_input(
    "Digite sua pergunta:",
    placeholder="Ex: Quantos dias de férias os funcionários têm?"
)

if st.button("Perguntar"):

    if not question.strip():
        st.warning("Digite uma pergunta.")

    else:
        with st.spinner("Consultando documentos..."):

            results = search_documents(question)

            if not results or results[0]["score"] < 0.25:
                st.warning(
                    "Não encontrei essa informação nos documentos disponíveis."
                )

            else:
                context = "\n\n".join(
                    [
                        f"Fonte: {result['source']}\n"
                        f"Conteúdo: {result['text']}"
                        for result in results
                    ]
                )

                prompt = f"""
Você é um assistente corporativo chamado CorpAI.

Sua função é responder perguntas de colaboradores utilizando
SOMENTE as informações presentes nos documentos fornecidos.

Regras:
- Não invente informações.
- Não utilize conhecimento externo.
- Responda de forma clara e objetiva.
- Se a informação não estiver no contexto, diga:
  "Não encontrei essa informação nos documentos disponíveis."
- Ao final, informe quais documentos foram utilizados como fonte.

CONTEXTO DOS DOCUMENTOS:

{context}

PERGUNTA DO COLABORADOR:

{question}
"""

                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt
                    )

                    st.markdown("### Resposta")
                    st.write(response.text)

                    st.markdown("### Fontes recuperadas")

                    sources = []

                    for result in results:
                        if result["source"] not in sources:
                            sources.append(result["source"])

                    for source in sources:
                        st.write(f"📄 {source}")

                    with st.expander("Ver contexto utilizado pela IA"):
                        for result in results:
                            st.write(f"**Fonte:** {result['source']}")
                            st.write(result["text"])
                            st.divider()

                except Exception as error:
                    st.error(
                        "Ocorreu um erro ao gerar a resposta com IA."
                    )
                    st.exception(error)