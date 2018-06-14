#!/bin/bash

ifconfig eth0 up
ifconfig eth0 10.0.1.1/24
route add -net default gw 10.0.1.254

#dns
rm /etc/resolv.conf
echo domain home.lan >> /etc/resolv.conf
echo search home.lan >> /etc/resolv.conf
echo nameserver 10.0.1.254 >> /etc/resolv.conf
echo nameserver 8.8.8.8 >> /etc/resolv.conf
echo nameserver 8.8.4.4 >> /etc/resolv.conf
