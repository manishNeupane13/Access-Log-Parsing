import csv
import threading
import re
ips_list=[]
def ipreader():
    with open("access1.log", "r") as logfile:
        global ips_list
        log = logfile.read()
        regexp = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        ips_list = re.findall(regexp, log)
def write_csv():
    with open("ip.csv", "w") as csvfile:
    
        writer = csv.writer(csvfile)
        for item in ips_list:
            writer.writerow((item,))
if __name__ == '__main__':
    # t1 = threading.Thread(ipreader())
    # t1.start()
    # t1.join()
    # t2 = threading.Thread(write_csv())
    # t2.start()
    # t2.join()
    ipreader()
    write_csv()
