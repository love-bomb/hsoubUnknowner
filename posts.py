# Oldest : 73985
# New Newest https://io.hsoub.com/go/75935

from bs4 import BeautifulSoup
import urllib.request
import time
from random import randint
number = 0
unknown = b'\xd9\x85\xd8\xb3\xd8\xaa\xd8\xae\xd8\xaf\xd9\x85 \xd9\x85\xd8\xac\xd9\x87\xd9\x88\xd9\x84' # Chinese, Don't touch it plz

def last_post():
	# Grabbing last post number
	page = requests.get('https://io.hsoub.com/new')
	soup = BeautifulSoup(page.content, 'lxml')

	post = soup.find('span', {'class':'commentsCounter'})

	return post.find('a')['href'].split('/')[2].split('-')[0] # a bit messy, but it does the job!


first = 73985 #Don't touch this, and don't put 1, we don't want to crash Hsoub servers
last = last_post() # you don't have to #Go to https://io.hsoub.com/new and get the latest topic (better do it in private browser mode)

for i in range(first,last + 1):
	url = "https://io.hsoub.com/go/{}".format(i)
	try:
		req = urllib.request.Request(
			url, 
			data=None, 
			headers={
				'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
			}
		)
		
		content = urllib.request.urlopen(url).read()

		soup = BeautifulSoup(content)

		spans = soup.find_all('span', {'class' : 'postUsername'})

		string = spans[0].string.encode('utf-8')

		if (unknown in string):
			number += 1
	except urllib.error.HTTPError as e:
		print("Error in {} - Code: {}".format(i, e.code))
	print('No : {}'.format(i))
	time.sleep(3 + randint(0,3))
	
with open("output.txt", "w") as my_file:
	my_file.write('Number of unknown users\' topics : {} out of {} topics'.format(number, last - first))
	my_file.write('Percentage: {}'.format(number/(first - last)))
#Done and dusted
