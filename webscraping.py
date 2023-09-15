import requests
from bs4 import BeautifulSoup

# Define the URL of Doraemon's Wikipedia page
url = "https://en.wikipedia.org/wiki/Doraemon"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Find the main content section
        content = soup.find(id="mw-content-text")

        # Extract the main article text
        article_text = ""
        for paragraph in content.find_all("p"):
            article_text += paragraph.text + "\n"

        # Save the information to a text file
        with open("doraemon.txt", "w", encoding="utf-8") as file:
            file.write(article_text)

        print("Information about Doraemon has been successfully scraped and saved to 'doraemon.txt'.")

    else:
        print("Failed to retrieve data from the Wikipedia page. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", str(e))
