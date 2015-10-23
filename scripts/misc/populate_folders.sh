for i in $(ls -d */); do
    cp job_template/sixtrack_input/* ${i%%/}
done
