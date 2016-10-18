# first_for_use
These files are used for network traffic simulation.
How to get pkt lost rate:
    Here we use command netstat -s to get rate.We assumed tcp send number as send number,tcp resend number as loss number,then loss rate can be caculated.
cli.py,net.py are located in ~/mininet/mininet;mn is located in ~/mininet/bin
ports_config.sh,port_config.sh are in the /root/ They are used to configure the ports parameters
data_process.py,multi_data_process.py are in the ~/log/netstat/.They are used to read the statistics.
