import requests, json
from dhooks import Webhook

hook = Webhook('PUT YOUR WEBHOOK LINK INTO HERE')

url = "https://mempool.space/api/v1/fees/recommended"

response = requests.get(url)
data = response.text 
parsed = json.loads(data)

fastest_rate = parsed["fastestFee"]
hook.send('The current fastest rate is: ' + str(fastest_rate) + ' sat/b')