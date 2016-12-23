import os
import time

path = os.getcwd()
# filenames = os.listdir(path)

# for filename in filenames:
    # print filename
    # print str(filename[-4:])
    # if str(filename[-4:]) == ".php":
        # os.rename(filename,filename[:-4]+".jpg")
        # print("wuxiang############")
       
    # else:
        # pass
import os
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith("poweredbyphpwindnet"):
            abs_name=os.path.join(root, file)
            print(os.path.join(root, file))
            # os.rename(abs_name,abs_name[:-4]+".jpg")
            os.rename(abs_name,abs_name[:-19])