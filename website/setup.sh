#!/bin/bash

iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 5671 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 5672 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 15672 -j ACCEPT
iptables-save
