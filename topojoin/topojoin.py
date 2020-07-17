"""Main module."""
import requests
print("hello poetry world!")

r = requests.get("https://www.spotlightpa.org")
print(r.content)
