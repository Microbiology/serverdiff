# serverdiff
Simple method for describing differences between directories.

A little beyond `diff` found in bash. This will detect different files **AND** shared files with different contents. A nice way to validate important data transfers.

Try running it on the example data:

`python compare.py -f server1 -s server2`

Output should look like this:

```
Shared file with different content test2.tsv found in server1 and server2/
Directory server1 uniquely contains ['test1.tsv']
Directory server2/ uniquely contains ['test5.tsv']
Shared file with different content test2.tsv found in server1/subserver and server2/subserver
Directory server1/subserver uniquely contains ['test3.tsv', 'test4.tsv']
Shared file with different content subsubfile.txt found in server1/subserver/subsubserver and server2/subserver/subsubserver
```
