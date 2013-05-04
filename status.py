#!/usr/bin/env python
import urllib2
import re
import sys

# this tool is coded by Yasoob
# just enjoy using it

try:
    print "####################################################################################################################################"
    print "###########################--[Down for me?]----::(Website status checker by Yasoob)::----[Down for me?]--###########################"
    print "####################################################################################################################################"
    headers=[{'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}]
    url = "http://www.isup.me/"
    web = raw_input("[Down for me?]  what is the url of website? \n[Down for me?]  ")
    if "http://www." in web:
        web = web.split(".")[1]+".com"
    elif "www." in web:
        web = web.split(".")[1]+".com"
    else:
        web = web
    print "[Down for me?]  opening webpage"
    request = urllib2.urlopen(url+web)
    request.addheaders = headers
    html = request.read()
    print html
    
    b = re.search(r"It's just you",html)
    c = re.search(r"It's not just you!",html)
    try:
        if b.group():
            print "[Down for me?]  it's just you"
        elif c.group():
            print "[Down for me?]  It's down"
    except AttributeError:
           print "[Down for me?]  Invalid url"
except KeyboardInterrupt:
    print "\n[Down for me?]  program was quited by the user."
    sys.exit()
finally:
    print "[Down for me?]  Goodbye"
    sys.exit()
    
    
    
