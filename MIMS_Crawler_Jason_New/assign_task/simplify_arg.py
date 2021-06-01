


def parse_vcf_to_table(vcf_to_table):
    """ Argument for converting VCF file to a Table """ 
    sample_choices = [
        "0",
        "sample A",
        "sample B",
        "prefix:XXXsample",
        "suffix:sampleXXX",
        "match:XXX",
        "all",
    ]
    
    vcf_to_table.add_argument(
        "-samples",
        default="all",
        nargs="+",
        help="SAMPLE of interest:\n"
        "  Space separated name of the samples or matching sample names.\n"
        "Matching prefix, suffix or string in the names can be provided too.\n"
        "Choices format:\n [%s]" % (", ".join(sample_choices)) + "\n"
        "Multiple choices can be requested.\n"
        "Note: 0 = ignore all the samples; Default = all",
        metavar=None,
    )

    pre_header_keys = ["0", "CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "all"]
    vcf_to_table.add_argument(
        "-preHeader", type=str,
        default=["all"],
        nargs="+",
        help="Space separated header fields before the 'INFO' field.\n"
        "Choices:\n [%s]. " % (", ".join(pre_header_keys)) + "\n"
        "Multiple choices can be requested.\n"
        "Note: 0 = ignore all the pre-header-keys; Default = all.",
        metavar=None,
    )

    infos_tags = ["0", "AC", "AF", "AN", "...", "all"]
    vcf_to_table.add_argument(
        "-infos", type=str,
        nargs="+",
        default=["all"],
        help="Space separate INFO tags of interest.\n"
        "Choices :\n [%s]. " % (", ".join(infos_tags)) + "\n"
        "Multiple choices can be requested.\n"
        "Note: 0 = ignore all the INFO tags; Default = all",
        metavar=None,
    )

    format_tags = ["0", "GT", "PG", "PI", "...", "all"]
    vcf_to_table.add_argument(
        "-formats", type=str,
        nargs="+",
        default=["all"],
        help="Space separate FORMAT tags of interest.\n"
        "Choices : [%s]. " % (", ".join(format_tags)) + "\n"
        "Multiple choices can be requested.\n"
        "Note: 0 = ignore all the pre-header-keys; Default = all.",
        metavar=None,
    )    

    vcf_to_table.add_argument(
        "-mode", type=str,
        required=False,
        default='0',
        help="Structure of the output table. Default = wide (0)",
        choices=["wide", "long", '0', '1'],
    )

    