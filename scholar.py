from crawler import Crawler

localhost = False
npage = 1
new_page = True
search_term = 'Giuseppe Vizzari'

if localhost:
    scholar = Crawler(port=50002)
    scholar.visit('http://localhost/scholar.htm')
else:
    scholar = Crawler(base_url = 'http://scholar.google.com', port=50002)
    scholar.visit('/')
    scholar.search('//*[@name="q"]', search_term)

while(new_page):
    new_page = False
    divs = scholar.sess.xpath('//*[@class="gs_r"]')

    for div in divs:
        papers = div.xpath('./*[@class="gs_rt"]/a')
        print "papers: %s"%papers

        if(papers):
            print papers[0].text()

        citedbies = div.xpath('./*[@class="gs_fl"]/a')
        print "citedbies: %s"%citedbies

        if(citedbies):
            print citedbies[0]["href"]

    print npage
    pages = scholar.sess.xpath('//*[@id="gs_n"]/center/table/tbody/tr/td/a[text()="%s"]'%(npage+1))

    if(pages):
        next_page = pages[0]["href"]
        npage += 1
        new_page = True
        print next_page
        scholar.visit(next_page)
