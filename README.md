# Python Ticket Event Checker (WIP)

A Python CLI program to check for concerts/events based on specified artists.

---

## Usage

Follow these steps to run the program:

1. Clone the repository and navigate to the project directory:
   ```bash
   $ cd ticket-checker
   ```

2. Create and activate a virtual environment:
   ```bash
   $ python -m venv .venv
   $ source .venv/bin/activate  # For Linux/Mac
   $ .venv\Scripts\activate    # For Windows
   ```

3. Install the required dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```

4. Run the program:
   ```bash
   $ python main.py
   ```

---

## Configuration

You can customize the artists you want to check by modifying the `artists` array in `main.py`:

```python
# main.py
# Line 139
artists = ['the script', 'the corrs']
```

Add or change the artists in the array to fit your needs.

---

## Base URL

The program fetches event details from the following base URL:
- [Ticketnet Event List](https://www.ticketnet.com.ph/event-list)

---

## Sample Output

```text
====================================================================================
🎜 Ticket Checker Program Started! Checking for available tickets now... 🎜
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

---

## Notes

- Ensure the `artists` array contains the names of the artists you want to track.
- The program is case-insensitive when checking for artist names.

Feel free to customize the `artists` array and adapt the program to your requirements!

