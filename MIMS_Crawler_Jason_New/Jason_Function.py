import collections
import json
import pprint


def vcf_records_as_json(metadict, outFile):
    """Convert the dictionary to a json object and write to a file"""
    print("\twriting metadata as JSON")

    json_obj_string = json.dumps(metadict)
    datastore = json.loads(json_obj_string)

    with open("%s.json" % outFile, "w", encoding="utf-8") as write_as_json:
        json.dump(datastore, write_as_json, ensure_ascii=False, indent=4)