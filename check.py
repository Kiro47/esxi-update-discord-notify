#!/usr/bin/env python3

import feedparser
import discord_notify
import os

URL="https://docs.vmware.com/en/VMware-vSphere/rn_rss.xml"
notify_URL="https://discord.com/api/webhooks/$GUILD_ID/$WEBHOOK_UUID"
feed = feedparser.parse(URL)

def get_last_update(path:str):
    """
    """
    if not os.path.exists(path):
        return None
    with open(path, "r") as last_checked:
        last = last_checked.read()
    return last

def new_update(new:str, path:str):
    """
    """
    with open(path, "w+") as last_checked:
        last_checked.truncate(0)
        last_checked.write(new)
    return

def notify(entry):
    """
    """
    msg = (
        "New ESXI Update:\n"
        f"Date updated: {entry.date}\n"
        "\n"
        f"{entry.link}\n"
        )

    notifier = discord_notify.Notifier(notify_URL)
    notifier.send(msg, print_message=True)

def compare(entry, path:str):
    """
    """
    new = entry.date
    old = get_last_update(path)

    if old != new:
        # Update file
        new_update(new, path)
        # Post
        notify(entry)
    return

entry = feed.entries[0]
compare(entry, "./last_checked")
