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

# Checks the Java version
echo "Checking Java version..."
JAVAV=$(java -version 2>&1 | sed -E -n 's/.* version "([^.-]*).*"/\1/p' | cut -d' ' -f1)
if [[ JAVAV -lt 11 ]]
then
    echo "ERROR: Please install JDK 11 or newer"
    exit
fi

# Installs the analysers
(cd SonarQube && ./install.sh)
(cd CheckStyle && ./install.sh)
# TODO PMD

echo "-- Installation successful --"
