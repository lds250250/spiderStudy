import re
from urllib import request


class Spider():
    url = 'https://www.douyu.com/directory/game/TVgame'
    root_pattern = '<div class="mes">[\s\S]*?<p>([\s\S]*?)</p>[\s\S]*?</div>'
    name_pattern = '<span class="dy-name ellipsis fl">([\s\S]*?)</span>'
    number_pattern = '<span class="dy-num fr"  >([\s\S]*?)</span>'

    def __fetch_contect(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'主播名字': name, '人数': number}
            anchors.append(anchor)
        return (anchors)

    def __refine(self, anchors):
        def l(anchor):
            return {
                '主播名字': anchor['主播名字'][0].strip(),
                '人数': anchor['人数'][0],
            }

        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['人数'])
        number = float(r[0])
        if '万' in anchor['人数']:
            number *= 10000
        return number

    def __show(self, anchors):
        for i in range(0, len(anchors)):
            print('第' + str(i + 1) + ' : ' + anchors[i]['主播名字'] + '    ' +
                  anchors[i]['人数'] + '人')

    def go(self):
        htmls = self.__fetch_contect()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
