
import sys

from records_parser.simplifyvcf.to_table import fnc_vcf_to_table



def vcf_solver(task, args):
    
    print("Using the following arguments: ")
    print(args)
    print()    
    
    try:
        print('Using option "%s"' % task)
    except IndexError:
        print(
            "Provide only one of the following positional arguments: SimplifyVCF, BuildVCF or ViewVCF"
        )
        print("Exiting the program")
        print()
        sys.exit()

    ## Starting SimiplyVCF
    if task == "SimplifyVCF":
        
        print("  Simplifying the VCF records ...")
    
        infile = args.inVCF

        preheader = args.preHeader
        samples = args.samples
        infos = args.infos
        fnc_vcf_to_table(infile,  preheader,  infos,  samples)

    else:
        print(
            "Provide one of the positional arguments: SimplifyVC "
        )

        print("Exiting the program")
        print()
        sys.exit()