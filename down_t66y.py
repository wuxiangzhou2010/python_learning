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
import threading
from threading import Thread, Lock

from PIL import Image
import re

pattern = re.compile(r'fuskator') # some url seems blocked

base_dir=u"Down/"
temp_i=0
dir_name = ""
image_type= ["&jpg"]
total = 0
downloaded = 0
percent = 0
mutex = Lock()
max_thread_count = 0


def verify_image(image_name):
    v_image = Image.open(image_name)
    if v_image.verify():
        print "image is ok"
        return True
    else:
        print "image is wrong"
        return False
        

def make_del_dir():
    if os.path.exists(base_dir):
        if os.name == 'nt':
            # os.removedirs(dir_name)
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

# myopener = MyOpener()
# myopener.retrieve('https://www.google.com/search?q=test', 'useragent.html')

def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'

def fetch_url(url, name):
    global downloaded
    global percent
    try:
        myopener = MyOpener()
        print "downloading",url
        myopener.retrieve(url,name)
        downloaded = downloaded+1
        percent = (downloaded*100/total)
        print "%s%%  downloaded  %s/%s" % (percent, downloaded, total)
    except Exception, e:
        print "myopener EORROR name:" + name +" ERROR_CODE:"+":"+unicode(e) 

def threading_download(image_list):
    global temp_i
    threads = [Thread(target=fetch_url, args=(url,)) for url in image_list]
    for thread in threads:
        # thread.daemon = True
        thread.start()
    for thread in threads:
        thread.join()
    # while threading.active_count() > 0:
        # time.sleep(0.1)

def threading_download2(image_list):	
    global temp_i
    global pattern
    length = len(image_list)
    while temp_i < length:	
        image = image_list[temp_i]
        #global name
        (return_code, name) = check_if_to_downloas(image)
        count = threading.activeCount()
        if return_code:
            while threading.activeCount() >5:
                pass
            print "temp_i = " +str(temp_i), "len = " +str(length)
            if pattern.search(image):
                temp_i += 1
            else:
                threads = threading.Thread(target=fetch_url, args=(image,name))
                threads.start()
            print "active thread count  = " + str(count)
        else:
            pass
        mutex.acquire()
        temp_i += 1
        mutex.release()
        
def check_if_to_downloas(image):
    global temp_i
    global downloaded
    global dir_name
    global image_type
    i = temp_i
    ext = str(image[-4:])
    if ext in image_type:
        pass
    else:
        image_type.append(ext)
    ext= str(get_ext(image)) ## get image type
    if str(ext) == ".php" or str(image[-4:]) =="&jpg":
        ext=".jpg"
    name= dir_name + "/"+ str(i) +ext
    # print "downloading",image
    if os.path.exists(name):
        if  verify_image(name): # image ok
            print "###############verified"
            downloaded = downloaded+1
            return 1, ""
        else:
            os.remove(name)
            return 0, name
    else:
        #temp_i += 1
        return -1, name
      
with jsonlines.open(sys.argv[1]+'.jsonlines') as reader:
    for obj in reader:
        image_list = obj["t_image_list"] # get image list
        if image_list: # if image list not NULL
            for image in image_list:
                total=total+1


def main():
    global image_type
    global dir_name
    global temp_i
    global max_thread_count
    
    make_del_dir()
    max_thread_count = sys.argv[2]
    print "max_thread_count = " + str(max_thread_count)
    with jsonlines.open(sys.argv[1]+'.jsonlines') as reader:
        for obj in reader:
            dir_name=base_dir+ u''.join(e for e in obj["t_title"] if e.isalnum())  # remove special character for the name and path
            # print dir_name
            if dir_name.endswith("poweredbyphpwindnet"):  # remove php title
                dir_name=dir_name[:-19]
                if len(dir_name) > 100:
                    dir_name=dir_name[:100]
            print dir_name
            if os.path.exists(dir_name): # if dir not exist, make it
                if os.name=='nt':
                    shutil.rmtree(dir_name)
            else:
                os.mkdir(dir_name)
            image_list = obj["t_image_list"] # get image list
            
            if image_list: # if image list not NULL
                temp_i = 0
                threading_download2(image_list)
            else:
                pass
            dir_name = ""
    print image_type

if __name__ == "__main__":
    main()


