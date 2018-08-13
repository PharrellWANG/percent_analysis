import os
from utils import comma_remover, scan_tree


HOME = os.environ['HOME']
ORIG_PREFIX = '/Documents/Data/PercentAnalysis/CSV/Orig/'
CM_PREFIX = '/Documents/Data/PercentAnalysis/CSV/001CommaRemoved/'

list_of_input_files = scan_tree(HOME + ORIG_PREFIX)

for x in range(len(list_of_input_files)):
    comma_remover(list_of_input_files[x])
