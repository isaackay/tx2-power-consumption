import sys
import os
import pprint


def average_from_path(path):
    sum = 0.0
    cnt = 0
    with open(path, 'r') as f:
        for line in f:
            sum += float(line)
            cnt += 1
    return sum / cnt


# Usage: ./avg
# Effect: Output the json data of power constant
if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    if len(sys.argv) == 1:
        paths = ["4k_360", "1080p"]
        names = ["elephant", "rhino", "roller", "paris", "nyc"]
        power_files = ["ddr", "soc", "cpu", "gpu", "wifi"]
        name_dict = {}
        for name in names:
            vr_dict = {}
            vr_dict["soc"] = 0
            vr_dict["wifi"] = 0
            normal_dict = {}
            normal_dict["soc"] = 0
            normal_dict["wifi"] = 0
            for pf in power_files:
                for path in paths:
                    target_path = os.path.join(path, name + "_" + pf + '.txt')
                    idle_path = os.path.join("idle", "idle_" + pf + '.txt')
                    # print(target_path, idle_path)
                    # print(average_from_path(target_path),
                    # average_from_path(idle_path))

                    value = average_from_path(target_path) - average_from_path(idle_path)
                    if path == "1080p":
                        if pf != "wifi":
                            normal_dict["soc"] += value
                        else:
                            normal_dict["wifi"] += value
                    if path == "4k_360":
                        if pf != "wifi":
                            vr_dict["soc"] += value
                        else:
                            vr_dict["wifi"] += value
            # print(value)
            name_dict[name] = {"360": vr_dict, "normal": normal_dict}
        pp.pprint(name_dict)
