from pprint import pprint
import requests
import json

# HTTP methods
# GET

response = requests.get("https://api.github.com")    # <Response [200]>

print(type(response.json()))
print(response.status_code)

# Content
# The response of a GET request often has some valuable information, known as a payload
# , in the message body. Using the attributes and methods of Response,
# you can view the payload in a variety of different formats.

response = requests.get('https://api.github.com')


decoded_content = response.content.decode("UTF-8")

# pprint(response.json())

print(json.loads(response.content) == response.json())  # True

# for k, v in response.headers.items():
#     print(k + ":", v)


response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

print(type(response))

json_response = response.json()

repository = json_response["items"][0]
print(repository["name"])
print(repository["description"])
print(repository["text_matches"])

print(requests.post('https://httpbin.org/post', data={'key':'value'}))

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])
print(response.request.url)
print(response.request.body)


from getpass import getpass
response = requests.get(
    'https://api.github.com/user',
    auth=("usernme", getpass())
)

print(response)