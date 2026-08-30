import requests

APIkey="dbc4e41f0eea8a5d8a663dfbd71e0be1"

def get_data(place_local, days_local):
    url = (f"https://api.openweathermap.org/data/2.5/forecast?q={place_local}&"
           f"cnt={days_local*8}&units=imperial&appid={APIkey}")
    response = requests.get(url)
    weather_dictionary = response.json()
    dates_to_plot = [weather_dictionary["list"][i]["dt_txt"] for i in range(weather_dictionary["cnt"])]
    temps_to_plot = [weather_dictionary["list"][i]["main"]["temp"] for i in range(weather_dictionary["cnt"])]
    feels_like_to_plot = [weather_dictionary["list"][i]["main"]["feels_like"] for
                          i in range(weather_dictionary["cnt"])]
    sky_conditions = [weather_dictionary["list"][i]["weather"][0]["main"] for
                      i in range(weather_dictionary["cnt"])]
    sky_descriptions = [weather_dictionary["list"][i]["weather"][0]["description"] for
                      i in range(weather_dictionary["cnt"])]
    sky_images = [f"images/{sky.lower()}.png" for sky in sky_conditions]
    return dates_to_plot, temps_to_plot, feels_like_to_plot, sky_images, sky_descriptions





