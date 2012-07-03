import dryscrape

class Crawler():
    def __init__(self, base_url, port):
        self.sess = dryscrape.Session(base_url = base_url, port = port)
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('auto_load_images', False)

    def visit(self, url):
        self.sess.visit(url)

    def search(self, search_field, search_term):
        q = self.sess.at_xpath(search_field)
        q.set(search_term)
        q.form().submit()
        return self.sess.body()
