a=2
b=21
while [ $a -lt $b ]
do
	echo $a
	a=`expr $a '+' 1`
done
