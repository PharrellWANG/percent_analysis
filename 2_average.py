import os
from utils import average_last_column, scan_tree


HOME = os.environ['HOME']
PREFIX = '/Documents/Data/PercentAnalysis/CSV/001CommaRemoved/'
# No Duplication Ref
NODUPREF = '/Documents/Data/PercentAnalysis/CSV/NoDuplicationReferences/'

list_of_input_files = scan_tree(HOME + PREFIX)
list_of_no_dup_ref_files = scan_tree(HOME + NODUPREF)


for x in range(len(list_of_input_files)):
    file_name = list_of_input_files[x].split('/')[-1]
    skip_flag = False
    for y in range(len(list_of_no_dup_ref_files)):
        if list_of_no_dup_ref_files[y].split('/')[-1] == file_name:
            skip_flag = True
            break
    if not skip_flag:
        average_last_column(list_of_input_files[x])
