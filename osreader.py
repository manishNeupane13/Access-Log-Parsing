import re
from collections import Counter
import csv
import threading
os_list=[]
def osreader1():

    global os_list
    with open("access1.log", 'r') as logfile:

        log = logfile.read()
        regexp = r'\([\w\d\s\.]*;\s[\w]*;\s[\w\s\d]*[;\s]*[\w\d:\.]*\)'
        os_list = re.findall(regexp, log)
def write_csv():
    with open("os.csv", "w") as csvfile:
        unique_list = []
        writer = csv.writer(csvfile)
        header = ["Os", "Frequency"]
        writer.writerow(header)
        for item in os_list:
            #print (item)
            if item not in unique_list:
                unique_list.append(item)
                # print("uni",unique_list)
        for item in unique_list:
            writer.writerow((item, os_list.count(item)))

if __name__=="__main__":
    # t1=threading.Thread(osreader1())
    # t1.start()
    # t1.join()
    # t2=threading.Thread(write_csv())
    # t2.start()
    # t2.join()
    osreader1()
    write_csv()
