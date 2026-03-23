# ⚽ UEFA Champions League — Artilheiros Históricos (2012–2024)

Dashboard interativo com dados dos maiores artilheiros da UEFA Champions League nas últimas 13 temporadas.

## 🔗 [Acesse o Dashboard ao vivo](https://RafaelS26.github.io/champions-league-top-scorers/champions_dashboard_v2.html)

---

## 📊 Visão Geral

O projeto é composto por duas partes:

- **Dashboard HTML** — visualização interativa com gráficos, tabelas e animações, construído com Chart.js puro (sem frameworks)
- **Script de extração Python** — coleta os dados diretamente da API-Sports via `requests` e exporta para CSV

---

## 🗂️ Estrutura do Repositório

```
champions-league-top-scorers/
│
├── champions_dashboard_v2.html     ← Dashboard interativo (abre direto no navegador)
├── top_scorers_extractor.py        ← Script Python de extração via API
└── README.md
```

---

## 🚀 Como Usar

### Dashboard
Basta abrir o arquivo `champions_dashboard_v2.html` no navegador — não requer servidor ou instalação.

### Script de Extração
```bash
pip install pandas requests
python top_scorers_extractor.py
```

> ⚠️ O plano gratuito da API-Sports restringe o acesso a temporadas anteriores a 2022. Os dados históricos (2012–2021) do dashboard foram inseridos manualmente.

---

## 🛠️ Tecnologias

| Ferramenta | Uso |
|---|---|
| Python | Extração e tratamento de dados |
| Pandas | Manipulação e exportação CSV |
| Requests | Consumo da API REST |
| HTML / CSS / JS | Dashboard frontend |
| Chart.js | Gráficos interativos |
| API-Sports | Fonte dos dados da UCL |

---

## 📌 Observações

- Os dados cobrem as temporadas de **2012/2013 a 2024/2025**
- Métricas disponíveis: gols, assistências e chutes por jogador
- O dashboard funciona 100% offline após carregado (dados embutidos no HTML)

---

*Projeto de portfólio — Rafael Santana*  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-rafael--santana--dados-blue?logo=linkedin)](https://linkedin.com/in/rafael-santana-dados)
[![GitHub](https://img.shields.io/badge/GitHub-RafaelS26-black?logo=github)](https://github.com/RafaelS26)
