# SEM Project

A static code analyser that can use SonarQube, CheckStyle or PMD to find errors in any commit of a Java project repository and put them in csv files

Authors:

- Qureeb Hameed
- Gabriel Jorge
- Henrik Sillanpää
- Alexis Vanhalle	

## Installation

First:
    In /SonarQube/sonarscannerfolder and /SonarQube/sonarscannerfolder, replace /home/qureeb/Documents/TUT/SEM/ in the paths to the corresponding directory on your PC
    
Then:
    Run this in a terminal (in the same directory as this file)
    ./install.sh

## Usage

Run this in a terminal (in the same directory as this file)
python3 main.py <url-to-your-repo> <code-analysis-tool>

code-analysis-tool is one of pmd, sonar, or checkstyle


