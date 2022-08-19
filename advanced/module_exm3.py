from ctypes import addressof
import os

print("C Drive folder")
print(os.getcwd())
print(os.listdir())

print("C Drive content")
os.chdir('C:\\Program Files')
print(os.getcwd())
print(os.listdir())

address = r'C:\Program Files\Python.exe'
if os.path.exists(address):
    print('Files exists')
else:
    print ('Files does not exist')