for i in *; do
    if [ -f $i ]; then
        sed -i s/ascii/binary/g $i
    fi
done    
