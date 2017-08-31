#!/usr/bin/env python
# -*- coding: utf-8 -*-
# this is python 2.7

import sys

import helper_url

def get_suspicious_urls(ReportName,THRESHOLD=1):

    import collections
    reports = helper_url.read_a_list_from_a_file(ReportName)

    repsonse_not_valid = 'response not valid'
    suspicious_srcs = collections.defaultdict(int)

    for i in reports:
        if repsonse_not_valid in i:
            continue
        elements = i.split('\t')
        if len(elements) >= 2 :
            try:
                src = elements[0]
                ele = elements[1]
                reported_av = int(ele)
                if reported_av >= THRESHOLD:
                    suspicious_srcs[src] = ele
            except:
                #print ('parse error, at '+ str(i)+'. Go to next...')
                pass

    for i in suspicious_srcs:
        print ("{} -> {}".format(i,suspicious_srcs[i]))

    return (suspicious_srcs)


if __name__ == "__main__":
    get_suspicious_urls("report.txt")
