VERSION=8.1.0.31237

# TODO Verify prerequisits:
# JDK >= 11     (run "java --version" to check)

# Download sonarqube community
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-$VERSION.zip
unzip sonarqube-$VERSION.zip
rm sonarqube-$VERSION.zip 

# Starts the server
./start-server.sh
