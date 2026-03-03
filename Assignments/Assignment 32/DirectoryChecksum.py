import os
import hashlib

def DirectoryChecksum(DirName):

    path = ""

    if(os.path.exists(DirName)):

        for foldername, subfolder, filename in os.walk(DirName):

            for file in filename:

                path = os.path.join(foldername, file)
                hobj = hashlib.md5()

                fobj = open(path, "rb")

                while True:
                    data = fobj.read(1024)

                    if not data:
                        break
                    else:
                        hobj.update(data)

                print(f"Checksum for {file} is {hobj.hexdigest()}")

                fobj.close()
                path = ""