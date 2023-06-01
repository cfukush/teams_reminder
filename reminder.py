import json
import requests

with open('reminder.py', 'r') as f:
	card = json.load(f)

incoming_webhook_url = "webhook_url" 

data = json.dumps(card)

requests.post(
	incoming_webhook_url,
	data = data
)


