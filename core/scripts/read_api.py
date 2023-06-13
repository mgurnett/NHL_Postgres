import requests

def read_api (endpoint):

    # Set up the request URL and headers
    base_url = "https://statsapi.web.nhl.com/api/v1/"
    # endpoint = "your_endpoint"  # Replace with the actual endpoint you want to access
    url = base_url + endpoint
    headers = {
        "User-Agent": "Mozilla/5.0",  # Set a user agent to avoid potential issues
        # Add any required headers or authentication tokens specified in the API documentation
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Process the response data
        data = response.json()
        # Extract and use the desired information from the 'data' variable
        # ...
    else:
        print("Request failed with status code:", response.status_code)
    
    return data

if __name__ == '__main__':
    data = read_api ('divisions')
    print (data)
    for record in data ['divisions']:
        name = record['name']
        print (name)



'''
{'copyright': 'NHL and the NHL Shield are registered trademarks of the National Hockey League. 
NHL and NHL team marks are the property of the NHL and its teams. © NHL 2023. All Rights Reserved.', 
    'divisions':  <--------------  see: for record in data ['divisions']:
    [{'id': 17, 'name': 'Atlanti
'''
