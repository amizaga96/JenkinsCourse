#/bin/bash

NAME=$1
REV_NAME=$(echo "$NAME" | rev)
CHAR_NAME=$(echo -n "$NAME" | wc -c)
IP=$(hostname -I | awk '{print $1}')
BUILD_DATE=$(date)
if [ "$NAME" = "Anonymous" ]
then
    echo "You didnt enter your name"
    echo "So I'll call you "$NAME""
    echo "But.. I know your IP: "$IP""
    echo "And you exicute this script in: "$BUILD_DATE""
    echo "Bye for now, and dont forget, Linux is the best!"
else
    echo "Hi you!"
    echo "Your name is: $NAME"
    echo "Your name in reversed: "$REV_NAME""
    echo "Characters number in your name: "$CHAR_NAME""
    echo "you exicute this script in: "$BUILD_DATE""
    echo "Bye for now, and dont forget, Linux is the best!"
fi
