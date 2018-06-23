#!/bin/busybox ash

# Obtener direccion ip externa.
EXTIP=$(ifconfig eth1 | grep "inet " | awk -F ' ' '{split($2,ip,":"); print ip[2]}')

# Agregar las subredes que se conectaran a internet.
sudo iptables -t nat -A POSTROUTING -s 10.0.100.0/24 -o eth1 -j SNAT --to-source $EXTIP
sudo iptables -t nat -A POSTROUTING -s 10.0.1.0/24 -o eth1 -j SNAT --to-source $EXTIP
sudo iptables -t nat -A POSTROUTING -s 10.0.2.0/24 -o eth1 -j SNAT --to-source $EXTIP
