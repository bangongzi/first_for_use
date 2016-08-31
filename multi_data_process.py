#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys
#from mininet.log import info, error, debug, output, warn
#The input should be like data_process.py (left=1) (right=12) (latency=1ms) depth=1

def readtxt(str,send_pkt,retrans_pkt,depth = 1 ):
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
	j = len(trans_sum)-depth
	SendPkt = trans_sum[j] - trans_sum[j-1]
	j = len(retrans_sum)-depth
	RetransPkt = retrans_sum[j] - retrans_sum[j-1]
	send_pkt.append(SendPkt)
	retrans_pkt.append(RetransPkt)
	file.close()
	return

def data_process(left,right,depth):
	txt_read_num = right -left + 1
	for i in xrange(1,depth+1):
		send_pkt = []
		retrans_pkt = []
		#The first element is used to store the total
		#number of packets retransmitted,the second for 
		#packets send,the third is for packet lost rate
		rate = [0,0,0]
		for j in xrange(left,right+1):
			string ='h' + str(j)
			readtxt(str=string,send_pkt = send_pkt,retrans_pkt = retrans_pkt,depth = (depth+1-i))
		for j in xrange(0,txt_read_num):
			rate[0] += retrans_pkt[j]
			rate[1] += send_pkt[j]
		rate[2] = rate[0]/rate[1]
		print "#############Information of test%d" %i
		print "Here are numbers of retrans/send packets of h%s to h%s:" %(str(left),str(right))
		print retrans_pkt,"\n",send_pkt
		print "The total packet loss rate is:%.8f" %rate[2]

if len(sys.argv) == 2:
	data_process(left = 1,right = 12,depth=int(sys.argv[1]) )
elif len(sys.argv) == 3:
	print "The latency is %s" %sys.argv[1]
	data_process(left = 1,right = 12,depth=int(sys.argv[2]) )
elif len(sys.argv) == 4:
	data_process(left = int(sys.argv[1]),right = int(sys.argv[2]),depth=int(sys.argv[3])  )
elif len(sys.argv) == 5:
	print "The latency is %s" %sys.argv[3]
	data_process(left = int(sys.argv[1]),right = int(sys.argv[2]),depth=int(sys.argv[4])  )
else:
	print "Wrong number of parameters"