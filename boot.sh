for i in {01..10} ; do nova boot --image "jgpaiva-clean" --flavor="4" m$i --availability-zone nova:node$i; sleep 5;  done
for i in {20..29} ; do nova boot --image "jgpaiva-clean" --flavor="4" m$i --availability-zone nova:node$i; sleep 5;  done

for i in {01..10} ; do nova boot --image "jgpaiva-clean" --flavor="4" m1$i --availability-zone nova:node$i;sleep 5;   done
for i in {20..29} ; do nova boot --image "jgpaiva-clean" --flavor="4" m1$i --availability-zone nova:node$i;sleep 5;   done
