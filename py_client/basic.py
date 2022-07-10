import requests 


endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(url=endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abc134"}, params={'abc': 123})
print(get_response.text)
print(get_response.status_code)