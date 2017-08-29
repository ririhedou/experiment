# used for data processing
# -*- coding: utf-8 -*-
# this is python 2.7

__author__ = "ketian"
__time__ = "2017"


import csv
import copy
def write_into_a_csv_file_one_dict(ans,filename="csvfile.csv"):
    """
    :param ans: a list of dictionaries
    :return:
    """

    keys = ans.keys()
    keys.sort()

    with open(filename, 'wb') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(keys)
        writer.writerows(zip(*[ans[key] for key in keys]))

    pass

def write_into_a_csv_file(ans,filename="csvfile.csv"):
    """
    :param ans: a list of dictionaries
    :return:
    """

    keys = ans[0].keys()
    keys.sort()

    with open(filename, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(ans)


#do the result extraction
def analyze_files_to_csv(filename, out="out.csv"):
    ff = "/mnt/sdb1/domcrawl"
    Idx = "IDX"
    detect = "detect"

    dic =[]

    with open(filename,"r") as f:
        lines = f.readlines()
        cur_file, cur_idx, detect_src = None,None,None
        for line in lines:
            line = line.strip()

            if line.startswith(ff):
                cur_file = line
            if line.startswith(Idx):
                cur_idx = int(line.split(" ")[0].split(":")[-1])
            if line.startswith(detect):
                cur_src = line.split(" ")[4].split("->")[-1]
                tmp_dic = {
                    "filename":cur_file,
                    "js idx":cur_idx,
                    "src":cur_src
                }
                dic.append(copy.deepcopy(tmp_dic))

    #write_into_a_csv_file(dic, filename=out)
    return dic


#filename="ex_aug_29/iframe2_res.out"
#out = "iframe.csv"
#analyze_files_to_csv(filename,out)
if __name__ == "__main__":
    martin =[ "martin_embed.txt", "martin_external.txt", "martin_iframe.txt"]
    alist = []
    for i in martin:
        alist.extend(analyze_files_to_csv(i))
    write_into_a_csv_file(alist, "martin_data.csv")

