import sys

import urllib2
from myapp.models import *
from django.utils import timezone
from bs4 import BeautifulSoup
url='http://www.sarkariyojna.co.in/central-government/pm-yojana/'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page,"html.parser")
Tlist=soup.find_all('h4',class_='article-title')
Dlist=soup.find_all('div',class_='entry')
for x in range(len(Tlist)):
    D=data(type='schemes', area='both', title=unicode(Tlist[x]).encode('utf8'), description=unicode(Dlist[x].p).encode('utf8'),date=timezone.now().date(),state='all',district='all',for_whom='all')
    D.save()

