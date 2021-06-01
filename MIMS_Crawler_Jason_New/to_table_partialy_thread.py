import time
import sys
import itertools
import warnings

import threading

from multiprocessing import Process

import json

from metadata_parser.vcf_metadata_parser import VcfReadMetaData
from records_parser.vcf_records_parser import VcfReadIndividualRecord
from metadata_parser.utils import time_memory_track

def sleep_thread():
    thread_list = []

def Process_data_to_jason(record_keys,all_samples,my_infos,output_header,my_preheader,write_as_json,write_as_json1,records):
# for records in records_gen:
    
    chr_on_process = ""
    
    line_to_write = []  # create new emtpy variable

    mapped_record = VcfReadIndividualRecord(
        recordKeys=record_keys, inRecord=records, 
        sample_names=all_samples
    ).read_vcfRecord()
    

    """Now, this mapped records can be mined for extracting required data."""
    contig = mapped_record["CHROM"]

    # find which chr is in the process
    if chr_on_process != contig:
        print("Contig %s is being processed ... " % str(contig))
        print()
        chr_on_process = contig

    # Step 04-A : mine the values for 'pre header' of interest
    #line_to_write += [mapped_record.get(prex, '.') for prex in pre_header]
    line_to_write += [mapped_record[prex] for prex in my_preheader]
    #raise KeyError('key does not exist')                


    # Step 04-B: mine the values for the INFO tags of interest
    infos_to_write = process_info(my_infos, mapped_record)
    line_to_write += infos_to_write
    
    dict_to_write = {output_header[x]:line_to_write[x] for x in range(len(line_to_write))}
    
    dict_link_to_write = {"_from":dict_to_write["ID"], "_to":dict_to_write["INFO:RS"]}
    
    del dict_to_write["INFO:RS"]
    
    

    # Step 04-C: compute values for the FORMAT fields of interest for each SAMPLE names of interest
    # so, we need to use both format_fields and sample_names together
    # and pass it to a defined function
    
###################################################################################################
#   Safoan Add this for nodes.json
#########################################################################################3##########
    """Convert the dictionary to a json object and write to a file"""
    print("\twriting metadata as JSON")
#             json_obj_string = json.dumps(mapped_record)
    json_obj_string = json.dumps([dict_to_write])
    datastore = json.loads(json_obj_string)
    
#     print(dict_to_write)
    
#                 outFile = "testOutput"

#                 with open("%s.json" % outFile, "w", encoding="utf-8") as write_as_json:

    json.dump(datastore, write_as_json, ensure_ascii=False, indent=4)

#     try:
#         json.dump(datastore, write_as_json, ensure_ascii=False, indent=4)
#          
#     except:
#          
#         pass
################################################################################################

###################################################################################################
#   Safoan Add this for links.json
#########################################################################################3##########
    """Convert the dictionary to a json object and write to a file"""
    print("\twriting metadata as JSON")
#             json_obj_string = json.dumps(mapped_record)
    json_obj_string = json.dumps([dict_link_to_write])
    datastore1 = json.loads(json_obj_string)
    
    json.dump(datastore1, write_as_json1, ensure_ascii=False, indent=4)
    
#     try:
#         
#         json.dump(datastore1, write_as_json1, ensure_ascii=False, indent=4)
#          
#     except:
#          
#         pass
    
#     return datastore1
    
#     print(dict_link_to_write)
    
#                 outFile = "testOutput"

#                 wit open("h%s.json" % outFile, "w", encoding="utf-8") as write_as_json:
#     json.dump(datastore1, write_as_json1, ensure_ascii=False, indent=4)
################################################################################################

# partial_sum_four = functools.partial(Process_data_to_jason, a, b, c)

"""Step 03 (B) : Function for VCF To Table."""
# @time_memory_track
def fnc_vcf_to_table(input_vcf, out_filename, preheader,  infos,  samples):
    # extract metadata and raw header from the input VCF
    metadata, only_header, record_keys = VcfReadMetaData(input_vcf).read_metadata()

    all_info = [info["ID"] for info in metadata["INFO"]]
    all_samples = [x["name"] for x in metadata["samples"]]

#     all_preheader = record_keys[0:7]
    all_preheader = record_keys[0:5]
    
    all_preheader.append(record_keys[7])

    print("%i samples found" % len(all_samples))
    print()

    start_time01 = time.time()


    outFile1 = "nodes"
    
    outFile2 = "links"

        
    with open(input_vcf) as invcf, open("%s.json" % outFile1, "w", encoding="utf-8") as write_as_json, open("%s.json" % outFile2, "w", encoding="utf-8") as write_as_json1:

        # get field values according to arguments and all possible tags
        my_preheader = process_fields(preheader, all_preheader, argument_flag = '-preHeader')
        my_infos = process_fields(infos, all_info, argument_flag = '-infos')
        #print(my_samples)
        
        # ensure that sample names and format tags are in sync
#         check_sample_and_format(my_samples, my_formats)
        
        # create a list to store the column header of the output table file
        output_header = []

        # Step 03-A: now, write the appropriate front part of the header
        output_header += my_preheader

        # Step 03-B: add INFO tags of interest to the output header
        # also add INFO: prefix to info tags
        my_infos_column = ['INFO:' + x for x in my_infos] 
        output_header += my_infos_column

        ## Step 03-C: first add tags from the "FORMAT" of interest to the header
        # *Note: the format tags should however be combined with sample name
        # as SAMPLE:FORMAT tag
        chr_on_process = ""

        """ Step 04: now, start parsing the VCF file using cyVCF2 and add the data for each header fields"""
        print("Reading the input vcf file ... ")
        print()

        # skips line starting with '#'
        records_gen = itertools.dropwhile(lambda line: line.startswith("#"), invcf)
        
#         n_processors = args.MultiThread

        items = [record for record in records_gen]
        
        thread_list = []

        n_processors = 6
        
        for record in items:
        # Instantiates the thread
            threading._start_new_thread(Process_data_to_jason, ( record_keys,all_samples,my_infos,output_header,my_preheader,write_as_json,write_as_json1,record,))

            
#             json.dump(A, write_as_json, ensure_ascii=False, indent=4)
#         for record in items:
            
#             Process_data_to_jason(record_keys,all_samples,my_infos,output_header,my_preheader,write_as_json,write_as_json1,record)
        
#         Process(target=Process_data_to_jason, args=( record_keys,all_samples,my_infos,output_header,my_preheader,write_as_json,write_as_json1,items))
        
        
                      
            # write_block.write('\n')
    print("elapsed time: ", time.time() - start_time01)
    print("Completed converting the VCF file to table output.")


def process_fields(given_tags, all_fields, argument_flag):
    if isinstance(given_tags, str) and given_tags == 'all':
        return all_fields
    elif given_tags[0] == "all":
        return all_fields
    elif given_tags[0] == "0":
        return []
    elif isinstance(given_tags, str) and given_tags == "0":
        return []
    else:
        #print(f'given_tags: {given_tags}') 
        #print(f'all_tags: {all_fields}')        
        if all(elem in all_fields for elem in given_tags):
            return given_tags            
        else:
            non_matching_key = [x for x in given_tags if x not in all_fields]
            #print('non matching keys\n', non_matching_key, argument_flag)
            
            ## ?? Bhuwan - this warning needs further rendering 
            warnings.warn(
                    (f"\n    The provided {non_matching_key} for '{argument_flag}' is not present in VCF metadata.\n" 
                    "    Please make sure your vcf file is valid or your input {given_tags} is valid."), stacklevel=4  )
            
            if argument_flag == '-infos' or argument_flag == '-formats':
                print("    The %s for '%s' will be populated with '.' if not present in vcf records." 
                      % (non_matching_key, argument_flag))
                return given_tags
            
            ## only exit when for the following arugments 
            elif argument_flag == '-preHeader' or argument_flag == '-samples':
                print("remove or fix the %s tags from the argument '%s'" 
                      % (non_matching_key, argument_flag))
                sys.exit(0)
            

def process_info(info_fields, mapped_record):    
    """ map and write info """
    
    infos_to_write = [
        mapped_record["INFO"].get(inftags, ".") for inftags in info_fields
    ]
    return infos_to_write

    # now, for each SAMPLE compute and write the FORMAT's field of interest


def process_format_wide(mapped_record, my_samples, my_formats):

    format_to_write = []
    for name in my_samples:
        format_to_write += [
            mapped_record[name].get(fmtags, ".") for fmtags in my_formats
        ]

    # ?? to do (Bishwa) - add method to convert GT tags numeric values to IUPAC bases
    return format_to_write


def process_format_long(mapped_record, sample, my_formats):
    format_to_write = [sample]
    format_to_write += [mapped_record[sample].get(fmtags, ".") for fmtags in my_formats]
    # ?? to do (Bishwa) - add method to convert GT tags numeric values to IUPAC bases

    return format_to_write


def find_sample_name_by_stringmatch(soi, all_samples):
    # for situation when sample name are given in prefix, suffix, or match
    # e.g: -sample MA605 prefix:ms match:A6
    
    selected_samples = []
    
    matches = ["prefix:", "suffix:", "match:"]
    
    for name in soi:
        if name.startswith("prefix:"):
            nameprefix = name.lstrip("prefix:")
            selected_samples += [x for x in all_samples if x.startswith(nameprefix)]
            
        elif name.startswith("suffix:"):
            namesuffix = name.lstrip("suffix:")
            selected_samples += [x for x in all_samples if x.endswith(namesuffix)]
            
        elif name.startswith("match:"):
            namematch = name.lstrip("match:")
            selected_samples += [x for x in all_samples if namematch in x]
            
        else:
            selected_samples += [name]
    
    # to make sure the sample names are unique, but will randomize the order of the names
    selected_samples = set(selected_samples)
    
    # this ensures that order of sample name is returned according to order of file sample names        
    sample_set = [sample for sample in all_samples if sample in selected_samples]
    
    # further check sample names are valid
    sample_set = process_fields(sample_set, all_samples, argument_flag='-samples')    
    
    return sample_set
    

def check_sample_and_format(sample_names, format_tags):
    """ check that format and sample names are raised properly 
        - if no samples are raised no formats can be raised and vice versa. 
    """
    if len(sample_names) == 0 and len(format_tags) != 0:
        print("if no sample names then there should be no format tags")
        print("exiting")
        sys.exit(0)

    if len(sample_names) != 0 and len(format_tags) == 0:
        print("if no format tags then there should be no sample names")
        print("exiting")
        sys.exit(0)
        
        
def parse_genotypes_format(gtbase):
    gt_output = []
    for gts in gtbase:
        gt_output.append(gts.split(':'))
        
    return tuple(gt_output)

