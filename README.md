# ESXI Update Discord Notify
Checks ESXI update page every so often and notifies a Discord channel when one is found.

I just added this to my user crontab.
(This can be obscenely improved, but 15 minutes and it's worked for months.)
```
0  8 * * * cd /home/kiro/git/esxi-update-notify && ./venv/bin/python3 ./check.py
```
