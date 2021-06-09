1. Design decisions: 
	A. Use argparse to Read the arguments from namespace. 
	B. Design an algorithm based Object Oriented to download and unzip the recent .vcf file from FTP server. 
	C. Design an algorithm based Object Oriented to extract the requested data from the downloaded .vcf file and save in .json file. 
	D. Each list (line) in the .vcf file is processed using one thread.

2. Shortcoming: 
	I designed the algorithm extracting the data from .vcf file in a way that each line is processed by one thread. It can be modified easily so the user can decide 	the number of threads.

3. Possible improvements:

	We may use PySpark in combination with our current algorithm for possible performance enhancement.
	Using Multiprocessing instead of Multi-threading for possible performance enhancement.

4. Use the following command to download and extract the .json file:

Python3 main.py SimplifyVCF  -MultiThread 4 -SaveDirectory C:/MIMS -toType jason   -infos AF_ESP AF_EXAC AF_TGP ALLELEID RS -preHeader CHROM POS ID REF ALT

5. Now we will explain the arguments, each argument can be explained as follows:

	-MultiThread: number of threads
	
	-SaveDirectory: where you want to save the downloaded and the extracted files
	
	-toType: type of the output file
	
	-infos: data need to be extracted from info 
	
	-preHeader: data need to be extracted from other columns
	
6. I used Eclipse IDE with git to develop this project.

7. I usually use EC2, Lambda, Sagemaker to run it for project instead docker.
