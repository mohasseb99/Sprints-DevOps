#!/usr/bin/env bash

# these commands are executed in the terminal but files not found
#  /etc/ssh/sshd_config:

echo "Please, Enter a Port Number"
read portNo

if [ ${portNo} -ge 1024 ] && [ ${portNo} -le 32767 ] || [ ${portNo} == 22 ]
then 
#	sed 's/Port .*/Port $portNo/' /etc/ssh/ssh_config
	echo "The Port Has Been Changed"
else
        echo "Invalid port"
        echo "Please Enter Another Number : "
        read ${portNo}
fi

#sed 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/ssh_config

#sudo systemctl restart ssh

echo "executed successfully"
