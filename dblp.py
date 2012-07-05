from crawler import Crawler

def get_title(text):
    a = text[text.index(':')+1:]
    return a[:a.index('.')]

localhost = False
search_term = 'Giuseppe Vizzari'

if localhost:
    dblp = Crawler(base_url='http://localhost', port=50001)
    dblp.visit('/dblp.html')
else:
    dblp = Crawler(base_url='http://www.informatik.uni-trier.de', port=50001)
    dblp.visit('/~ley/db/indices/a-tree/index.html')
    dblp.search('//*[@name="author"]', search_term)

trs = dblp.sess.xpath('//p[1]/table/tbody/tr')
print trs

for tr in trs:
    tds = tr.xpath('./td')
    if(tds):
        print "%s -> %s"%(tds[0].text(), get_title(tds[2].text())) #tds[2].text(), 
