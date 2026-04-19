# 04 — Avaliação e Métricas

## Objetivo

Garantir que o MentorIA entrega respostas que são ao mesmo tempo **úteis, personalizadas e confiáveis** — sem alucinações sobre trilhas, salários ou certificações.

---

## Métricas Principais

### 1. Relevância ao Perfil (0–5)
Avalia se a resposta levou em conta os dados reais do usuário (habilidades, cursos em andamento, objetivos).

| Pontuação | Critério |
|---|---|
| 5 | Resposta 100% personalizada, cita dados do perfil explicitamente |
| 4 | Levou o perfil em conta, mas poderia ser mais específica |
| 3 | Resposta válida, mas genérica — poderia ser dada a qualquer pessoa |
| 1–2 | Ignorou o perfil completamente |

**Meta:** ≥ 4,0 de média.

---

### 2. Ausência de Alucinações (Pass/Fail)
Verifica se trilhas, plataformas, certificações ou faixas salariais mencionadas estão na base de conhecimento.

**Critério de falha:** Qualquer recomendação de trilha, curso ou certificação que não conste no `trilhas_disponiveis.json`.

**Meta:** 100% de Pass.

---

### 3. Acionabilidade da Resposta (0–5)
Avalia se a resposta gera uma ação clara que o usuário pode tomar imediatamente.

| Pontuação | Critério |
|---|---|
| 5 | Próximo passo definido, com prazo e recurso específico |
| 4 | Orienta bem, mas sem prazo claro |
| 3 | Resposta informativa, mas sem call-to-action |
| 1–2 | Vaga demais para gerar qualquer ação |

**Meta:** ≥ 4,0 de média.

---

### 4. Satisfação do Usuário (1–5)
Coletada ao final de cada sessão com uma pergunta simples:

> "Essa orientação foi útil para você? (1 = Não ajudou / 5 = Muito útil)"

**Meta:** ≥ 4,0 de média (referência: histórico atual do usuário é 4,5).

---

### 5. Taxa de Redirecionamento Correto (%)
Quando o usuário faz uma pergunta fora do escopo, o agente deve redirecionar sem frustrar.

**Meta:** 100% das perguntas fora de escopo redirecionadas de forma amigável.

---

## Cenários de Teste Sugeridos

| Cenário | Comportamento Esperado |
|---|---|
| "Me recomenda uma trilha" | Citar trilha do catálogo com etapas e prazo realista |
| "Quanto vou ganhar?" | Dar faixas do JSON + disclaimer de estimativa |
| "O que devo estudar essa semana?" | Mencionar cursos em andamento + plano prático |
| "Me ensina machine learning do zero" | Verificar pré-requisitos e avisar se não estão atendidos |
| "Qual a capital da França?" | Redirecionar para escopo de carreira/estudos |
| "Existe a certificação XYZ?" (inexistente) | Afirmar que não está no catálogo e sugerir alternativa real |

---

## Ferramenta de Avaliação Sugerida

Para avaliação mais formal, utilizar **LLM-as-judge**: enviar a conversa + critérios acima para um segundo modelo (ex: Claude Opus) e pedir pontuação estruturada em JSON.

```python
avaliacao_prompt = """
Avalie a resposta do agente nos seguintes critérios (0-5 cada):
- relevancia_ao_perfil
- acionabilidade
- ausencia_de_alucinacao (0 ou 5 apenas)

Responda apenas em JSON.

Pergunta do usuário: {pergunta}
Resposta do agente: {resposta}
Dados do perfil: {perfil}
"""
```
