if(ifconfig | grep 'wlp2s0')> /dev/null
then
 echo "network connection ok"
else
 echo "network connection failed"
fi
