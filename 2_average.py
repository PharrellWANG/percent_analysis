import os
from utils import average_last_column, scan_tree


HOME = os.environ['HOME']
PREFIX = '/Documents/Data/PercentAnalysis/CSV/001CommaRemoved/'

list_of_input_files = scan_tree(HOME + PREFIX)


for x in range(len(list_of_input_files)):
    average_last_column(list_of_input_files[x])
