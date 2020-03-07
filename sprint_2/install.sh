#!/usr/bin/env bash

# Installs the whole program

# Checks if Python >= 3.0 is installed
echo "Checking Python version (>= 3.0 is needed)..."
PYV=`python3 -c '\
import sys;\
import platform;\
major, minor, patch = platform.python_version_tuple();\
sys.stdout.write("OK" if (int(major) >= 3 and int(minor) >= 0) else "");\
'`
# If the above command couldn't execute then PYV = ""
# If it executed but the version is less than 3.0 then PYV = ""
if [[ -z "$PYV" ]]
then
    echo "ERROR: Please install Python >= 3.0"
    exit 1
fi

# Checks if pip3 is installed
echo "Checking PIP3 installation..."
PIPV=`pip3 --version`
if [[ -z "$PIPV" ]]
then
    echo "ERROR: Please install PIP3 (Python3 package installer)"
    exit
fi

# Installs needed python modules
echo "Installing needed Python modules..."
pip3 install gitpython
pip3 install PyDriller

# Asks the user if he wants to install sonarqube or if he already has it
read -r -p "Do you want to install SonarQube and Sonar Scanner? [Y/n] " response
response=${response:l} #tolower
if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]
then
    # Installs sonarqube and sonar-scanner
    echo "Installing SonarQube and Sonar Scanner..."
    (cd SonarQube && ./install.sh)
else
    # If the user already has SonarQube installed, asks him the location
    read -r -p "Absolute location of SonarQube server (Example: \"/home/user/sonarqube-8.1.0.31237\")
    " response
    echo $response > SonarQube/sonarserver-folder
    read -r -p "Absolute location of Sonar Scanner (Example: \"/home/user/sonar-scanner-4.2.0.1873-linux\")
    " response
    echo $response > SonarQube/sonarscanner-folder
fi

# Creates a temporary folder
mkdir -p SonarQube/tmp

echo "-- Installation successful --"
