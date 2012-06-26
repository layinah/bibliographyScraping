import dryscrape

class Scholar():
    def __init__(self):
        self.sess = dryscrape.Session(base_url = 'http://scholar.google.com', port = 50002)
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('auto_load_images', False)
        self.sess.visit('/')

    def work(self, search_term):
        q = self.sess.at_xpath('//*[@name="q"]')
        print q
        q.set(search_term)
        q.form().submit()

        print self.sess.body()

        #for link in sess.xpath('//a[@href]'):
        #  print link['href']

        #sess.render('scholar.png')
        #print "Screenshot written to 'scholar.png'"
