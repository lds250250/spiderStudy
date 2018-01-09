import json
import re

import requests
from requests.exceptions import RequestException


class Spider():
    def __init__(self, offset):
        self.Url = f'http://maoyan.com/board/4?offset={offset}'
        self.root_pattern = (
            '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">' +
            '<a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' +
            '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>')

    def __get_one_page(self):
        try:
            response = requests.get(self.Url)
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            return None

    def __parse_one_page(self, html):

        pattern = re.compile(self.root_pattern, re.S)
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

    def __write_to_file(self, content):
        with open('maoyan100.txt', 'a', encoding="utf8") as f:
            f.write(json.dumps(content, ensure_ascii=False) + '\n')
            f.close()

    def go(self, offset):
        html = self.__get_one_page()
        for item in self.__parse_one_page(html):
            print(item)
            self.__write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        spider = Spider(i * 10)
        spider.go(i * 10)
