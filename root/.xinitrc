#!/bin/bash

# disable blanking
setxkbmap fi
xset s off
xset -dpms

uzbl-core --geometry=maximize -u $(<~/homepage.url)
