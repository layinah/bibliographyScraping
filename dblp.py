import dryscrape

# set up a web scraping session
sess = dryscrape.Session(base_url = 'http://www.informatik.uni-trier.de')
#sess = dryscrape.Session(base_url = 'http://www.dblp.org')

# there are some failing HTTP requests, so we need to enter
# a more error-resistant mode (like real browsers do)
sess.set_error_tolerant(True)

# we don't need images
sess.set_attribute('auto_load_images', False)

# visit homepage and search for a term
sess.visit('/~ley/db/indices/a-tree/index.html')
#sess.visit('/search/index.php')

# save a screenshot of the web page
sess.render('dblp.png')
print "Screenshot written to 'dblp.png'"

q = sess.at_xpath('//*[@name="author"]')
#q = sess.at_xpath('//*[@name="query"]')
search_term = 'Giuseppe Vizzari'
q.set(search_term)
q.form().submit()

# extract all links
for link in sess.xpath('//a[@href]'):
  print link['href']

# save a screenshot of the web page
sess.render('dblp.png')
print "Screenshot written to 'dblp.png'"
