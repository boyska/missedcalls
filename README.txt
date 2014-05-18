Just a scraper that stores in a DirSet.

To receive notifications, watch that directory some way.

Configuration
=============

Default conf is read from `defaultconf.json`. If you want to tweak, just make
another json file that contains a dictionary. The two files will be merged, so
the custom file can be a subset of the default one.

Credential file is very simple: first line contains the username, second line
contains the password. Subsequent lines are ignored.

Running
=======

`python leggi.py`
or
`python leggi.py /path/to/custom.json`
