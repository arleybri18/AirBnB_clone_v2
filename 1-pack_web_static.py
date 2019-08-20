#!/usr/bin/python3
""" This script generate .tgz from the contents of the web_static
"""
from fabric.api import local


def do_pack():
    """ Create a tar gz file

    """
    local("mkdir -p ./versions")
    comp = local(
        "tar -cvzf versions/web_static_$(date '+%Y%m%d%H%M%S').tgz web_static")

    if (comp.succeeded):
        return local(
            "echo \"versions/web_static_$(date '+%Y%m%d%H%M%S').tgz\"")
    else:
        return None
