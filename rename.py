import os
import time

# path = os.getcwd()
path = '/home/wuxiang/syno_share/download'
filenames = os.listdir(path)
#
# for filename in filenames:
#     print filename
#     print str(filename[-4:])
#     if str(filename[-4:]) == ".php":
#         os.rename(filename,filename[:-4]+".jpg")
#         print("test############")
#
#     else:
#         pass
# import os
# for root, dirs, files in os.walk(path):
#     for file in files:
#         if file.endswith("poweredbyphpwindnet"):
#             abs_name=os.path.join(root, file)
#             print(os.path.join(root, file))
#             # os.rename(abs_name,abs_name[:-4]+".jpg")
#             os.rename(abs_name,abs_name[:-19])


# remove the download before the file name: eg downloadxxx.jpgc-> xxxx.jpg
for file in filenames:
    print(file)
    test = file[0:7]
    print(id(test))
    if str(file[0:7]) == 'download':
        print(file[7:])
        os.rename(os.path.join(path, file), os.path.join(path, str(file[7:])))
