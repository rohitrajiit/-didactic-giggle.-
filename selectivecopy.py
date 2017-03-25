#! python3
# selectivecopy.py - Copies an entire folder and its contents into
import os, shutil, sys
print('Enter Source Directory')
Source = input()
print('Enter Destination Directory')
Destination = input()
print('Enter file extension to copy')
pattern = input()

if os.path.isdir(Source) == False:
 print('Error: Source is not a Directory')
 sys.exit()

if os.path.isdir(Destination) == False:
 os.makedirs(Destination)

for foldername, subfolders, filenames in os.walk(Source):
 for filename in filenames:
  if pattern in filename:
   shutil.copy(os.path.join(foldername,filename), Destination)




