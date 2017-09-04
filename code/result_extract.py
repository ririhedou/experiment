# used for data processing
# -*- coding: utf-8 -*-
# this is python 2.7

__author__ = "ketian"
__time__ = "2017"


import csv
import copy


def write_list_into_a_file(alist,filename):
    with open(filename,'wb') as f:
        for i in alist:
            f.write(i + "\n")
        f.flush()
        f.close()


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


def filter_src(cur_src):
    if cur_src == "about:blank":
        return False
    if len(cur_src) <1 :
        return False
    if cur_src == "javascript:false":
        return False
    return True

#do the result extraction
def analyze_files_to_csv(filename, out="out.csv"):
    ff = "/mnt/sdb1/domcrawl"
    ff2 = "/Users/ketian/Desktop"
    Idx = "IDX"
    detect = "detect"

    dic =[]

    with open(filename,"r") as f:
        lines = f.readlines()
        cur_file, cur_idx, detect_src = None,None,None
        for line in lines:
            line = line.strip()

            if line.startswith(ff) or line.startswith(ff2):
                cur_file = line
            if line.startswith(Idx):
                cur_idx = int(line.split(" ")[0].split(":")[-1])
            if line.startswith(detect):
                cur_src = line.split(" ")[4].split("->")[-1]
                tmp_dic = {
                    "filename":cur_file,
                    "JS_IDX":cur_idx,
                    "src":cur_src,
                    "domain": cur_file.split("/")[-1],
                    "y_lable": None
                }
                if filter_src(cur_src):
                    dic.append(copy.deepcopy(tmp_dic))

    #write_into_a_csv_file(dic, filename=out)
    return dic

def get_unique_list_of_urls(dicList):
    src = []
    for i in dicList:
        if i["src"] == "about:blank":
            continue
        src.append(i["src"])

    print (len(src))
    src = list(set(src))
    print (len(src))
    write_list_into_a_file(src, "iframe_iframe2_unique_src_url.txt")


if __name__ == "__main__":
    #martin =[ "martin_embed.txt", "martin_external.txt", "martin_iframe.txt"]
    #alist = []
    #for i in martin:
    #    alist.extend(analyze_files_to_csv(i))
    #write_into_a_csv_file(alist, "martin_data.csv")

    #data = ["iframe_res.out", "iframe2_res.out"]
    #data2 = ["martin_embed.txt","martin_iframe.txt","martin_external.txt"]
    #data = data + data2
    data = ["2.out"]

    dicList = []
    for i in data:
        i = "../ex_aug_29/" + i
        dicList += analyze_files_to_csv(i)

    #dicList2 = analyze_files_to_csv(filename2)
    #dicList = dicList+dicList2
    write_into_a_csv_file(dicList,"alexa1m_2.csv")
