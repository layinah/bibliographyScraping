import dryscrape

class Crawler():
    def __init__(self, base_url=None, port=None):
        self.sess = dryscrape.Session(base_url = base_url, port = port)
        self.sess.set_error_tolerant(True)
        self.sess.set_attribute('auto_load_images', False)

    def visit(self, url):
        self.sess.visit(url)

    def search(self, search_field, search_term):
        qs = self.sess.xpath(search_field)
        q = qs[0]
        q.set(search_term)
        q.form().submit()
        return self.sess.body()
