import requests


def resize(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    resize_coords = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["boundedBy"][
        "Envelope"]
    left_top = resize_coords["upperCorner"].split(" ")
    right_bottom = resize_coords["lowerCorner"].split(" ")
    dx = abs(float(left_top[0]) - float(right_bottom[0])) / 2
    dy = abs(float(left_top[1]) - float(right_bottom[1])) / 2
    return "{},{}".format(dx, dy)
