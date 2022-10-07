
import os

folder = r"C:\Users\mcastro\Documents\MCastro\2_Codigo\GANs_derma\Data\ham10000\1"

im_size = 256

"""
relative_path = os.getcwd(); tail = ""; name = ""
while tail != "Data":
    head, tail = os.path.split(folder)
    name = tail + "-" + name; folder = head
"""

"""
tail = ""; name = ""; folder = folder
while tail != "Data":
    head, tail = os.path.split(folder)
    if tail != "Data": name = tail + "-" + name
    folder = head

relative_path = os.path.join(os.getcwd(),"Data", name + "-npy-" + str(im_size))
"""

tail = ""; name = ""; folder = folder
while tail != "Data":
    head, tail = os.path.split(folder)
    if tail != "Data": name = tail + "-" + name
    folder = head
relative_path = os.path.join(os.getcwd(),"Data",name + "-npy-" + str(im_size))
os.mkdir(relative_path)
print(relative_path)

