import csv
from os import scandir


def comma_remover(input_file):
    output_file = '/Users/pharrell/Documents/Data/PercentAnalysis/CSV/001CommaRemoved/' + input_file.split('/')[-1]
    with open(input_file, 'r') as r, \
            open(output_file, 'w') as w:
        cnt = 0
        for num, line in enumerate(r):
            cnt += 1
            if num >= 0:
                newline = line[:-2] + "\n" if "\n" in line else line[:-1]
            else:
                newline = line
            w.write(newline)

        print("total lines of " + input_file + str(" :      ") + str(cnt))


def average_last_column(csv_file_path):
    column_sum = 0
    row_count = 0
    with open(csv_file_path, "rt") as f:
        reader = csv.reader(f)
        for row in reader:
            row_count += 1
            for column_idx, column_value in enumerate(row):
                column_value = float(column_value)
                column_idx = int(column_idx)
                if column_idx == 5:
                    if column_value != 1:
                        try:
                            column_sum += column_value
                        except BaseException as e:
                            print(str(e))
                    else:
                        row_count -= 1
    average = float(column_sum) / float(row_count)
    print(csv_file_path, ': ', round(average, 4), ' row count: ', row_count)


def scan_tree(path):
    """Recursively yield DirEntry objects for given directory."""
    list_of_file_paths = []
    for file_obj in scandir(path):
        if file_obj.is_dir(follow_symlinks=False):
            # yield from scan_tree(file_obj.path)
            list_of_file_paths.extend(scan_tree(file_obj.path))
        else:
            # yield file_path
            if 'DS_Store' not in file_obj.path:
                list_of_file_paths.append(file_obj.path)
    return list_of_file_paths
