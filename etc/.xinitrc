#!/bin/bash

# disable blanking
setxkbmap fi
xset s off
xset -dpms

~/cli-webkit/cli-webkit $(<~/homepage.url)
#arora $(<~/homepage.url)
