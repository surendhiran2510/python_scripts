import requests
import time

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is accessible")
        else:
            print(f"{url} is not accessible (Status Code: {response.status_code})")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
url = 'https://example.com'
check_website(url)
