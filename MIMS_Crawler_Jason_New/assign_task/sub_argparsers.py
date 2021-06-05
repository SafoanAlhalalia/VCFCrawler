
import argparse

from . import simplify_arg

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
        "INFO",
    ]

    # available output data types 
    data_types = ["json"]

    # add argument keys within "ViewVCF"
   
    parser_a.add_argument("-MultiThread", required=True, help="MultiThread.")
    
    parser_a.add_argument(
        "-outType",
        required = False,
        choices = data_types,
        nargs = "+",
        help = "Space separated list of output data types.\n" 
        "Multiple types can be requested.",
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
    parser_b.add_argument("-MultiThread", help="MultiThread", required=True)
    
    """Part A (02) : sub arguments for - From VCF to Table"""
    vcf_to_table = parser_b.add_argument_group(
            title = 'Additional arguments for "VCF To -> Table"')
    
    # now, pass the parser to respective function that collects arguments .. 
    # .. for each group     
   
    simplify_arg.parse_vcf_to_table(vcf_to_table)
    


    
    
    
    
    