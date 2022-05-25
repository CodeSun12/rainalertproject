import requests
from twilio.rest import Client

# TODO This Api Key is basically our Account Number Name.
api_key = "861fed2417f9ce3b28eb5979d5674133"


# lat = 30.201920
# long = 71.453056

account_sid = "AC83c24c274943a82dd698596718423dfb"
auth_token = "395a8acf5a95db28d880d7f6e29ff65c"

parameters = {
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=31.561920&lon=74.348083&exclude={"
                             "part}&appid=861fed2417f9ce3b28eb5979d5674133", params=parameters)

response.raise_for_status()
data = response.json()
# hourly_weather_report = data["hourly"][0]["weather"][0]["id"]

will_rain = False
weather_slide = data["hourly"][:12]
for hour_data in weather_slide:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Please bring your Umbrella with you.",
        from_='+18637775284',
        to='+923147896819'
    )
    # print("Bring An Umbrella With You Today")






# TODO we can write this code in this way too
# api_key = "861fed2417f9ce3b28eb5979d5674133"
# OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
# MY_LAT = 30.201920
# MY_LONG = 71.453056
#
# weather_params = {
#     "lat": MY_LAT,
#     "long": MY_LONG,
#     "appid": api_key,
# }
#
# response = requests.get(OWM_ENDPOINT, params=weather_params)
# data = response.json()
# print(data)
