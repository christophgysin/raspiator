#!/bin/bash

URLFILE=homepage.url

if [ ${QUERY_STRING} = reboot=reboot ]; then
   echo rebooting...
   reboot
   exit
fi

urldecode(){
  echo -e "$(sed 's/+/ /g;s/%\(..\)/\\x\1/g;')"
}

set_url=${QUERY_STRING#*url=}
set_url=$(echo ${set_url%%&*} | urldecode)

#[ $set_url ] && echo $set_url | urldecode > $URLFILE

url=$(<$URLFILE)

cat << EOF
<html>
<head><title>RasPI Radiator</title></head>
<body>
<h1>RasPI radiator</h1>

<pre>
$set_url
</pre>

<form>
<label for="url">URL:</label>
<input id="url" name="url" type="text" value="$(<$URLFILE)" size="60"></input>
<input type="submit" value="set URL"></input>
</form>
<form>
<input name="reboot" type="submit" value="reboot"></input>
</form>
</body>
</html>
EOF
