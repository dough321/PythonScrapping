from lxml import html
import requests

desitvbox ='http://www.desitvbox.net/bigg-boss-season-10-26th-january-2017-episode-watch-online/'
#'http://www.desitvbox.net/yaaron-ki-baarat-20th-november-2016-episode-watch-online/'
#'http://www.desitvbox.me/the-kapil-sharma-show-9th-october-2016-episode-watch-online/'
#parts = 3
#Totalparts = parts
pgName = desitvbox[desitvbox.rfind('/',0,-1)+1:-15]
fileName = pgName[:10]
pgName = pgName[15:-13]  # We can comment this line. if we want long progName
page = requests.get(desitvbox)
tree = html.fromstring(page.content)
allHrefLink = []
hrefLink = tree.xpath('//div[@class="entry_content"]/div/p[5]/a') # Dailymotion Link Starts 5th P tag on DesiTv page ('//div[@class="entry_content"]/div/p[5]/a[1]')
for el in hrefLink:
	allHrefLink.append(el.items()[0][1])
#print(allHrefLink)
parts = len(allHrefLink)
Totalparts = parts
id = allHrefLink[0]

linkwithoutid = id[:id.find('=')+1]

newID = id[id.find('=')+1:]
#print(newID)

num = int(newID)

add = num + (parts - 1)

print ('DailyMotion URL IDs ' + str(add) + ' ' + str(num))
finallinks = []
for p in range(add,num -1,-1):
	#print(linkwithoutid + str(p))
	r = requests.get(linkwithoutid + str(p))
	t = html.fromstring(r.content)
	for element in t.xpath("//iframe"):
		href = element.items()[3][1]
		if href.startswith('http'):
			finallinks.append(href[href.find('=')+1:])
#print('These are dailyvideokeys finallinks' + str(finallinks))
plexLnks = ''
for l in finallinks:
    #result = l[start:]
    plexLnks += 'http://www.dailymotion.com/video/' + l + ' '+ pgName +' P'+ str(Totalparts) +'\n'
    Totalparts = Totalparts -1

print(plexLnks)
'''
outfile = open('c:/Project/' + fileName + '.txt',"w")
outfile.write(plexLnks)
outfile.close()
'''