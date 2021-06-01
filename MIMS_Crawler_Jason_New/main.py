
import sys
import argparse


from assign_task import sub_argparsers
from assign_task.perform_operation import vcf_solver

from multiprocessing import freeze_support

import FTP_download



""" Purpose of the program: mine the data from the VCF files and convert it into Json file.
The output file consists of 
state may be extracted as well."""


def main():

    # define argument variables
    main_parser = argparse.ArgumentParser(
            prog="VCF-Simplify", formatter_class=argparse.RawTextHelpFormatter)
    
    # Create sub_parsers (for SimplifyVCF)
    subparsers = main_parser.add_subparsers(help="Choose one of the following method.")
    
    sub_argparsers.simplify_argparser(subparsers)

    # creating an argument variable to handle the loaded argument
    args = main_parser.parse_args()

    """ Step 02: Based on positional arugments and task go to specific function """   

    task = sys.argv[1]
    
    print(f'Number of Threads is {args.MultiThread}')
    
    vcf_solver(task, args)
   
if __name__ == "__main__":
    
    freeze_support()   # required to use multiprocessing
    
    site_address = "ftp.ncbi.nlm.nih.gov"
    
    MIMS = FTP_download.NCBI_CLINVAR(site_address)
    
    print("File has been downloaded")
    
    main()