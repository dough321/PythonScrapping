from lxml import html
import requests

desitvbox ='http://www.desiserials.tv/bigg-boss-season-10-25th-january-2017-watch-online-episode-hd/179490/'
#parts = 0  # NO NEED FOR THIS FIGURING OUT PARTS VIA XPATH
#Totalparts = parts
xpath1 ='//div[@class="post-content bottom"]//p[6]/a' # If make it //div[@class="post-content bottom"]//p[6]/a[1] then i will need to use parts value removing 1 get all a tags in Daily <p> tag
xpath2 ='//table//iframe'
trimmed = desitvbox[:-8]  # removed last '/179309/' from this http://www.desiserials.tv/bigg-boss-season-10-24th-january-2017-watch-online-episode-hd/179309/
pgName = trimmed[trimmed.rfind('/',0,-1)+1:-20]
fileName = pgName[:9]
pgName = pgName[17:-13]  # We can comment this line. if we want long progName

page = requests.get(desitvbox)
tree = html.fromstring(page.content)
allHrefLink = []


for element in tree.xpath(xpath1):
		#allLinks will have all the links from the page
	allHrefLink.append(element.items()[0][1])
parts = len(allHrefLink)
Totalparts = parts
#print(allHrefLink)

id = allHrefLink[0]

linkwithoutid = id[:id.find('=')+1]

newID = id[id.find('=')+1:]
#print(newID)

num = int(newID)

add = num + (parts - 1)

print ('DailyMotion URL IDs ' + str(add) + ' ' + str(num))

finallinks = []
for p in range(add,num -1,-1):
	r = requests.get(linkwithoutid + str(p))
	t = html.fromstring(r.content)

	for element in t.xpath(xpath2):
		href = element.items()[3][1]
		#print(href)
		if href.find('dailymotion')>1:
			finallinks.append(href[href.rfind('/') + 1:])
#print('These are dailyvideokeys finallinks' + str(finallinks))
plexLnks = ''
for l in finallinks:
    plexLnks += 'http://www.dailymotion.com/video/' + l + ' '+ pgName +' P'+ str(Totalparts) +'\n'
    Totalparts = Totalparts -1

print(plexLnks)

'''
outfile = open('c:/Project/' + fileName + '.txt',"w")
outfile.write(plexLnks)
outfile.close()
'''