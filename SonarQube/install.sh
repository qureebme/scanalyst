#!/usr/bin/env bash

VERSION=8.1.0.31237

# TODO Verify prerequisits:
# JDK >= 11     (run "java --version" to check)

# Download sonarqube community
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-$VERSION.zip
unzip sonarqube-$VERSION.zip
rm sonarqube-$VERSION.zip 

# Download sonar-scanner
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873-linux.zip
unzip sonar-scanner-cli-4.2.0.1873-linux.zip
rm sonar-scanner-cli-4.2.0.1873-linux.zip
