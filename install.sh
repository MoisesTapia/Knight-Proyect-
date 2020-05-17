#!/bin/bash
#
# Author: Moises Tapia(equinockx)
# Author: Adan Vazquez
# Author: Dart - Security

clear
AUX=$(dpkg -s inspec | grep "Status: install ok installed")
echo "Espere un momento..."
sleep 2
echo "Descargando Inspec espere un momento ..."
sudo wget https://packages.chef.io/files/stable/inspec/4.18.111/debian/10/inspec_4.18.111-1_amd64.deb
clear 
echo "Instalando Inspec"
sleep 5
sudo dpkg -i inspec_4.18.111-1_amd64.deb
sleep 5
echo " "
echo " "
echo "Terminando"
clear
echo "Verificando instalacion"
echo $AUX
sleep 4
echo "Instalando nmap"
sudo apt-get install nmap -y
sleep 2
echo "Done"

