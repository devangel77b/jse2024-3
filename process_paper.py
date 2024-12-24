#!/usr/bin/env python

import yaml
import pymupdf

input_file = open('papers.yaml','r')
paper_list = yaml.safe_load(input_file)

thepage = 1
for entry in paper_list:
    print(entry)
    entry_pdf = pymupdf.open(entry['pdf'])
    print("{0} pages in {1}".format(entry_pdf.page_count,entry['pdf']))
    print(r"{{ {0} \\ {1} }}".format(entry['title'],entry['authors']))
    # get number of pages and increment count
    # add to toc
    entry_pdf.close()

input_file.close()
    
