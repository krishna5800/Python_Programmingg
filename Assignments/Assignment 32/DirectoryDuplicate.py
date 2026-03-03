import os
import hashlib

def DirectoryDuplicate(DirName):

    path = ""
    duplicate = {}

    if(os.path.exists(DirName)):

        lobj = open("Krishna.log", "w")

        for foldername, subfolder, filename in os.walk(DirName):

            for file in filename:

                path = os.path.join(foldername, file)
                hobj = hashlib.md5()

                fobj = open(path, "rb")

                try:
                    while True:
                        data = fobj.read(1024)

                        if not data:
                            break
                        else:
                            hobj.update(data)

                    checksum = hobj.hexdigest()

                    if checksum in duplicate:
                        duplicate[checksum].append(path)
                    else:
                        duplicate[checksum] = [path]

                except Exception as e:
                    print("Can't execute")

                for checksum, file in duplicate.items():

                    if len(file) > 1:
                        lobj.write(str(file))

                fobj.close()
                path = ""