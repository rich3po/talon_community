#!/bin/bash

restart_dragon () {
        DRAGON_PID=`ps -ax | grep Dragon.app | grep -v "grep" | awk '{print $1}' | xargs`
        echo Dragon PID: $DRAGON_PID
        TALON_PID=`ps -ax | grep Talon.app | grep -v "grep" | awk '{print $1}' | xargs`
        echo Talon PID: $TALON_PID
        if [ -z "$DRAGON_PID" ]
        then
                echo Dragon not running!
        else
                echo Killing Dragon...
                kill -9 $DRAGON_PID
        fi
        if [ -z "$TALON_PID" ]
        then
                echo Talon not running!
        else
                echo Killing Talon...
                kill -9 $TALON_PID
        fi
        echo Restarting...
        sleep 2
        open /Applications/Dragon.app
        open /Applications/Talon.app
        echo "BOOM :)"
}
