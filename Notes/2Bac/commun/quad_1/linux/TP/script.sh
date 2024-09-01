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

sudo mkdir /users
sudo groupadd usersgroup

sudo usermod -aG usersgroup user1
sudo usermod -aG usersgroup user2

sudo chown :users /users
sudo chmod 470 /users

sudo find / -uid 1001 > /tmp/toto

sudo find / -uid 1005 -exec rm -rf {} +
sudo userdel toto

sudo mkdir /exam
sudo chown :lastuser /exam

sudo dnf install NetworkManager-tui
sudo systemctl restart NetworkManager

sudo dnf install nfs-utils
sudo mkdir /partage
sudo chown user1 /partage
sudo chmod 755 /partage
echo "/partage 192.168.0.0/24(rw,sync,no_root_squash,no_subtree_check)" | sudo tee -a /etc/exports
sudo exportfs -a
sudo systemctl restart nfs-server

sudo touch /temp/test
sudo chattr +i /temp/test
