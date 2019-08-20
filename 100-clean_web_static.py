#!/usr/bin/python3
""" This script generate .tgz from the contents of the web_static
"""
from fabric.api import local, run, cd, put, env


def do_pack():
    """ Create a tar gz file

    """
    local("mkdir -p ./versions")
    comp = local(
        "tar -cvzf versions/web_static_$(date '+%Y%m%d%H%M%S').tgz web_static")

    if (comp.succeeded):
        return local(
            "echo \"versions/web_static_$(date '+%Y%m%d%H%M%S').tgz\"",
            capture=True)
    else:
        return None


env.hosts = ['34.73.255.16', '34.74.104.239']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ unzip all files in the remote servers """
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


def deploy():
    """ Deploy new version """
    archive_path = do_pack()
    if archive_path:
        result = do_deploy(archive_path)
        return result
    else:
        return False


def do_clean(number=0):
    """ Clean directories """
    count = local("ls versions | wc -l", capture=True)
    r_dir = "/data/web_static/releases"
    r_count = run("ls /data/web_static/releases | wc -l")
    if int(number) <= 1:
        while (int(count) > 2):
            nm_file = local("ls -1tr versions | head -1", capture=True)
            local("rm versions/{}".format(nm_file))
            count = local("ls versions | wc -l", capture=True)
        while (int(r_count) > 2):
            nm_folder = run("ls -1tr {} | head -1".format(r_dir))
            run("sudo rm -rf {}/{}".format(r_dir, nm_folder))
            r_count = run("ls {} | wc -l".format(r_dir))
    else:
        while (int(count) > int(number)):
            nm_file = local("ls -1tr versions | head -1", capture=True)
            local("rm versions/{}".format(nm_file))
            count = local("ls versions | wc -l", capture=True)
        while (int(r_count) > int(number)):
            nm_folder = run("ls -1tr {} | head -1".format(r_dir))
            run("sudo rm -rf {}/{}".format(r_dir, nm_folder))
            r_count = run("ls {} | wc -l".format(r_dir))
