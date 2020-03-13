#!/usr/bin/env bash

# Installs CheckStyle

VERSION=8.30

# TODO Verify prerequisits:
# JDK >= 11     (run "java --version" to check)

# Installs CheckStyle
wget https://github.com/checkstyle/checkstyle/releases/download/checkstyle-$VERSION/checkstyle-$VERSION-all.jar
