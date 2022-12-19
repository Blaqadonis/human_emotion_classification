import requests

url =  " https://84qh5luh2i.execute-api.us-east-1.amazonaws.com/test/predict"
data = {
   
    "url": "https://i.pinimg.com/originals/6a/ef/bb/6aefbbc556900e05a336d8a616a310d6.jpg"
}


results = requests.post(url, json=data).json()

print(results)