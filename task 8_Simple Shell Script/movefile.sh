for f in *
do
 if [ -f "$f" ]
 then
 if ( less $f |grep 'linux' )
  then 
 mv $f ./linux_files/
  fi
fi
done
