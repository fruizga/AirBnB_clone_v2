#!/usr/bin/python3

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os.path import exists
env.hosts = ["34.74.1.177", "35.227.127.123"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Deploy the web static to the server"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[1].split(".")[0]
        path = "/data/web_static/releases/{}".format(file_name)
        run("sudo mkdir -p {}/".format(path))
        run("sudo tar -zxf /tmp/{}.tgz -C {}/".format(file_name, path))
        run("sudo rm /tmp/{}".format(archive_path.split("/")[1]))
        run("sudo mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(file_name, file_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}\
        /data/web_static/current".format(file_name))
        print("New version deployed!")
        return True
    except Exception:
        return False
