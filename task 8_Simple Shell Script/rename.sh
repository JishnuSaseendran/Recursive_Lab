for f in *
do
    if [ -f $f ]; then 
        echo "$f" | tr 'A-Z' 'a-z' >/dev/null
    fi
done
