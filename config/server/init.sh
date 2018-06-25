#!/bin/bash

if [ -z "$1" ]; then
	echo "Uso: ./init.sh <IP_MASK> <GATEWAY>"
	exit 1
fi

IP=${1}
GATEWAY=${2}
INTERFACE=enp0s0
DNS_SERVER=10.0.100.100

# ************* rc.local
echo "#!/bin/bash
ifconfig $INTERFACE up
ifconfig $INTERFACE $IP
ip route add default via $GATEWAY

/etc/init.d/apache2 start
/etc/init.d/snmpd start

exit 0" > rc.local
chmod +x rc.local
chmod +x rc.local
mv rc.local /etc/

# ************ resolv.conf
echo "nameserver $DNS_SERVER
nameserver 8.8.8.8" > resolv.conf
mv resolv.conf /etc/

# ************ Install dependences.
apt update && apt install snmpd

# *********** snmpd.conf
echo "#
# example access restrictions setup
#
com2sec readonly default public
group MyROGroup v2c readonly
view all included .1 80
access MyROGroup "" any noauth exact all none none
#
# enable master agent for AgentX subagents
#
master agentx" > snmpd.conf
mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.bak
mv snmpd.conf /etc/snmp/

# ********** Remover este script.
rm init.sh
reboot
