import os 

def DirectoryCopy(DirSrc, DirDest):
    
    if(os.path.exists(DirSrc) and os.path.isdir(DirSrc)):

        os.mkdir(DirDest)
        src_path = ""
        dest_path = ""

        for folder, subfolder, filename in os.walk(DirSrc):
            FileList = filename

        for file in FileList:
            src_path = os.path.join(DirSrc, file)
            dest_path = os.path.join(DirDest, file)

            fobj1 = open(src_path, "r")
            fobj2 = open(dest_path, "w")

            Buffer = fobj1.read()

            fobj2.write(Buffer)

            fobj1.close
            fobj2.close