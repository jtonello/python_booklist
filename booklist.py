import requests

# Take input from the command line
author_search = input("Enter the author: ")
title_search  = input("Enter the title: ")

# Adjust the search values based on what the user entered
if author_search and title_search:
    author = "inauthor:" + author_search + "+"
    title = "intitle:" + title_search 
    search = author + title
else:
    if len(author_search) > 0:
        search = "inauthor:" + author_search
    if len(title_search) > 0:
        search = "intitle:" + title_search 

# Fetch the JSON content via this URL to the Google API
url = "https://www.googleapis.com/books/v1/volumes?q=" + search + "&key=ENTER-YOUR-GOOGLE-API-KEY&startIndex=0&maxResults=40"

# Show the URL -- for testing only
# print(url)

# Use the imported requests function to get the URL
r = requests.get(url)

# Decode the returned JSON
j = r.json()

# Iterate over the JSON array of data and return titles and authors
for book in j['items']:
    print(book['volumeInfo']['title'] + " -- By " + book['volumeInfo']['authors'][0])



