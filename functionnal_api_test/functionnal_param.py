import json


def get_endpoint_base_url():
    with open("C:/Users/oumayma.sebbata/PycharmProjects/api_test/pythonProject/config/endpoint.json") as json_file :
        properties = json.load(json_file)
        env = properties["environment"]["env"]
        return properties[env]['base_url']


get_endpoint_base_url()