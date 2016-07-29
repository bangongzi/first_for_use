#!/bin/bash
#This file is write to configure ports in simplified_topo.
#the ports is divided into 4 layers,layer1 is for access layer,
#layer2 is for convergence layer,layer3 is for skeleton layer,
#layer4 consists only one port,which is s1-eth1
latenci=`expr 1000 \* ${3}` 
if test $# -eq 3
then
#	this is about to configure ports of layer1
	if test $1 -eq 1
	then
		for i in 5 6 7 8 9 10
		do
			for j in 1 2
			do
				echo "dev s${i}-eth${j} are going to be configured"
				tc qdisc delete dev s${i}-eth${j} root
				tc qdisc add dev s${i}-eth${j} handle 1: root dsmark indices 1 default_index 0
				tc qdisc add dev s${i}-eth${j} handle 2: parent 1: tbf burst 2048KB latency ${latenci} mtu 1514 rate ${2}Gbit
				tc qdisc show dev s${i}-eth${j}
			done
		done
#	This is about to configure ports of layer2
	elif test $1 -eq 2
	then
		for i in 5 6 7 8 9 10
		do
			j=3
			echo "dev s${i}-eth${j} are going to be configured"
			tc qdisc delete dev s${i}-eth${j} root
			tc qdisc add dev s${i}-eth${j} handle 1: root dsmark indices 1 default_index 0
			tc qdisc add dev s${i}-eth${j} handle 2: parent 1: tbf burst 2048KB latency ${latenci} mtu 1514 rate ${2}Gbit
			tc qdisc show dev s${i}-eth${j}
		done
		for i in 2 3 4
		do
			for j in 1 2
			do	
				echo "dev s${i}-eth${j} are going to be configured"
				tc qdisc delete dev s${i}-eth${j} root
				tc qdisc add dev s${i}-eth${j} handle 1: root dsmark indices 1 default_index 0
				tc qdisc add dev s${i}-eth${j} handle 2: parent 1: tbf burst 2048KB latency ${latenci} mtu 1514 rate ${2}Gbit
				tc qdisc show dev s${i}-eth${j}	
			done
		done
#	This is about to configure ports of layer3
	elif test $1 -eq 3
	then
		for i in 2 3 4
		do
			j=3
			echo "dev s${i}-eth${j} are going to be configured"
			tc qdisc delete dev s${i}-eth${j} root
			tc qdisc add dev s${i}-eth${j} handle 1: root dsmark indices 1 default_index 0
			tc qdisc add dev s${i}-eth${j} handle 2: parent 1: tbf burst 2048KB latency ${latenci} mtu 1514 rate ${2}Gbit
			tc qdisc show dev s${i}-eth${j}
		done
		i=1
		for j in 2 3 4
		do
			echo "dev s${i}-eth${j} are going to be configured"
			tc qdisc delete dev s${i}-eth${j} root
			tc qdisc add dev s${i}-eth${j} handle 1: root dsmark indices 1 default_index 0
			tc qdisc add dev s${i}-eth${j} handle 2: parent 1: tbf burst 2048KB latency ${latenci} mtu 1514 rate ${2}Gbit
			tc qdisc show dev s${i}-eth${j}
		done
#	This is about to configure ports of layer4
	elif test $1 -eq 4
	then
		i=1
		j=1
		echo "dev s${i}-eth${j} are going to be configured"
		tc qdisc delete dev s${i}-eth${j} root
		tc qdisc add dev s${i}-eth${j} handle 1: root dsmark indices 1 default_index 0
		tc qdisc add dev s${i}-eth${j} handle 2: parent 1: tbf burst 2048KB latency ${latenci} mtu 1514 rate ${2}Gbit
		tc qdisc show dev s${i}-eth${j}
	else
		echo "the first parameter should be 1,2,3 or 4"
	fi
else
	echo "The input number format is not right,the right 
format is layer=1,rate=1(1Gbit),limit=3(ms)"
fi