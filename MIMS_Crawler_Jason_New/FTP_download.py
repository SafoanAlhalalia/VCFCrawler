import ftplib

import re

import os

import gzip

import shutil

def gz_extract(directory):
    
    extension = ".gz"
    
    os.chdir(directory)
    
    for item in os.listdir(directory): # loop through items in dir
        
        if item.endswith(extension): # check for ".gz" extension
          
            gz_name = os.path.abspath(item) # get full path of files
          
            file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] #get file name for file within
            
            print("gz_name",gz_name)
            
            print("file_name",file_name)
          
            with gzip.open(gz_name,"rb") as f_in, open(file_name,"wb") as f_out:
              
                shutil.copyfileobj(f_in, f_out)
              
            os.remove(gz_name) # delete zipped file
            
    return directory+'/'+file_name

class NCBI_CLINVAR:
    
    def __init__(self,site_address,input_file__name="none"):
        
        self.site_address = site_address
        
        self.Crawler(site_address)

    def Crawler(self,site_address):
    
        with ftplib.FTP(site_address) as ftp:
            
            ftp.login("anonymous", "email@email.com")
            
#             print(ftp.getwelcome())   # print welcome message from the site
            
            ftp.cwd("pub/clinvar/vcf_GRCh38/weekly")  # change the current directory to "pub/clinvar/vcf_GRCh38/weekly"
            
            print("Current Directory",ftp.pwd()) # print out the current directory using pwd
            
            savedir = "C:/MIMS"    # name of the directory in which the file will be installed
            
            os.chdir(savedir)       # change the directory to the directory you want to install the file in
            
            filesneed = [filename for filename in ftp.nlst() if re.search("vcf.gz$",filename) != None]
             
            print(filesneed[-3])
            
            download = filesneed[-3]
    
            ftp.retrbinary('RETR ' + download, open(download,'wb').write)
            
        directory = savedir
        
        
        
        self.input_file__name = gz_extract(directory)
            
       
            

    