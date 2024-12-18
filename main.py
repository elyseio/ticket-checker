import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init

def get_request(url):
    """
    Sends a GET request to the specified URL and returns the response object.
    
    Args:
        url (str): The URL to send the request to.
        
    Returns:
        Response object if the request is successful, None otherwise.
    """
    # Make request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    # Handle timeout errors
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    # Handle other request-related errors
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return None

def show_available_ticket(available_artists):
    """
    Option to show all available tickets

    Args:
        available_artists (dict): List of available artists based on check_ticket()

    Returns:
        None. Prints available tickets
    """
    ask = input(Fore.MAGENTA + "Would you like to list available artists (y/n): ")

    if ask != "y":
        return

    print()
    print("Available tickets:")
    for artist, link in available_artists.items():
        print(Fore.LIGHTBLACK_EX + "="*100)
        print(f"{artist.title()}: {Fore.CYAN + link}")
        print(Fore.LIGHTBLACK_EX + "="*100)
        print()

def check_ticket(response, artists, url, dash_num):
    """
    Parses the HTML content of the response to check for tickets for specified artists.

    Args:
        response (Response): The HTTP response object containing the page HTML.
        artists (list): A list of artist names to search for.
        url (str): The base URL for constructing ticket links.
        dash_num (int): Number of dash for the print statement
        
    Returns:
        None. Prints the ticket information if found.
    """
    # Exit if there is no artists list to check
    if not artists:
        # Warn if no artists are provided
        print("No artists specified to check tickets for.")
        return

    artist_found = False

    available_artists = {}

    soup = BeautifulSoup(response.text, "lxml")

    ticket_content = soup.find_all("div", class_="movie-item movie-item-three mb-50")

    # Return if no tickets found
    if not ticket_content:
        print("No movies found on the page.")
        return

    for ticket in ticket_content:
        title_tag = ticket.select_one(".title a")
        # Skip if there is no title
        if not title_tag:
            continue
        
        title = title_tag.get_text().strip().lower()
        link_url = url + title_tag["href"]
        available_artists[title] =  link_url
        for artist in artists:
            if artist.lower() == title:
                link_url = url + title_tag["href"]

                print("=" * dash_num)
                print(f"Ticket available for {artist.title()}")
                print(f"Link: {link_url}")
                print("=" * dash_num + "\n")
                artist_found = True

    if not artist_found:
        print(Fore.RED + f"No ticket available for {artists}\n")
        show_available_ticket(available_artists)



def main():
    """
    Main function to define the workflow of the script:
    - Defines base URL and artist list.
    - Fetches the webpage.
    - Checks for tickets of specified artists.
    """

    # Initialize colorama
    init(autoreset=True)

    # Dash numbers
    dash_num = 84

    # Opening message
    print(Fore.LIGHTBLACK_EX + "=" * dash_num)
    print(Fore.GREEN + "🎜 Ticket Checker Program Started! Checking for available tickets now...🎜")
    print(Fore.LIGHTBLACK_EX + "=" * dash_num)

    # Base URL
    base_url = "https://www.ticketnet.com.ph"
    url = "https://www.ticketnet.com.ph/event-list"

    # URL Ticket
    print(f"\nURL: {Fore.CYAN + url}")

    # What artist to check
    artists = ['coldplay', 'linkin park']

    # GET request to the website
    request = get_request(url)
    if request:
        print(f"\nChecking for these artists: {artists}\n")
        check_ticket(request, artists, base_url, dash_num)
    else:
        print("Failed to retrieve the page.")

if __name__ == "__main__":
    main()
