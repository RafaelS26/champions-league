⚽ UEFA Champions League — Artilheiros Históricos (2012–2024)
Dashboard interativo com dados dos maiores artilheiros da UEFA Champions League nas últimas 13 temporadas.

🔗 Acesse o Dashboard ao vivo
📊 Visão Geral
O projeto é composto por duas partes:

Dashboard HTML — visualização interativa com gráficos, tabelas e animações, construída com Chart.js puro (sem frameworks)
Script de remoção Python — coleta dos dados diretamente da API-Sports via requestse exporta para CSV
🗂️ Estrutura do Repositório
champions-league-top-scorers/
│
├── champions_dashboard_v2.html     ← Dashboard interativo (abre direto no navegador)
├── top_scorers_extractor.py        ← Script Python de extração via API
└── README.md
🚀 Como Usar
Painel
Basta abrir o arquivo champions_dashboard_v2.htmlno navegador — não requer servidor ou instalação.

Script de Extração
pip install pandas requests
python top_scorers_extractor.py
⚠️O plano gratuito da API-Sports restringe o acesso às temporadas anteriores a 2022. Os dados históricos (2012–2021) do dashboard foram inseridos manualmente.

🛠️ Tecnologias
Ferramenta	Uso
Python	Extração e tratamento de dados
Pandas	Manipulação e exportação CSV
Solicitações	Consumo da API REST
HTML / CSS / JS	Interface do painel de controle
Chart.js	Gráficos interativos
API-Esportes	Fonte dos dados da UCL
📌 Observações
Os dados cobrem as temporadas de 2012/2013 a 2024/2025
Métricas disponíveis: gols, assistências e chutes por jogador
O dashboard funciona 100% offline após carregado (dados embutidos no HTML)
Projeto de portfólio — Rafael Santana
LinkedIn GitHub# champions-league
