import bs4
import requests
import os
import pytesseract
import base64
from PIL import Image, ImageDraw

"""
DISCLAIMER: I'm relying on tesseract to get the text out of the image, so it might not succeed
100% of the time. But it will definitely succeed in a max of 2 to 3 attempts.
"""

url = 'https://ringzer0team.com/challenges/17/'  # Challenge url
creds = {
    'username': 'YOURUSERNAME',     # Replace with your creds
    'password': 'YOURPASSWORD'      # in this dictionnary
}


# Turn colored pixels into white pixels but keep our text distinct
def ethnic_cleansing(image, d):
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if image.getpixel((x, y)) == (255, 255, 255):
                d.point((x, y), (0, 0, 0))
            else:
                d.point((x, y), (255, 255, 255))
    print 'Done processing image'


with requests.session() as s:
    # Login to site:
    postreq = s.post('https://ringzer0team.com/login', data=creds)
    # Go to challenge page now that we're logged in:
    page = s.get(url).content
    soup = bs4.BeautifulSoup(page)

    div = soup.findAll('div', {'class': 'message'})
    imagesrc = div[0].img['src']
    # We know the extension is png, so get rid of the meta data and keep the base64 encoded data
    imagedata = str(imagesrc).split(',', 1)[1]
    decdata = base64.b64decode(imagedata)
    # We'll have to save this in a png file and read from it with pillow, pls don't hate me.
    with open('imagetext.png', 'wb') as f:
        f.write(decdata)
    # Fetch image for pillow:
    img = Image.open('imagetext.png')
    draw = ImageDraw.Draw(img)
    ethnic_cleansing(img, draw)
    img.save('imagetext.png')
    # Let the OCR do its magic
    text = pytesseract.image_to_string(img)
    print "Done extracting text:" + text
    # Construct the URL and open it in the browser (make sure you're logged in in your browser as well)
    url += text
    os.startfile(url)
