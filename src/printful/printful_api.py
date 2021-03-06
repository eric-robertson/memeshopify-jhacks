#pyhon 3.x

# importing the requests library
import requests

import base64

# your API key here
API_KEY_BYTES = b'XXXXXXXXXXXXXXXXX'
BASE_64_API_BYTES = base64.b64encode(API_KEY_BYTES)
BASE_64_API = (BASE_64_API_BYTES).decode("utf-8")

def createItem (url_path):

    # defining the api-endpoint
    API_ENDPOINT = "https://api.printful.com/store/products"

    # data to be sent to api
    data = {
        "sync_product": {
            "name": "API EXAMPLE",
            "thumbnail": url_path,
        },
        "sync_variants": [
            {
                "retail_price": "21.00",
                "variant_id": 4011,
                "files": [
                    {
                        "url": url_path,
                    },
                ]
            },
            {
                "retail_price": "21.00",
                "variant_id": 4012,
                "files": [
                    {
                        "url": url_path,
                    },
                ]
            },
            {
                "retail_price": "21.00",
                "variant_id": 4013,
                "files": [
                    {
                        "url": url_path,
                    },
                ]
            }
        ]
    }

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, json = data, headers = {"Authorization" : ("Basic " + BASE_64_API)})

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)


def deleteItem ():

    # defining the api-endpoint
    API_ENDPOINT = "http://pastebin.com/api/api_post.php"

    # your API key here
    API_KEY = "XXXXXXXXXXXXXXXXX"

    # your source code here
    source_code = '''
    print("Hello, world!")
    a = 1
    b = 2
    print(a + b)
    '''

    # data to be sent to api
    data = {'api_dev_key':API_KEY,
            'api_option':'paste',
            'api_paste_code':source_code,
            'api_paste_format':'python'}

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)


def listItems ():

    # api-endpoint
    URL = "http://maps.googleapis.com/maps/api/geocode/json"

    # location given here
    location = "delhi technological university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address':location}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()


    # extracting latitude, longitude and formatted address
    # of the first matching location
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']

    # printing the output
    print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
          %(latitude, longitude,formatted_address))


def modifyItem ():

    # defining the api-endpoint
    API_ENDPOINT = "http://pastebin.com/api/api_post.php"

    # your API key here
    API_KEY = "XXXXXXXXXXXXXXXXX"

    # your source code here
    source_code = '''
    print("Hello, world!")
    a = 1
    b = 2
    print(a + b)
    '''

    # data to be sent to api
    data = {'api_dev_key':API_KEY,
            'api_option':'paste',
            'api_paste_code':source_code,
            'api_paste_format':'python'}

    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = data)

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s"%pastebin_url)


##MAIN TEST

createItem("https://i.redd.it/jdvvnuqq4ay21.jpg")
