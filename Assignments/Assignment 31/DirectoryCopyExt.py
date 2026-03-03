import os
import shutil

def DirectoryCopyExt(DirSrc, DirDest, Extension):
    
    if(os.path.exists(DirSrc) and os.path.isdir(DirSrc)):
        os.mkdir(DirDest)

        for folder, subfolder, filename in os.walk(DirSrc):

            for file in filename:

                base, extension = os.path.splitext(file)

                if extension == f".{Extension}":
                    src_path = os.path.join(DirSrc, file)
                    dest_path = os.path.join(DirDest, file)

                    shutil.copy2(src_path, dest_path)
                    print(f"Copied: {file}")