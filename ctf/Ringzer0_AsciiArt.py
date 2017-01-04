import BeautifulSoup
import requests
import os

cleanlist = []
numslist = []
result = ''
url = 'https://ringzer0team.com/challenges/119/'  # Challenge url
creds = {
    'username': 'YOURUSERNAME',     # Replace with your creds
    'password': 'YOURPASSWORD'      # in this dictionnary
}


# Checks against sufficient conditions to return letter, Messy but necessary
def identify(l):
    # Number 0:
    if l[0] == ' xxx ' and l[-1] == ' xxx ' and l[2] == 'x   x':
        return '0'
    # Number 1:
    elif l[0] == ' xx  ' and l[1] == 'x x  ' and l[-1] == 'xxxxx':
        return '1'
    # Number 2:
    elif l[0] == ' xxx ' and l[2] == '  xx ' and l[-1] == 'xxxxx':
        return '2'
    # Number 8:
    elif l[0] == ' xxx ' and l[2] == '  xx ' and l[-1] == ' xxx ':
        return '8'
    # Number 4:
    # TODO: Unsure if this is the reason of occasional failure (return 9 instead of 4)
    # But hey, it'll still get you the flag in a 2 or 3 attempts
    elif l[0] == ' x   x' and l[1] == 'x    x' and l[2] == ' xxxxx':
        return '4'
    # Number 5:
    elif l[0] == 'xxxxx' and l[2] == ' xxxx' and l[-1] == 'xxxxx':
        return '5'
    else:
        return 'unknown letter'

with requests.session() as s:
    # Login to site:
    postreq = s.post('https://ringzer0team.com/login', data=creds)
    # Go to challenge page now that we're logged in:
    page = s.get(url).content
    soup = BeautifulSoup.BeautifulSoup(page)
    # Make a list from lines that contain 'x'
    div = soup.findAll('div', {'class': 'message'})[0]
    linelist = div.contents[1:-1]
    linelist = [x for x in linelist if 'x' in str(x)]

    # Replace garbage with ' ' and give us list of sublists where each sublist represents a number
    for i in range(len(linelist)):
        cleanlist.append(str(linelist[i]).replace('&nbsp;', ' '))
    for i in xrange(0, len(cleanlist), 5):
        numslist.append(cleanlist[i:i+5])
    # Identify the number from each sublist and add it to our result string
    for n in numslist:
        result += identify(n)
    # Construct the url and open in browser
    url += result
    os.startfile(url)
