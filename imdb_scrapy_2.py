import requests
from lxml import html

def get_movie(url):
	content = requests.get(url).content
	sel = html.fromstring(content)
	Movies =[]
	for i in sel.xpath('//td[@class="titleColumn"]'):
		movie = {}
		movie['No.']=i.xpath('./text()')[0].strip()
		movie['name'] = i.xpath('a/text()')[0]
		movie['cast'] = i.xpath('a/@title')[0]
		movie['year'] =i.xpath('span[@class="secondaryInfo"]/text()')[0]
		Movies.append(movie)

	index = 0
	for i in sel.xpath('//td[@class="ratingColumn imdbRating"]'):
		score =i.xpath('strong/@title')[0]
		Movies[index]['score'] = score
		index=index+1

def print_movie(Movies):
	for movie in Movies:
		print 'TOP'+movie['No.']
		print 'Name: '+movie['name']
		print 'Score: '+movie['score']
		print 'Year: '+movie['year']
		print 'Cast: '+movie['cast']
		print '================='


def main():
	url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6' 
	Movies = get_movie(url)
	print(Movies)

if __name__ =='__main__':
	main()