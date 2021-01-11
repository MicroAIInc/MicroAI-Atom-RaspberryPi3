from MicroAI_Network_Output import mAI_N
import csv
import time
import redis


def read_router(group=None):
    with open("AIengine_router", "r") as route_table:
        csv_reader = csv.reader(route_table)
        line_count = 0
        groups = []
        for row in csv_reader:
            if line_count > 0:
                if group is not None:
                    if row[7] == str(group):
                        groups.append(row[7])
                else:
                    groups.append(row[7])
            line_count += 1
    groups = list(dict.fromkeys(groups))
    groups.sort()
    return groups


def get_obj(group_list):
    obj_list = []
    for each in group_list:
        obj_list.append(mAI_N(each))
    return obj_list


def get_result(obj, G):
    ratio = obj.abnormalRatio()
    if ratio > .15:
        print("Group {} IS EXPERIENCING ABNORMAL BEHAVIOR".format(G))
    else:
        print("Group {} is behaving normally".format(G))
    return


def main():
    main_group=read_router()
    main_obj_list=get_obj(main_group)
    while True:
        for i in range(len(main_group)):
            get_result(main_obj_list[i], main_group[i])
        print()
        time.sleep(2)

if __name__ == "__main__":
    main()
