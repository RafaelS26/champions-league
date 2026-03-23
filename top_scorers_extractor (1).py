import pandas as pd
import requests
import time

# ============================================================
# UEFA Champions League — Extração de Artilheiros Históricos
# Fonte: API-Sports (https://www.api-football.com/)
# Liga ID: 2 (UEFA Champions League)
# Temporadas: 2012 a 2024
# ============================================================

# Configurações da API
api_key = 'SUA_CHAVE_AQUI'  # Substitua pela sua chave em api-sports.io
base_url = "https://v3.football.api-sports.io/players/topscorers"
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': api_key
}

# Temporadas desejadas
temporadas = range(2012, 2025)
todos_artilheiros = []

print("Iniciando extração de dados...")

for ano in temporadas:
    print(f"Buscando temporada {ano}/{ano+1}...")

    params = {'league': '2', 'season': str(ano)}
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        # Verifica erros explícitos da API
        # Nota: o plano gratuito restringe temporadas anteriores a 2022
        if data.get('errors'):
            print(f"   ERRO DA API (Temporada {ano}): {data['errors']}")

        scorers = data.get('response', [])

        if not scorers:
            print(f"   Aviso: Sem dados para {ano}. (Restrição do plano gratuito)")
        else:
            for item in scorers:
                todos_artilheiros.append({
                    'Temporada': f"{ano}/{ano+1}",
                    'Jogador': item['player']['name'],
                    'Time': item['statistics'][0]['team']['name'],
                    'Gols': item['statistics'][0]['goals']['total']
                })
            print(f"   OK: {len(scorers)} registros encontrados.")
    else:
        print(f"   Erro HTTP na temporada {ano}: {response.status_code} - {response.reason}")

    # Pausa entre requisições para respeitar o rate limit da API
    time.sleep(2)

# Criando o DataFrame final
df_final = pd.DataFrame(todos_artilheiros)

# Ordenando por temporada e gols (decrescente)
df_final = df_final.sort_values(by=['Temporada', 'Gols'], ascending=[True, False])

# Exportando para CSV (compatível com Looker Studio e Google Sheets)
df_final.to_csv('artilheiros_champions_2012_2024.csv', index=False, encoding='utf-8-sig')

print("\nArquivo 'artilheiros_champions_2012_2024.csv' gerado com sucesso!")
print(f"Total de registros: {len(df_final)}")
