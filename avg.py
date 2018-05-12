import sys
import os
import re


def avg_from_folder(path, out, base_dict):
    p = re.compile('([\w,-]*)-(\d)')
    sum_dict = {}

    with open(out, 'w') as f:
        for filename in sorted(os.listdir(path)):
            if filename[0] != '.':
                # print('processing:', filename)
                avg = average(os.path.join(path, filename))

                # extract file name
                k = filename.split('_')
                name = k[0]
                match = p.match(name)
                extract_name = match.group(1)

                # if k[3] == 'CPU':
                #     avg -= base_dict[filename.split('_')[3]]

                if k[3] == 'SOC' or k[3] == 'WIFI':
                    if k[3] == 'SOC':
                        avg -= base_dict[filename.split('_')[3]]
                        extract_name = extract_name + '_' + 'SOC'
                    elif k[3] == 'WIFI':
                        extract_name = extract_name + '_' + 'WIFI'

                    if extract_name in sum_dict:
                        sum_dict[extract_name] += avg
                    else:
                        sum_dict[extract_name] = avg

        for k, v in sum_dict.items():
            line = k + ':' + str(v / 3) + '\n'
            print(line)
            f.write(line)


def get_baseline_data(path):
    base_dict = {}
    for filename in sorted(os.listdir(path)):
        if filename[0] != '.':
            avg = average(os.path.join(path, filename))
            k = filename.split('_')
            base_dict[k[3]] = avg
    return base_dict


def average(filename):
    sum = 0.0
    cnt = 0

    with open(filename, 'r') as f:
        for line in f:
            sum += float(line)
            cnt += 1

    return sum / cnt


# this program is for printing all the average file in the specify folder
# ex: python3.5 avg.py dump out.txt
if __name__ == "__main__":
    path = sys.argv[1]
    out = sys.argv[2]
    base_dict = get_baseline_data('idle')
    avg_from_folder(path, out, base_dict)
