import os
import json
import pandas as pd
import streamlit as st
from groq import Groq

# ── Configuração da página ─────────────────────────────────────────────────────
st.set_page_config(
    page_title="MentorIA — Agente de Carreira e Estudos",
    page_icon="🎓",
    layout="centered",
)

# ── Carregamento da base de conhecimento ──────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


@st.cache_data
def carregar_dados():
    with open(os.path.join(DATA_DIR, "perfil_profissional.json"), "r", encoding="utf-8") as f:
        perfil = json.load(f)

    with open(os.path.join(DATA_DIR, "trilhas_disponiveis.json"), "r", encoding="utf-8") as f:
        trilhas = json.load(f)

    historico_estudos = pd.read_csv(
        os.path.join(DATA_DIR, "historico_estudos.csv"), encoding="utf-8"
    )

    historico_atendimento = pd.read_csv(
        os.path.join(DATA_DIR, "historico_atendimento.csv"), encoding="utf-8"
    )

    return perfil, trilhas, historico_estudos, historico_atendimento


perfil, trilhas, historico_estudos, historico_atendimento = carregar_dados()


# ── Montagem do System Prompt ─────────────────────────────────────────────────
def montar_system_prompt(perfil, trilhas, historico_estudos, historico_atendimento):
    return f"""
Você é o MentorIA, um agente especializado em orientação de carreira e desenvolvimento profissional para estudantes e iniciantes na área de tecnologia.

Você tem acesso ao perfil completo do usuário, ao histórico de estudos, ao catálogo de trilhas disponíveis e ao histórico de sessões anteriores. Baseie TODAS as suas respostas nesses dados — nunca invente trilhas, certificações, plataformas ou faixas salariais que não estejam na base de conhecimento fornecida.

## Comportamento esperado
- Seja direto e específico. Evite respostas genéricas.
- Use o perfil e histórico do usuário para personalizar cada resposta.
- Quando recomendar uma trilha, sempre mencione: etapas prioritárias, tempo estimado e se os pré-requisitos do usuário estão atendidos.
- Ao identificar cursos em andamento ou não concluídos, mencione-os proativamente quando relevante.
- Estimativas de prazo devem ser conservadoras.
- Se a pergunta estiver fora do escopo de carreira e estudos em tecnologia, redirecione educadamente.

## O que você NUNCA deve fazer
- Inventar vagas específicas ou garantir que o usuário "vai conseguir" sem embasamento
- Garantir salários exatos — sempre use faixas e mencione que são estimativas de mercado
- Recomendar certificações ou cursos fora do catálogo disponível
- Ignorar o histórico quando ele for relevante para a resposta

---

## Perfil do Usuário
{json.dumps(perfil, ensure_ascii=False, indent=2)}

---

## Histórico de Estudos
{historico_estudos.to_string(index=False)}

---

## Trilhas Disponíveis
{json.dumps(trilhas, ensure_ascii=False, indent=2)}

---

## Histórico de Sessões Anteriores
{historico_atendimento.to_string(index=False)}
""".strip()


SYSTEM_PROMPT = montar_system_prompt(perfil, trilhas, historico_estudos, historico_atendimento)

# ── Interface ─────────────────────────────────────────────────────────────────
st.title("🎓 MentorIA")
st.caption("Seu agente pessoal de carreira e estudos em tecnologia.")

nome = perfil["perfil"]["nome"].split()[0]
st.markdown(
    f"Olá, **{nome}**! Estou aqui para te ajudar com trilhas de estudo, "
    "orientação de carreira e planejamento. O que você quer resolver hoje?"
)

st.divider()

# ── Estado da sessão ──────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Input do usuário ──────────────────────────────────────────────────────────
if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Chamada à API Claude
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                max_tokens=1024,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                ],
            )

            resposta = response.choices[0].message.content
            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})

# ── Sidebar com info do usuário ───────────────────────────────────────────────
with st.sidebar:
    st.header("📋 Seu Perfil")
    p = perfil["perfil"]
    st.markdown(f"**Nome:** {p['nome']}")
    st.markdown(f"**Formação:** {p['formacao_atual']}")
    st.markdown(f"**Objetivo:** {p['objetivo_curto_prazo']}")

    st.divider()
    st.subheader("📚 Cursos em Andamento")
    em_andamento = historico_estudos[historico_estudos["status"] == "Em andamento"]
    for _, row in em_andamento.iterrows():
        st.markdown(f"- {row['curso']} ({row['plataforma']})")

    st.divider()
    st.subheader("🏆 Áreas de Interesse")
    for area in perfil["areas_de_interesse"]:
        st.markdown(f"- {area}")

    st.divider()
    if st.button("🗑️ Limpar conversa"):
        st.session_state.messages = []
        st.rerun()
