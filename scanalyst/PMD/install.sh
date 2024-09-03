#!/usr/bin/env bash

# Installs PMD

VERSION=6.22.0

# Asks the user if he wants to install checkstyle
read -r -p "Do you want to install PMD (No if you already have it)? [Y/n] " response
response=${response:l} #tolower

if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]
then

    # Installs CheckStyle
    echo "Installing PMD..."
    wget https://github.com/pmd/pmd/releases/download/pmd_releases%2F$VERSION/pmd-bin-$VERSION.zip
    unzip pmd-bin-$VERSION.zip
    rm pmd-bin-$VERSION.zip

    # Gives the program the location of the server and the scanner
    echo "$PWD/pmd-bin-$VERSION/bin" > pmd-bin-location

else

    # If the user already has CheckStyle installed, asks him the location
    read -r -p "Absolute location of the PMD bin folder (Example: \"/home/user/PMD/bin\")
    " response
    echo $response > pmd-bin-location

fi
