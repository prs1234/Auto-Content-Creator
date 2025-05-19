from googleapiclient.discovery import build

def google_search(query, api_key, cse_id, num=3):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, num=num).execute()
    results = []
    for item in res.get('items', []):
        results.append({
            'title': item['title'],
            'link': item['link'],
            'snippet': item['snippet']
        })
    return results
