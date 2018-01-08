import json
import re

import requests
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pa = ('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">' +
          '<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' +
          '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>')
    pattern = re.compile(pa, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('maoyan100.txt', 'a', encoding="utf8") as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = f'http://maoyan.com/board/4?offset={offset}'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i * 10)
