import requests
from base64 import b64encode
from customerio import APIClient, SendEmailRequest, CustomerIOException

res = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
        )
if res.status_code == requests.codes.ok:
    todays_joke = "Joke of the day:\n" + str(res.json()['joke'])
else:
    todays_joke = ''
    
api = APIClient("a855d7a169e484e0bdc91b11d6660327")
request = SendEmailRequest(
    to="chrisiglesias@lgcypower.com",
    transactional_message_id="2",
    identifiers={
        "id": "1660324645"
    },
    _from="dondufour@lgcypower.com",
    subject=f"Joke of the Day",
    body=f"{todays_joke}",
)
print(todays_joke)
api.send_email(request)
