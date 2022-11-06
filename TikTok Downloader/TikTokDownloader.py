import requests
from bs4 import BeautifulSoup

payload = {
    'id': 'https://vt.tiktok.com/ZSRvvNgr1/',
    'locale': 'en',
    'tt': 'RkJtejg5'
}

resp = requests.post('https://tiktokdownload.online/abc?url=dl',data=payload)
soup = BeautifulSoup(resp.text,'lxml')

title = soup.select_one('p.maintext').text
videoDownloadLink = soup.select_one('a.without_watermark').get('href')

with open(f'{title}.mp4','wb') as f:
    chunk = requests.get(videoDownloadLink).content
    f.write(chunk)