SET VERSION=8.1.0.31237

:: TODO Verify prerequisits:
:: JDK >= 11     (run "java -version" to check)

:: Download sonarqube community
curl -O https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-%VERSION%.zip
tar -xf sonarqube-%VERSION%.zip
del sonarqube-%VERSION%.zip