import requests

url = "https://type.fit/api/quotes"
res = requests.get(url=url)
data = res.json()
for i in range(len(data)):
    quote = data[i]['text']
    author = data[i]['author'].split(",")[0]
    print(f"quote # {i+1}")
    print("Quote: ", quote, "\nAuthor:", author )