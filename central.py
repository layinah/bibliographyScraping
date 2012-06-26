from scholar import Scholar
from dblp import Dblp

s = Scholar()
d = Dblp()
search_term = 'Giuseppe Vizzari'

s.work(search_term)
d.work(search_term)
