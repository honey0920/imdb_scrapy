import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def get_page():
	try:
		url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = {'User-Agent':user_agent }
		request = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(request)
		content = response.read().decode('utf-8')
	except urllib2.URLError, e:
		if hasattr(e,"code"):
			print e.code
		if hasattr(e,"reason"):
			print e.reason
	return content

def get_movie(page,filename):
	pattern = re.compile('titleColumn">(.*?)<a href="/title/tt.*?title="(.*?)" >(.*?)</a>.*?"secondaryInfo">(.*?)</span>.*?ratingColumn '
		+'imdbRating">.*?<strong title="(.*?)">.*?</strong>',re.S)
	items = re.findall(pattern,page)
	Movies = []
	with open(filename,'w') as f:

		for item in items:
			movie = {}
			movie['No.'] = item[0].strip()
			movie['name'] = item[2]
			movie['cast'] = item[1]
			movie['year'] = item[1:-1]
			movie['score'] = item[4]
			f.write("TOP%s\nName: %s\nScore: %s\nYear: %s\nCast: %s\n" %(movie['No.'],movie['name'],movie['score'],movie['year'],movie['cast']))
			f.write("=====================================\n")
			Movies.append(movie)
	return Movies

def main():
	filename = 'top250.txt'
	content = get_page()
	Movies = get_movie(content,filename)

if __name__ == '__main__':
	main()
