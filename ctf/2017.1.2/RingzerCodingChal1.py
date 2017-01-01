import BeautifulSoup, requests
import os , hashlib

url = 'https://ringzer0team.com/challenges/13/' # challenge url
creds = {
    'username' : 'YOURUSERNAME',    #Replace with your creds
    'password' : 'YOURPASSWORD'     #in this dictionnary
}

responseurl = "https://ringzer0team.com/challenges/13/"

with requests.session() as s:
    # Login to site:
    postreq = s.post('https://ringzer0team.com/login', data=creds)
    # Go to challenge page now that we're logged in:
    page = s.get(url).content
    soup = BeautifulSoup.BeautifulSoup(page)
    # We know there's just one div result:
    div = soup.findAll('div', {'class' : 'message'})[0]
    # Extract the text as string and Remove useless garbage
    message = str(div.text)[25:-23]
    # Apply SHA512 on the message
    hashobj = hashlib.sha512(message)
    responsemsg = hashobj.hexdigest()
    #Construct the URL and open it in the browser (make sure you're logged in in your browser as well)
    url += responsemsg
    os.startfile(url)