import os 
import hashlib

def DirectoryDuplicateRemoval(DirName):
    duplicate = {}

    if os.path.exists(DirName):
        # Phase 1: Scan and Checksum
        for foldername, subfolder, filename in os.walk(DirName):
            for file in filename:
                path = os.path.join(foldername, file)
                
                try:
                    hobj = hashlib.md5()
                    # Open the file
                    fobj = open(path, "rb")
                    
                    while True:
                        data = fobj.read(1024)
                        if not data:
                            break
                        hobj.update(data)
                    
                    # IMPORTANT: Close the file immediately after reading
                    # This unlocks the file so Windows can delete it later
                    fobj.close()

                    checksum = hobj.hexdigest()
                    if checksum in duplicate:
                        duplicate[checksum].append(path)
                    else:
                        duplicate[checksum] = [path]

                except Exception as e:
                    print(f"Could not process {path}: {e}")

        # Phase 2: Logging and Deletion
        with open("Krishna1.log", "w") as lobj:
            for checksum, file_list in duplicate.items():
                if len(file_list) > 1:
                    # Keep the first file (file_list[0]), delete the rest
                    for path_to_delete in file_list[1:]:
                        try:
                            os.remove(path_to_delete)
                            lobj.write(f"Deleted: {path_to_delete}\n")
                            print(f"Removed: {path_to_delete}")
                        except Exception as e:
                            print(f"Error deleting {path_to_delete}: {e}")
    else:
        print("Invalid Directory Path")

# To run the script:
# DirectoryDuplicateRemoval("Demo")
