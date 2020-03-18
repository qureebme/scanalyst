#!/usr/bin/env bash

# Installs CheckStyle

VERSION=8.30

# Asks the user if he wants to install checkstyle
read -r -p "Do you want to install CheckStyle (No if you already have it)? [Y/n] " response
response=${response:l} #tolower

if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]
then

    # Installs CheckStyle
    echo "Installing CheckStyle..."
    wget https://github.com/checkstyle/checkstyle/releases/download/checkstyle-$VERSION/checkstyle-$VERSION-all.jar

    # Gives the program the location of the server and the scanner
    echo "$PWD/checkstyle-$VERSION-all.jar" > checkstyle-jar-location

else

    # If the user already has CheckStyle installed, asks him the location
    read -r -p "Absolute location of the CheckStyle jar (Example: \"/home/user/checkstyle.jar\")
    " response
    echo $response > checkstyle-jar-location

fi
