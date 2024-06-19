import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Application at {url} is UP and functioning correctly.")
        else:
            print(f"Application at {url} is DOWN with status code {response.status_code}.")
    except requests.ConnectionError:
        print(f"Could not connect to the application at {url}. It may be DOWN or unreachable.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    application_url = "http://example.com"
    check_application_health(application_url)
