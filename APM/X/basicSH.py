import redis
import time
from sense_hat import SenseHat
import csv

sense = SenseHat()
localIP = "192.168.1.89"  # Must be edited to be devices local IP address


#  Reads the route table to determine which channels to send data to and build 2D list
def read_router():
    table = []
    with open("signalsource_router", "r") as route_table:
        csv_reader = csv.reader(route_table)
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                if row[1] == "127.0.0.1" or row[1] == "localhost" or row[1] == localIP:  # Removes channels assigned to other X-Code devices
                    table.append(row)
            line_count += 1
    return table


#  Returns the SenseHat acc/gyro information
def get_data():

    a_x = []
    a_y = []
    a_z = []
    g_x = []
    g_y = []
    g_z = []


    start = time.time()
    while time.time() - start < .8:
        acc = sense.get_accelerometer_raw()
        gyro = sense.get_gyroscope_raw()
        a_x.append(acc["x"])
        a_y.append(acc["y"])
        a_z.append(acc["z"])
        g_x.append(gyro["x"])
        g_y.append(gyro["y"])
        g_z.append(gyro["z"])

    sensor_vals = [a_x, a_y, a_z, g_x, g_y, g_z]
    avg_list = [sum(each)/len(each) for each in sensor_vals]
    return avg_list


def send2Redis(table, routeChannels, data):
    unique_dict = {}
    for i in range(routeChannels):
        if i == 0:
            unique_dict[table[0][2]] = {table[0][0]: data[0]}
        else:
            if table[i][2] in unique_dict:
                unique_dict[table[i][2]][table[i][0]] = data[i]
            else:
                unique_dict[table[i][2]] = {table[i][0]: data[i]}
    print(unique_dict, "\n")
    for each in unique_dict:
        addr = each.split(":")
        #  Potential problem depending on how db values in route table get used
        r = redis.Redis(host=addr[0], port=addr[1], db=0)
        r.mset(unique_dict[each])
        r.close()


def main():
    table = read_router()
    routeChannels = len(table)
    o_data = get_data()
    totalChannels = len(o_data)
    print("routeChannels", routeChannels, "\ttotalChannels", totalChannels)
    if totalChannels != routeChannels:  # Checks to see if total data channels is in line with route table
        print("There is a discrepancy in the number of Total Channels and the number of Routed Channels")
        return
    else:
        while True:
            data = get_data()
            send2Redis(table, routeChannels, data)



main()
