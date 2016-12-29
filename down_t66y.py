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


###### global variables start ######
g_base_dir=u"Down/"
g_temp_image_num=0
g_current_dir = ""
g_image_type= ["&jpg"]
g_total_image_count = 0
g_downloaded = 0
g_downloaded_percentage = 0
g_thread_lock = Lock()
g_max_thread_count = 12
###### global variables end  ######

###### functions start ######
def verify_image(image_name):
    v_image = Image.open(image_name)
    if not v_image.verify():
        return True
    else:
        return False
        
if os.path.exists(g_base_dir):
    if os.name == 'nt':
        # os.removedirs(g_current_dir)
        shutil.rmtree(g_base_dir)
    else:
        pass
else:
    os.mkdir(g_base_dir)
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
print sys.argv[1]

def fetch_url(url):
    global g_downloaded
    global g_downloaded_percentage
    (return_code, name) = check_if_to_downloas(url)
    if return_code == 0:
        try:
            myopener = MyOpener()
            print "downloading",url
            myopener.retrieve(url,name)
            g_downloaded = g_downloaded+1
            g_downloaded_percentage = (g_downloaded*100/g_total_image_count)
            print "%s%%  g_downloaded  %s/%s" % (g_downloaded_percentage, g_downloaded, g_total_image_count)
        except Exception, e:
            print "myopener EORROR name:" + name +" ERROR_CODE:"+":"+unicode(e) 
    else:
        pass
    # print "'%s\' fetched in %ss" % (url, (time.time() - start))

def threading_download(image_list):
    global g_temp_image_num
    threads = [Thread(target=fetch_url, args=(url,)) for url in image_list]
    for thread in threads:
        # thread.daemon = True
        thread.start()
    for thread in threads:
        thread.join()
    # while threading.active_count() > 0:
        # time.sleep(0.1)
		
		
def threading_download2(image_list):	
	while True:	
		count = threading.activeCount()
		if count < g_max_thread_count:
			if temp_count < len(image_list):
				threads = threading.Thread(target=target, args=(image_list[temp_count],))
				threads.start()
				print "active thread count  == " + str(count)
			if temp_count  == len(image_list):
				temp_count = 0
				#break


def check_if_to_downloas(image):
    global g_temp_image_num
    global g_downloaded
    global g_current_dir
    g_thread_lock.acquire()
    # g_temp_image_num += 1
    i = g_temp_image_num
    g_thread_lock.release()
    ext = str(image[-4:])
    if ext in g_image_type:
        pass
    else:
        g_image_type.append(ext)
    ext= str(get_ext(image)) ## get image type
    if str(ext) == ".php" or str(image[-4:]) =="&jpg":
        ext=".jpg"
    name= g_current_dir + "/"+ str(i) +ext
    # print "downloading",image
    if os.path.exists(name):
        if  verify_image(name): # image ok
            print "###############verified"
            g_downloaded = g_downloaded+1
            return -1, ""
        else:
            os.remove(name)
            return 0, name
    else:
        g_temp_image_num += 1
        return 0, name
      
with jsonlines.open(sys.argv[1]+'.jsonlines') as reader:
    for obj in reader:
        image_list = obj["t_image_list"] # get image list
        if image_list: # if image list not NULL
            for image in image_list:
                g_total_image_count=g_total_image_count+1
		
def main():
    global g_image_type
    global g_current_dir
    global g_temp_image_num
    with jsonlines.open(sys.argv[1]+'.jsonlines') as reader:
        for obj in reader:
            g_current_dir=g_base_dir+ u''.join(e for e in obj["t_title"] if e.isalnum())  # remove special character for the name and path
            # print g_current_dir
            if g_current_dir.endswith("poweredbyphpwindnet"):  # remove php title
                g_current_dir=g_current_dir[:-19]
                if len(g_current_dir) > 100:
                    g_current_dir=g_current_dir[:100]
            print g_current_dir
            if os.path.exists(g_current_dir): # if dir not exist, make it
                if os.name=='nt':
                    shutil.rmtree(g_current_dir)
            else:
                os.mkdir(g_current_dir)
            image_list = obj["t_image_list"] # get image list
            
            if image_list: # if image list not NULL
                g_temp_image_num = 0
                threading_download(image_list)
            else:
                pass
            g_current_dir = ""
    print g_image_type
###### functions end ######	

if __name__ == "__main__":
    main()


