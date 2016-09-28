#import urllib2
#from bs4 import BeautifulSoup 


#where are we scraping our midi files from
base='http://www.free-midi.org/midi/a'

urls = ['http://www.free-midi.org/midi/a/']

## Save directory
location="files/"
midi_urls=[]   
from bs4 import BeautifulSoup
import urllib2
import itertools
import urllib


for _ in itertools.repeat(None, 10):
    new_urls=[]
    for url in urls:
        data = urllib2.urlopen(url).read()   
        page = BeautifulSoup(data,'html.parser')
        for link in page.findAll('a'):
            l = link.get('href')
            if l:
                if l[-3:]=='mid':
                        midi_urls.append(l)
                        try:
                            urllib.urlretrieve(l, location+l.split('/')[-1])
                        except:
                            print(l, " has failed")

                elif l[0]=='/':
                        l=base+l
                
            new_urls.append(l)
    urls=new_urls  