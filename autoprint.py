from operator import truediv
import random
import os
import shutil
def double():
    number=random.randint(0,20)
    result=True
    while(result):
        filename="file"+str(number)+".txt"
        shutil.copyfile("file.txt",(filename))
        result=False
    return filename
def main():
    while(True):
        name=double()
main()