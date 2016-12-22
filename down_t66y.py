import jsonlines
import os
import time
import urllib
from urlparse import urlparse
from os.path import splitext
import shutil
import wget
from urllib import FancyURLopener
import sys
base_dir=u"Down/"
if os.path.exists(base_dir):
    if os.name == 'nt':
        os.removedirs(dir_name)
        shutil.rmtree(base_dir)
    else:
        pass
else:
    os.mkdir(base_dir)
# data = []
# with open('C:\Users\\xihaj\PycharmProjects\\test\DaGaiErDeQiZhi.jsonlines') as f:
#     for line in f:
#         data.append(json.loads(line))
# print data


class MyOpener(FancyURLopener, object):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

myopener = MyOpener()
# myopener.retrieve('https://www.google.com/search?q=test', 'useragent.html')

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'
print sys.argv[1]
with jsonlines.open(sys.argv[1]+'.jsonlines') as reader:
    for obj in reader:
        # print obj
        dir_name=base_dir+ u''.join(e for e in obj["t_title"] if e.isalnum())  # remove special character for the name and path
        print dir_name
        if dir_name.endswith("poweredbyphpwindnet"):  # remove php title
            dir_name=dir_name[:-19]
            if len(dir_name) > 100:
                dir_name=dir_name[:100]
                print dir_name
                time.sleep(10)
        if os.path.exists(dir_name): # if dir not exist, make it
            if os.name=='nt':
                # os.removedirs(dir_name)
                shutil.rmtree(dir_name)
        else:
            os.mkdir(dir_name)
        image_list = obj["t_image_list"] # get image list
        if image_list: # if image list not NULL
            i=0
            for image in image_list:
                #print image
                ext= get_ext(image) ## get image type
                # if str(ext) is ".php" or str(ext[-4:-1]) is "&jpg":
                if str(ext) == ".php" or str(ext).endswith("&jpg"):
                    ext=".jpg"
                    print ext + "wuxiang######"
                name= dir_name + "/"+ str(i) +ext
                # print name
                print "downloading",image
                # opener = urllib.FancyURLopener({}) 
                # opener.version = 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'
                # opener.retrieve(image, name)
                # opener.retrieve(image, name)
                if os.path.exists(name):
                    pass
                else:
                    try:
                        myopener.retrieve(image,name)
                    except Exception, e:
                        print "myopener EORROR" + dir_name + "/"+ str(i)+":"+unicode(e)
                    # urllib.urlcleanup()
                    print name
                # wget.download(image,name)
                # tt="wget "+ image +" " + dir_name+"/"+str(i)+get_ext(image)
                # print tt
                # os.system(name.strip())
                # print dir_name+"/"+str(i)+get_ext(image)
                # print name
                    i=i+1
                    #time.sleep(0.5)
        else:
            pass
        #for line in obj[u't_image_list']:

