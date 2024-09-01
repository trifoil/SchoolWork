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


echo "*/7 8-12 * * * free -h | grep Mem | awk '{print \$4}' >> /tmp/mem" | sudo tee -a /etc/crontab
echo "tail -n 10 /tmp/mem" | sudo tee -a /root/.bashrc

# crontab -e

#------------------
sudo mount -o remount,usrquota /home
sudo quotacheck -cug /home
sudo quotaon /home
sudo setquota -u examuser 0 0 50 50 /home
#------------------


echo "find /etc -type f -mmin -60" | sudo tee /tmp/exam.txt

sudo sed -i '/\/boot/s/defaults/defaults,ro/' /etc/fstab
sudo mount -o remount,ro /boot


sudo lvextend -L +1G /dev/mapper/fedora-home
sudo xfs_growfs /dev/mapper/fedora-home


# Script pour configurer iptables

# Vider les tables existantes
iptables -F

# Permettre les connexions entrantes sur les ports 80 (HTTP) et 443 (HTTPS)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Bloquer tout le reste
iptables -A INPUT -j DROP

# Sauvegarder les règles iptables
sudo iptables-save | sudo tee /etc/iptables/rules.v4


# Copiez le script dans /etc/init.d/ et donnez-lui les permissions d'exécution
sudo cp iptables-config.sh /etc/init.d/
sudo chmod +x /etc/init.d/iptables-config.sh

# Utilisez systemctl pour activer le script au démarrage
sudo systemctl enable iptables-config.sh

