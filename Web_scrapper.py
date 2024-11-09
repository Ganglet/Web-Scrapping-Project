import threading
import requests
from bs4 import BeautifulSoup
urls=[
    'https://developers.google.com/',
    'https://developers.google.com/products',
    'https://developers.google.com/products/developer-platforms-and-os?category=devsitemarketingplatformsandoperatingsystems',
    'https://cloud.google.com/docs?hl=en',
    'https://cloud.google.com/docs/ai-ml?hl=en'
]
def content_fetch(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched: {len(soup.text)} from {url}')

threads=[]
for url in urls:
    thread=threading.Thread(target=content_fetch,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")