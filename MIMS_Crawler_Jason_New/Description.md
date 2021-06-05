Design decisions: 
A. Use argparse to Read the arguments from namespace. 
B. Design an algorithm based Object Oriented to download and unzip the recent .vcf file from FTP server. 
C. Design an algorithm based Object Oriented to extract the requested data from the downloaded .vcf file and save in .json file. 
D. Each list (line) in the .vcf file is processed using one thread.

Shortcoming: 
I designed the algorithm extracting the data from .vcf file in a way that each line is processed by one thread. It can be modified easily so the user can decide the number of threads.

Possible improvements:

We may use PySpark in combination with our current algorithm for possible performance enhancement.
Using Multiprocessing instead of Multi-threading for possible performance enhancement.