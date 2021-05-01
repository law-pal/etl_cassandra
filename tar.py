import tarfile

# extracts tar file
tar = tarfile.open("workspace_archive.tar")
tar.extractall()
tar.close()