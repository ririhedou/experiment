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
def analyze_files_to_csv(filename, filepath):

    cur_file, cur_idx, cur_src = None, None, None

    infile = open(filename, 'r')
    cur_src = infile.readline().rstrip().strip()

    if not filter_src(cur_src):
        return None

    domain_idx = filename.split("/")[-1]

    domain = domain_idx.split("-")[0]
    if not str(filepath).endswith("/") :
        filepath = filepath + "/"

    cur_file = filepath + domain
    cur_idx = domain_idx.split("-")[1]

    tmp_dic = {
        "filename": cur_file,
        "JS_IDX": cur_idx,
        "src": cur_src,
        "domain": domain,
        "y_lable": None
    }
    return tmp_dic

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


def get_result(path, myfilepath):
    import os
    files = [os.path.join(path,fn) for fn in next(os.walk(path))[2]]

    print (files)
    raw_input()
    ans = []
    for i in files:
        dic = analyze_files_to_csv(i,myfilepath)
        if not dic:
            ans.append(dic)

    return ans

if __name__ == "__main__":

    mypath = "/mnt/sdb1/domcrawl/htmls/1/"
    d = "/tmp/1"
    ans = get_result(d,mypath)
    write_into_a_csv_file(ans,"1.csv")
    #dicList2 = analyze_files_to_csv(filename2)
    #dicList = dicList+dicList2
    pass
