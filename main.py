import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Fetch the page
URL = "https://www.imdb.com/chart/top/"
response = requests.get(URL)

# Step 2: Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
movies = []
rows = soup.select('tbody.lister-list tr')

for row in rows:
    title = row.select_one('.titleColumn a').text
    year = row.select_one('.titleColumn span').text.strip("()")
    rating = row.select_one('.imdbRating strong').text
    movies.append({"Title": title, "Year": year, "Rating": rating})

# Step 4: Save to a CSV file
df = pd.DataFrame(movies)
df.to_csv("imdb_top_250.csv", index=False)

print("Data saved to imdb_top_250.csv")
