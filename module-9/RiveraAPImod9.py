# Name: Damitrious Rivera
# Date: November 9, 2025
# Assignment: Module 9 - Working with APIs
#
# Purpose: Demonstrate how to connect to, test, and retrieve data
# from APIs using Python's requests library.

import requests
import json

# ---------------------------------------------------------------
# PART 1: TEST THE CONNECTION (per assignment instructions)
# ---------------------------------------------------------------
print("=== Testing Connection to Google ===")
response = requests.get('http://www.google.com')
print("Status Code:", response.status_code)
if response.status_code == 200:
    print("Connection successful!\n")
else:
    print("Connection failed.\n")

# ---------------------------------------------------------------
# PART 2: RETRIEVE CURRENT ASTRONAUTS (OpenNotify API)
# ---------------------------------------------------------------
print("=== Retrieving Current Astronaut Data ===")

# Correct URL provided in the assignment
astro_url = "http://api.open-notify.org/astros.json"

astro_response = requests.get(astro_url)

# Print raw response (unformatted JSON)
print("\nRaw JSON Response:")
print(astro_response.text)

# If the request succeeded, format and display readable output
if astro_response.status_code == 200:
    data = astro_response.json()

    print("\nFormatted Astronaut Data:")
    print(f"Number of astronauts currently in space: {data['number']}")
    print("People currently in space:")
    for person in data['people']:
        print(f" - {person['name']} aboard {person['craft']}")
else:
    print("Error retrieving astronaut data.")

# ---------------------------------------------------------------
# PART 3: SECOND SIMPLE API EXAMPLE
# ---------------------------------------------------------------
print("\n=== Retrieving a Random Joke from the Joke API ===")

# Simple public API (no key required)
joke_url = "https://official-joke-api.appspot.com/random_joke"
joke_response = requests.get(joke_url)

# Print raw JSON
print("\nRaw JSON Response:")
print(joke_response.text)

# Format and display joke nicely
if joke_response.status_code == 200:
    joke_data = joke_response.json()
    print("\nFormatted Joke Output:")
    print("Setup:", joke_data['setup'])
    print("Punchline:", joke_data['punchline'])
else:
    print("Error retrieving joke.")

# ---------------------------------------------------------------
# END OF PROGRAM
# ---------------------------------------------------------------
print("\n=== Program Complete ===")
