from crawler import Crawler

search_term = 'Giuseppe Vizzari'

dblp = Crawler('http://scholar.google.com', 50002)
dblp.visit('/')
result = dblp.search('//*[@name="q"]', search_term)
