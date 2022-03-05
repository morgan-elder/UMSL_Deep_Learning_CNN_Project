import tarfile
import os.path
from os import listdir
from os.path import isfile, join

from numpy import source


source_dir = "../images"
output_dir = "../images"
img_files = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]


for i in range(12):
    start = 100 * i
    stop = 100 * i + 100
    output_filename = f"{output_dir}/images_{start+1}_{stop}.tar.gz"

    with tarfile.open(output_filename, "w:gz") as tar:
        for img in img_files[start:stop]:
            tar.add(f"{source_dir}/{img}", arcname=img)
        tar.close()
