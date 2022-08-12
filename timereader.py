from os import write
import threading
import re
import csv
time_list = []
hour_list=[]
def datatimereader():
    with open("access1.log", "r") as logfile:
        log = logfile.read()
        global time_list,hour_list,hour_val
        regexp = r'\d{2}\/[A-z][a-z][a-z]\/\d{4}'
        hour_list = re.findall(r'\:\d{2}\:',log)
        time_list = re.findall(regexp, log)
def write_hour():
    with open("hour.csv", "w") as csvfile:
        unique_list = []
        writer = csv.writer(csvfile)
        header=["Hour","Frequency"]
        writer.writerow(header)
        for item in hour_list:
            if item not in unique_list:
                unique_list.append(item)
        for item in unique_list:
            writer.writerow((item, hour_list.count(item)))
def write_date():
    with open("date.csv", "w") as csvfile:
        unique_list = []
        writer = csv.writer(csvfile)
        header = ["Date", "Frequency"]
        writer.writerow(header)
        for item in time_list:
            #print (item)
            if item not in unique_list:
                unique_list.append(item)
                # print("uni",unique_list)
        for item in unique_list:
            writer.writerow((item, time_list.count(item)))
if __name__=="__main__":
    # t1=threading.Thread(datatimereader())
    # t1.start()
    # t1.join()
    # t2 = threading.Thread(write_hour())
    # t2.start()
    # t2.join()
    # t3 = threading.Thread(write_hour())
    # t3.start()
    # t3.join()

    datatimereader()
    write_date()
    write_hour()
        
