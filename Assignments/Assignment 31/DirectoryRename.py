import os

def DirectoryRename(DirName, Extension1, Extension2):

    if os.path.exists(DirName) and os.path.isdir(DirName):

        for FolderName, SubFolderName, FileName in os.walk(DirName):

            for file in FileName:

                base, extension = os.path.splitext(file)

                if extension == f".{Extension1}":

                    old_path = os.path.join(FolderName, file)
                    
                    new_path = os.path.join(FolderName, f"{base}.{Extension2}")

                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} -> {new_path}")