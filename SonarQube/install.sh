#!/usr/bin/env bash

# Installs SonarQube

SERVER_VERSION=8.1.0.31237
SERVER_PATH=.
SCANNER_VERSION=4.2.0.1873-linux
SCANNER_PATH=.

# TODO Verify prerequisits:
# JDK >= 11     (run "java --version" to check)

# Installs sonarqube server
wget -P $SERVER_PATH/ https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-$SERVER_VERSION.zip
unzip $SERVER_PATH/sonarqube-$SERVER_VERSION.zip -d $SERVER_PATH/
rm $SERVER_PATH/sonarqube-$SERVER_VERSION.zip 

# Installs sonar scanner
wget -P $SCANNER_PATH https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SCANNER_VERSION.zip
unzip $SCANNER_PATH/sonar-scanner-cli-$SCANNER_VERSION.zip -d $SCANNER_PATH/
rm $SCANNER_PATH/sonar-scanner-cli-$SCANNER_VERSION.zip
