
import argparse
# from . import simplify_arg, build_arg

from . import simplify_arg




## *to do: add gt base as numeric vs IUPAC, 
    # control sample names (prefix, suffix, match)?? 
    # add INFO:tag in table output file 
    # write unit test
    # application optimization (for loop optimization)
    # cythonize etc. 


# to format the help message 
class BlankLinesHelpFormatter (argparse.RawTextHelpFormatter):
    def _split_lines(self, text, width):
        return super()._split_lines(text, width) + ['']



def view_argparser(subparsers):

    """Step 01 - Parser A: Sub parser to view and extract metadata information from the VCF file. """
    parser_a = subparsers.add_parser(
        "ViewVCF", help = "  View and extract metadata from the VCF.", 
        formatter_class = BlankLinesHelpFormatter
    )

    # available parameters 
    #** if possible add more in the future 
    metadata_keys = [
        "VCFspec",
        "reference",
        "contig",
        "samples",
        "INFO",
        "FORMAT",
        "FILTER",
        "GATKCommandLine",
        "GVCFBlock",
    ]

    # available output data types 
    data_types = ["json"]

    # add argument keys within "ViewVCF"
    parser_a.add_argument("-inVCF", required=False, help="Sorted vcf file.")
    
    parser_a.add_argument("-MultiThread", required=True, help="MultiThread.")
    
    parser_a.add_argument(
        "-outFile",
        required = False,
        help = "Name of the output file without file extension.",
    )
    parser_a.add_argument(
        "-outType",
        required = False,
        choices = data_types,
        nargs = "+",
        help = "Space separated list of output data types.\n" 
        "Multiple types can be requested.",
    )
    parser_a.add_argument(
        "-metadata",
        required=False,
        nargs="+",
        help="Space separated list of metadata of interest." + "\n"
        + "Allowed values are: " + "\n"
        + "  " + ", ".join(metadata_keys) + ".\n" 
        + "Multiple choices can be requested.",
        metavar=None,
    )


def simplify_argparser(subparsers):

    """Step 01 - Parser B: Sub parser to extract record information from the VCF file. """
    parser_b = subparsers.add_parser(
        "SimplifyVCF", help="  Simplify VCF -> to jason data.", 
        formatter_class=BlankLinesHelpFormatter
    )

    # add argument keys within SimplifyVCF
    parser_b.add_argument(
        "-toType",
        help="Type of the output file.",
        nargs=1,
        choices=["jason"],
        required=True,
    )
    parser_b.add_argument("-inVCF", help="Sorted vcf file.", required=False)
    parser_b.add_argument("-MultiThread", help="MultiThread", required=True)
    parser_b.add_argument("-outFile", help="Name of the output file.", required=True)
    parser_b.add_argument(
            "-outHeaderName", 
            help = "Write the VCF raw METADATA HEADER to a separate output file.\n" 
            "Default: no output.", 
            required=False)
    
    """Part A (02) : sub arguments for - From VCF to Table"""
    vcf_to_table = parser_b.add_argument_group(
            title = 'Additional arguments for "VCF To -> Table"')
    
    # now, pass the parser to respective function that collects arguments .. 
    # .. for each group     
   
    simplify_arg.parse_vcf_to_table(vcf_to_table)
    


    
    
    
    
    