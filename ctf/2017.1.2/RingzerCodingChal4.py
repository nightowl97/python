import BeautifulSoup
import requests
import os

url = 'https://ringzer0team.com/challenges/32/'  # challenge url
creds = {
    'username': 'YOURUSERNAME',     # Replace with your creds
    'password': 'YOURPASSWORD'      # in this dictionary
}


with requests.session() as s:
    # Login to site:
    postreq = s.post('https://ringzer0team.com/login', data=creds)
    # Go to challenge page now that we're logged in:
    page = s.get(url).content
    soup = BeautifulSoup.BeautifulSoup(page)
    # We know there's just one div result:
    div = soup.findAll('div', {'class': 'message'})[0]
    # Extract the text as string and remove useless garbage
    message = str(div.text)[25:-23]
    ops = message.split(' ')
    result = int(ops[0]) + int(ops[2], 16) - int(ops[4], 2)
    # Construct the URL and open it in the browser (make sure you're logged in in your browser as well)
    url += str(result)
    os.startfile(url)
