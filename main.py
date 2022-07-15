import requests
import json

response = requests.get("https://newsline.kg/getNews.php?limit=30&last_dt=2022-07-04%2007:57:33.933739")
result_json = json.JSONDecoder().decode(response.text)

with open('news.json', 'w', encoding='utf-8') as f:
    json.dump(result_json, f, indent=4, ensure_ascii=False)