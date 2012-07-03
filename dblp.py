from crawler import Crawler

search_term = 'Giuseppe Vizzari'

dblp = Crawler('http://www.informatik.uni-trier.de', 50001)
dblp.visit('/~ley/db/indices/a-tree/index.html')
result = dblp.search('//*[@name="author"]', search_term)
