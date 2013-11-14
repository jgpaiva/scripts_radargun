for i in `nova list | grep public | cut -d" " -f2`; do echo $i; nova delete $i; done
