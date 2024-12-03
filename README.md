# Python Ticket Event Checker

## Usage:
```
$ cd ticket/checker
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ python main.py
```


## Notes:

(artists array contains the artist you want to check, change according to the artist you want to check)
`artists = ['the script', 'the corrs']`  
base url: https://www.ticketnet.com.ph/event-list



## Sample output:
```
====================================================================================
🎫 Ticket Checker Program Started! Checking for available tickets now... 🎫
====================================================================================

URL: https://www.ticketnet.com.ph/event-list

Checking for these artists: ['the script', 'the corrs']

====================================================================================
Ticket available for The Script
Link: https://www.ticketnet.com.ph/event-detail/THE-SCRIPT-SATELLITES-WORLD-TOUR
====================================================================================

====================================================================================
Ticket available for The Corrs
Link: https://www.ticketnet.com.ph/event-detail/The-Corrs
====================================================================================

Would you like to list available artists (y/n): 
```
