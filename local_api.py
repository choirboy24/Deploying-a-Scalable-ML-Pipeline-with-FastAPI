import requests

url = 'http://127.0.0.1:8000'

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get(url=url)

# TODO: print the status code
print(f'Status Code: {r.status_code}')
# TODO: print the welcome message
print(f'Results: {r.json()}')


local_data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send a POST using the data above
r2 = requests.post("http://127.0.0.1:8000/data/", json=local_data)
# Print the status code
print(f'Status Code: {r2.status_code}')
# Print the result
if r2.status_code == 200:
    results = list(r2.json().values())
    print(f'Results: {results[0]}')
else:
    print('Failed to retrieve results.  You suck.')
