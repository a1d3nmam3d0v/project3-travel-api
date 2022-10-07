import requests

url = "https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers= {
  "apikey": "Nvqg6mTuZJzXbbxPvB04J4BuDcCMeJcA"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text