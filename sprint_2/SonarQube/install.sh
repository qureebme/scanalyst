#!/usr/bin/env bash

# Installs SonarQube

SERVER_VERSION=8.1.0.31237
SERVER_PATH=.
SCANNER_VERSION=4.2.0.1873-linux
SCANNER_PATH=.

# Asks the user if he wants to install sonarqube or if he already has it
read -r -p "Do you want to install SonarQube and Sonar Scanner (No if you already have it)? [Y/n] " response
response=${response:l} #tolower

if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]
then

    # Installs sonarqube and sonar-scanner
    echo "Installing SonarQube and Sonar Scanner..."
    
    # Installs sonarqube server
    wget -P $SERVER_PATH/ https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-$SERVER_VERSION.zip
    unzip $SERVER_PATH/sonarqube-$SERVER_VERSION.zip -d $SERVER_PATH/
    rm $SERVER_PATH/sonarqube-$SERVER_VERSION.zip 

    # Installs sonar scanner
    wget -P $SCANNER_PATH https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SCANNER_VERSION.zip
    unzip $SCANNER_PATH/sonar-scanner-cli-$SCANNER_VERSION.zip -d $SCANNER_PATH/
    rm $SCANNER_PATH/sonar-scanner-cli-$SCANNER_VERSION.zip

    # Gives the program the location of the server and the scanner
    echo "$PWD/$SERVER_PATH/sonarqube-$SERVER_VERSION" > sonarserver-folder
    echo "$PWD/$SCANNER_PATH/sonar-scanner-$SCANNER_VERSION" > sonarscanner-folder

else

    # If the user already has SonarQube installed, asks him the location
    read -r -p "Absolute location of SonarQube server (Example: \"/home/user/sonarqube-8.1.0.31237\")
    " response
    echo $response > sonarserver-folder
    read -r -p "Absolute location of Sonar Scanner (Example: \"/home/user/sonar-scanner-4.2.0.1873-linux\")
    " response
    echo $response > sonarscanner-folder

fi

# Creates a temporary folder
mkdir -p tmp
