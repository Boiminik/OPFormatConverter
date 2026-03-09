import requests

base_url = "https://www.optcgapi.com/api/allPromos/"

def test_api(url):
    print(f"\n--- Testing URL: {url} ---")
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        print("Status Code:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("First 200 chars of response:")
        print(response.text[:200])  # nur die ersten 200 Zeichen
    except Exception as e:
        print("Request failed:", e)

if __name__ == "__main__":
    # Raw Request ohne ?format=json
    test_api(base_url)

    # Request mit ?format=json
    test_api(base_url + "?format=json")