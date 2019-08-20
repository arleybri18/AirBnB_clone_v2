#!/usr/bin/python3
""" This script generate .tgz from the contents of the web_static
"""
from fabric.api import local, run, cd, put, env

env.hosts = ['34.73.255.16', '34.74.104.239']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    put("{}".format(archive_path), "/tmp/")
    with cd("/tmp"):
        nm_folder = archive_path[9:-4]
        current = "/data/web_static/current"
        r_path = "/data/web_static/releases/{}".format(nm_folder)
        run("mkdir -p {}".format(r_path))
        run("sudo tar -xzf {} -C {}".format(archive_path[9:], r_path))
        run("rm {}".format(archive_path[9:]))
        run("sudo mv {0}/web_static/* {0}".format(r_path))
        run("rm -rf {}".format(current))
        run("ln -s {} {}".format(r_path, current))
    result = run("ls {}".format(r_path))
    if result.succeeded:
        return True
    else:
        return False
