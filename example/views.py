# example/views.py
from datetime import datetime

from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup



def run(day):
    def get_scores(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html5lib')
        mdsoup = soup.find('div', {"id": "score-data"})
        # deep_mdsoup = mdsoup.find_all('h4')
        # listmd = deep_mdsoup.text
        # print(listmd)
        textsoup = []
        # for x in mdsoup:
        #     # textsoup.append(x.text)
        #     x.span.unwrap()
        #
        match = []
        h4_tags = mdsoup.find_all('h4')

        # Clear the content of each h4 tag
        for tag in h4_tags:
            tag.decompose()

        fullres = []
        for des in mdsoup.find_all('span'):

            try:
                time = des.text
                match = des.next_sibling
                result = des.next_sibling.next_sibling.text
                parts = match.split(' - ')
                fullres.append({'time': time, 'home': parts[0], 'away': parts[1], 'result': result})
            except Exception:
                print(Exception)
        for span in mdsoup:
            next_tag = span.find_next()
        return fullres

    # Use the function
    if (day == 0):
        return get_scores('https://www.flashscore.mobi/')
    else:
        return get_scores('https://www.flashscore.mobi/?d=' + str(day))


def index(request):
    now = datetime.now()
    datas = []
    data = []
    if request.method == "POST":
        data = json.loads(request.body.decode())
        datas = run(data['day'])
    else:
        datas = [{"status":"error","message":"send only POST requests in body"}]
    html = f'''
    <html>
        <body>
        <h1>{data}</h1>
          {datas}
        </body>
    </html>
    '''
    return HttpResponse(json.dumps(datas))
