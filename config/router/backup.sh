#!/bin/bash

rm /root/ftp/quagga*
vtysh -c write
tar -zcvf /root/ftp/quagga-1_$(date +%Y-%m-%d_%H-%M-%S).tar.gz /etc/quagga/
