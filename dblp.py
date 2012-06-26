import dryscrape

class Dblp():
    def __init__(self):
        self.sess = dryscrape.Session(base_url = 'http://www.informatik.uni-trier.de', port = 50001)
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('auto_load_images', False)
        self.sess.visit('/~ley/db/indices/a-tree/index.html')

    def work(self, search_term):
        q = self.sess.at_xpath('//*[@name="author"]')
        q.set(search_term)
        q.form().submit()

        print self.sess.body()

        #for link in sess.xpath('//a[@href]'):
        #  print link['href']

        #sess.render('scholar.png')
        #print "Screenshot written to 'scholar.png'"
