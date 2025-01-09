import pandas as pandas
read_time =[2,3,6]
sleep_hour = [3,7,8]
stu_name = ["hemanth","lokesh","mintu"]
dic1 = {
    "read_time":read_time,
    "sleep_hour":sleep_hour,
    "stu_name":stu_name
} 
print(dic1)
df = pandas.DataFrame(dic1)
print(df)