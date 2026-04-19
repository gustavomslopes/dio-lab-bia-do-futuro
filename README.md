# 🎓 Agente de Carreira e Estudos com IA Generativa

## Contexto

O mercado de trabalho evolui cada vez mais rápido, e profissionais precisam de orientação **personalizada e contínua** para tomar boas decisões sobre sua carreira e desenvolvimento. Neste projeto, foi idealizado e prototipado um agente inteligente que utiliza IA Generativa para:

- **Antecipar lacunas de habilidade** antes que se tornem um obstáculo na carreira
- **Personalizar planos de estudo** com base no perfil e objetivos de cada usuário
- **Sugerir trilhas de aprendizado** alinhadas ao mercado atual
- **Garantir respostas confiáveis** sobre certificações, tecnologias e oportunidades (anti-alucinação)

> 💡 Na pasta [`examples/`](./examples) você encontra referências de implementação para cada etapa deste projeto.

---

## O Que Foi Entregue

### 1. Documentação do Agente

Definição do **o que** o agente faz e **como** ele funciona:

- **Caso de Uso:** Consultoria de carreira e recomendação de trilhas de estudo para desenvolvedores
- **Persona e Tom de Voz:** Mentor experiente, direto e encorajador
- **Arquitetura:** Fluxo de dados com base de conhecimento e LLM
- **Segurança:** Estratégias para evitar alucinações em recomendações de carreira

📄 [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Dados mockados disponíveis na pasta [`data/`](./data):

| Arquivo | Formato | Descrição |
|---|---|---|
| `historico_estudos.csv` | CSV | Histórico de cursos e certificações do usuário |
| `historico_atendimento.csv` | CSV | Histórico de sessões com o agente |
| `perfil_profissional.json` | JSON | Perfil, habilidades e objetivos do usuário |
| `trilhas_disponiveis.json` | JSON | Trilhas de aprendizado e certificações disponíveis |

📄 [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documentação dos prompts que definem o comportamento do agente:

- **System Prompt:** Instruções de comportamento, tom de voz e restrições
- **Exemplos de Interação:** Cenários reais com entrada e saída esperada
- **Edge Cases:** Como o agente lida com perguntas fora do escopo

📄 [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Protótipo funcional do agente com:

- Interface de chat via **Streamlit**
- Integração com **API Claude (Anthropic)**
- Leitura da base de conhecimento local (JSON + CSV)

📁 [`src/app.py`](./src/app.py)

---

### 5. Avaliação e Métricas

Métricas utilizadas para avaliar a qualidade do agente:

- Relevância das recomendações ao perfil do usuário
- Taxa de respostas sem alucinações
- Alinhamento das sugestões com o mercado real

📄 [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Roteiro do pitch de 3 minutos apresentando o agente.

📄 [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Utilizadas

| Categoria | Ferramentas |
|---|---|
| **LLM** | [Claude (Anthropic)](https://claude.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), Python |
| **Orquestração** | Nativo com API REST |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 dio-lab-agente-carreira/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_estudos.csv         # Histórico de cursos e certificações (CSV)
│   ├── historico_atendimento.csv     # Histórico de sessões com o agente (CSV)
│   ├── perfil_profissional.json      # Perfil e objetivos do usuário (JSON)
│   └── trilhas_disponiveis.json      # Trilhas e certificações disponíveis (JSON)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # Chatbot Streamlit + Claude API
│
├── 📁 assets/                        # Imagens e diagramas
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Como Rodar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/gustavomslopes/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# 2. Instale as dependências
pip install streamlit anthropic pandas

# 3. Configure sua chave de API
export ANTHROPIC_API_KEY="sua-chave-aqui"

# 4. Rode a aplicação
streamlit run src/app.py
```

---

## Dicas

1. **Comece pelo system prompt:** A persona do mentor define tudo
2. **Use os dados mockados:** Eles simulam um usuário real com histórico consistente
3. **Foque na personalização:** O diferencial é recomendar com base no perfil, não genericamente
4. **Teste perguntas reais:** "Devo aprender Rust ou Go?", "Quanto tempo pra conseguir emprego em dados?"
5. **Anti-alucinação:** Nunca invente vagas, salários ou prazos — só recomende o que está na base

---

*Projeto desenvolvido como parte do lab **"BIA do Futuro"** da [DIO](https://www.dio.me/), adaptado para o domínio de Carreira e Estudos.*
