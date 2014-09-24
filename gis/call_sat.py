##This function, call() takes path of parameter file,output file and absolute path
##of SaTScan software.It then calls SaTScanBatch.exe to start the analysis.

##Import required files
import os
import subprocess

def call(file_path_prm,out_file,sat_path):
    path=file_path_prm
    path=path.split('/')
    file_name_prm=path.pop()
    path='/'.join(path)
    arg1=path+'/'+file_name_prm
##Call SaTScan for analysis	
    subprocess.call([sat_path,arg1,'-o',out_file])

