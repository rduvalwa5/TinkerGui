#!/usr/local/bin/python3
'''
Created on Mar 8, 2013
For interview test
Consider a log file that showed important network events including packet drops.  Log format is below:
2012-12-29 22:00 172.16.8.48 drops 24 packets
2012-12-29 22:01 172.16.8.48 buffer full
2012-12-29 22:02 172.16.8.45 drops 21 packets
2012-12-29 22:03 172.16.8.44 drops 10 packets
2012-12-29 22:04 172.16.8.48 drops 10 packets
2012-12-29 22:04 172.16.8.48 latency 3 seconds
2012-12-29 22:03 172.16.8.45 drops 2 packets

Write a script that generates a report of total packets dropped per IP address.  Report format is below:
172.16.8.48 drops total 34 packets
172.16.8.45 drops total 23 packets
172.16.8.44 drops total 10 packets

OPTIONAL BONUS:  Sort the report by IP address, like this:
172.16.8.44 drops total 10 packets
172.16.8.45 drops total 23 packets
172.16.8.48 drops total 34 packets

@author: rduvalwa2
'''
report = {}
open_testFile = open('testfile.txt', 'r').readlines()  # open and read from same expression
string_trigger = "drops"
for line in open_testFile:
    if line.find(string_trigger) > 1:
                words = line.strip().split()
                report[words[2]] = words[4]
print("Unsorted Report")
for ip in report:
    print(ip, "drops total" , report[ip], "packets")
print("Sorted Report")
for ip in sorted(report):
    print(ip, "drops total" , report[ip], "packets")

