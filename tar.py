import tarfile
tar = tarfile.open("workspace_archive.tar")
tar.extractall()
tar.close()