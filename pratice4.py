import os
from root import ROOT


listdir_cwd = os.listdir(os.getcwd())
listdir_root = os.listdir(ROOT)

print(listdir_cwd == listdir_root)
