#!/bin/bash

sudo useradd user1
sudo useradd user2
sudo useradd examuser
sudo useradd lastuser

echo "user1:user1" | sudo chpassswd
echo "user2:user2" | sudo chpasswd
echo "examuser:examuser" | sudo chpasswd
echo "lastuser:lastuser" | sudo chpasswd

sudo chage -d 0 lastuser

