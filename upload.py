#!/bin/sh
#!/usr/bin/python

chmod +x merge.py 
./merge.py

git add .
git commit -m "upload"
git push