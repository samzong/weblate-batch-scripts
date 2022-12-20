# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

gitlab api docs: https://python-gitlab.readthedocs.io/en/stable/api-usage.html
git api docs: https://gitpython.readthedocs.io/en/stable/tutorial.html

"""
import os

import gitlab
from git import Repo

from config import Config

gl = gitlab.Gitlab(url=Config.GITLAB_URL, oauth_token=Config.GITLAB_PERSON_TOKEN)


def get_project_name(project_id):
    return gl.projects.get(project_id).name


def get_project_url(project_id):
    return gl.projects.get(project_id).http_url_to_repo


def get_project_clone_url(project_id):
    return gl.projects.get(project_id).http_url_to_repo.replace(Config.GITLAB_URL, Config.GITLAB_CLONE_URL)


def clone_project(project_id):
    branch_name = 'weblate'
    download_path = os.path.join('cache_repo/', get_project_name(project_id))

    Repo.clone_from(get_project_clone_url(project_id), to_path=download_path, branch=branch_name)

    return os.path.abspath(download_path)


def remove_clone_project(project_name):
    download_path = os.path.join('cache_repo/', project_name)
    if os.path.exists(download_path):
        os.system('rm -rf {}'.format(download_path))

    return "remove {} success".format(download_path)


def create_branch(project_id):
    branch_name = 'weblate'
    project = gl.projects.get(project_id)
    project.branches.create({'branch': branch_name, 'ref': 'master'})


def check_weblate_branch(project_id):
    branch_name = 'weblate'
    project = gl.projects.get(project_id)
    for branch in project.branches.list():
        if branch_name == branch.name:
            return True
    return False
