# serverdiff
Simple method for describing differences between directories.

A little beyond `diff` found in bash. This will detect different files **AND** shared files with different contents. A nice way to validate important data transfers.

Try running it on the example data:

`python compare.py -f server1 -s server2`

Output should look like this:

```
Shared file with different content test2.tsv found in server1 and server2
Common file test3.tsv found in server1 and server2
Common file test4.tsv found in server1 and server2
Common file test2.tsv found in server1 and server2
Shared file with different content test2.tsv found in server1/subserver and server2/subserver
Common file test2.tsv found in server1/subserver and server2/subserver
Shared file with different content subsubfile.txt found in server1/subserver/subsubserver and server2/subserver/subsubserver
Common file subsubfile.txt found in server1/subserver/subsubserver and server2/subserver/subsubserver
```
