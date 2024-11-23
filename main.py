import requests
from bs4 import BeautifulSoup

def get_request(url):
    # Make request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return None

def check_ticket(response, artists, url):
    soup = BeautifulSoup(response.text, "lxml")

    movie_content = soup.find_all("div", class_="movie-item movie-item-three mb-50")

    if not movie_content:
        print("No movies found on the page.")
        return

    for movie in movie_content:
        title_tag = movie.select_one(".title a")
        if not title_tag:
            continue
        
        title = title_tag.get_text().strip().lower()
        for artist in artists:
            if artist.lower() == title:
                link_url = url + title_tag["href"]

                print("=" * 64)
                print(f"Ticket available for {artist}")
                print(f"Link: {link_url}")
                print("=" * 64 + "\n")

def main():
    base_url = "https://www.ticketnet.com.ph"
    url = "https://www.ticketnet.com.ph/event-list"

    artists = ['the script', 'the corrs']

    request = get_request(url)
    if request:
        check_ticket(request, artists, base_url)
    else:
        print("Failed to retrieve the page.")

if __name__ == "__main__":
    main()
