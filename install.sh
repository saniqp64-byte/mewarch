#!/bin/bash
./bin/install.sh
./configs/install.sh

cp -r Pictures ~/

mkdir ~/.themes
cp -r theme/Simple-Tokyo-Night.zip ~/.themes
unzip ~/.themes/Simple-Tokyo-Night.zip -d ~/.themes