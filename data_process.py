#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
from mininet.log import info, error, debug, output, warn

def readtxt(str,send_pkt,retrans_pkt):
	filename = str + "netstat.txt"
	file = open(filename,"r")
	trans_sum = [];
	retrans_sum = [];
	while 1:
		line = file.readline()
		if not line:
			break
		if line.find("segments send out") == -1:
			pass
		else:
			i=line.find("segments send out")-1
			str = line[4:i]
			trans_sum.append(int(str))
		if line.find("segments retransmited") == -1:
			pass
		else:
			i=line.find("segments retransmited")-1
			str = line[4:i]
			retrans_sum.append(int(str))
	j = len(trans_sum)-1
	SendPkt = trans_sum[j] - trans_sum[j-1]
	j = len(retrans_sum)-1
	RetransPkt = retrans_sum[j] - retrans_sum[j-1]
	send_pkt.append(SendPkt)
	retrans_pkt.append(RetransPkt)
	file.close()
	return

host_num = 13
tag_num = host_num -1
send_pkt = [];
retrans_pkt = [];
rate = [];
total_send = 0
total_retrans = 0
#read the statics in the files
for i in xrange(0,tag_num):
	string ='h' + str(i+1)
	readtxt(str=string,send_pkt = send_pkt,retrans_pkt = retrans_pkt);
#calculate the packet lost rate of each host
for i in xrange(0,tag_num):
	rate.append(retrans_pkt[i]/send_pkt[i])
	total_retrans += retrans_pkt[i]
	total_send += send_pkt[i]
#show the data
print retrans_pkt
print send_pkt
rate.append(total_retrans/total_send)
print "The packet loss rate of h1 to h12 are:"
#for i in xrange(0,tag_num):
#	output("%.8f\t" %rate[i])
print "%.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f %.8f " %(rate[0],rate[1],rate[2],rate[3],rate[4],rate[5],rate[6],rate[7],rate[8],rate[9],rate[10],rate[11])
print "The total packet loss rate is:%.8f" %rate[tag_num] 
