#!/bin/sh

apk add --update

echo "     "
echo "     "
echo "installing python"
apk add python3

echo "     "
echo "     "
echo "installing pip"
apk add py-pip

echo "     "
echo "     "
echo "installing requests"
pip3 install requests;
echo "     "
echo "     "

export BASE_NAME=$(./gradlew printBaseName)

python3 "$WERCKER_STEP_ROOT/run.py"
