# 02 — Base de Conhecimento

## Estratégia de Dados

A base de conhecimento do MentorIA é composta por 4 arquivos locais que simulam um usuário real com histórico consistente. Em produção, esses dados viriam de um banco de dados ou API conectada à plataforma do usuário.

---

## Arquivos e Estrutura

### `perfil_profissional.json`
Contém informações estáticas e preferências do usuário:
- Dados pessoais e formação atual
- Habilidades técnicas com nível de proficiência
- Áreas de interesse e de menor interesse
- Preferências de aprendizado (formato, horas disponíveis)
- Projetos realizados
- Certificações já obtidas
- Pontos de atenção identificados pelo sistema

**Uso pelo agente:** Injetado integralmente no system prompt para personalização total das respostas.

---

### `historico_estudos.csv`
Registro de todos os cursos e atividades de estudo:

| Campo | Descrição |
|---|---|
| `id` | Identificador único |
| `data` | Data de início ou conclusão |
| `plataforma` | Onde o curso foi feito |
| `curso` | Nome do curso |
| `categoria` | Área (Front-end, Back-end, IA/ML, etc.) |
| `carga_horaria` | Total de horas |
| `status` | Concluído / Em andamento / Não iniciado |
| `nota` | Nota obtida (quando disponível) |
| `certificado` | Se gerou certificado (Sim/Não) |

**Uso pelo agente:** Identifica gaps, cursos abandonados e evolução por categoria.

---

### `trilhas_disponiveis.json`
Catálogo de trilhas de carreira que o agente pode recomendar:

| Campo | Descrição |
|---|---|
| `id` | Identificador da trilha |
| `nome` | Nome da trilha |
| `nivel` | Nível alvo |
| `duracao_estimada_meses` | Estimativa de duração |
| `demanda_mercado` | Alta / Muito Alta / Média-Alta |
| `salario_junior_brl` | Faixa salarial júnior estimada |
| `etapas` | Lista ordenada de habilidades a desenvolver |
| `certificacoes_recomendadas` | Certificações relevantes para a trilha |
| `plataformas` | Onde estudar |
| `pre_requisitos_atendidos_pelo_usuario` | Se o usuário já tem o básico |

**Uso pelo agente:** Base exclusiva para recomendações de trilha — agente nunca inventa trilhas fora deste catálogo.

---

### `historico_atendimento.csv`
Histórico de sessões anteriores com o agente:

| Campo | Descrição |
|---|---|
| `id` | Identificador da sessão |
| `data` | Data da sessão |
| `duracao_min` | Duração em minutos |
| `tema` | Tema principal discutido |
| `resumo_sessao` | O que foi abordado e decidido |
| `satisfacao` | Nota de satisfação (1–5) |

**Uso pelo agente:** Dá continuidade às conversas, evitando repetição e referenciando decisões anteriores.

---

## Como Expandir a Base

Para adicionar novos dados ao sistema:

1. **Novo usuário:** Criar novo `perfil_profissional.json` com os dados do usuário
2. **Novos cursos:** Adicionar linhas ao `historico_estudos.csv`
3. **Nova trilha:** Adicionar objeto ao array `trilhas` em `trilhas_disponiveis.json`
4. **Nova sessão:** Registrar no `historico_atendimento.csv` após cada interação

Em produção, recomenda-se substituir os CSVs por um banco PostgreSQL e os JSONs por uma API REST de perfil.
