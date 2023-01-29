# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""
import logging

import requests
import json
import time
from config import Config
import wlc
from src.utils import get_files_from_dir

wb = wlc.Weblate(key=Config.WEBLATE_API_TOKEN, url=Config.WEBLATE_API_URL)


def add_component_addon(project, component):
    """
    - weblate.json.customize
    """
    json_addon_name = "weblate.json.customize"
    json_addon_configuration = {"sort_keys": False, "indent": 2, "style": "spaces"}

    resp = wb.post(path="components/{}/{}/addons/".format(project, component), name=json_addon_name,
                   configuration=json_addon_configuration)
    logging.info(resp)


def find_components(project_slug: str, component_slug: str):
    url = Config.WEBLATE_API_URL + "/components/{}/{}/".format(project_slug, component_slug)
    headers = {
        "Authorization": Config.WEBLATE_API_TOKEN,
        "Accept": "application/json, text/javascript",
        "Content-Type": "application/json"
        }

    response = requests.request("GET", url, headers=headers, allow_redirects=False, timeout=10)

    return response.json()


def create_first_component(project_slug, repo_url):
    branch = "weblate"
    repo = repo_url
    filemask = "src/locales/*/common.json"
    file_format = "json-nested"
    slug = name = "common"
    language_code_style = "bcp_long"
    template = "src/locales/zh-CN/common.json"
    vcs = "git"
    source_language = {
        "code": "zh-CN",
        "name": "中文(zh-CN)",
        }

    try:
        wb.create_component(project=project_slug,
                            repo=repo,
                            push=repo,
                            branch=branch,
                            push_branch=branch,
                            file_format=file_format,
                            filemask=filemask,
                            name=name,
                            slug=slug,
                            template=template,
                            vcs=vcs,
                            source_language=source_language,
                            language_code_style=language_code_style
                            )
        add_component_addon(project_slug, slug)
        logging.info("create first component success")
    except Exception as e:
        return e


def create_wb_project(name, url):
    try:
        if wb.get_project(name):
            return "项目已存在"
    except Exception as e:
        return wb.create_project(name=name, slug=name, website=url)


def sync_create_components(project_slug: str, repo: str, component_name: str, component_slug: str,
                           filemask: str, new_base: str):
    url = Config.WEBLATE_API_URL + "/projects/{}/components/".format(project_slug)

    payload = json.dumps({
        "file_format": "json-nested",
        "filemask": filemask,  # "src/locales/*/common.json"
        "name": component_name,
        "slug": component_slug,
        "repo": repo,
        "template": new_base,
        "new_base": "",  # new_base make null
        "vcs": "git",
        "language_code_style": "bcp_long",

        # add zh-CN source language
        "source_language": {
            "code": "zh-CN",
            "name": "中文(zh-CN)",
            },
        })

    headers = {
        "Authorization": Config.WEBLATE_API_TOKEN,
        "Accept": "application/json, text/javascript",
        "Content-Type": "application/json"
        }

    response = requests.request("POST", url, headers=headers, data=payload, allow_redirects=False, timeout=10)

    logging.info(response.text)

    return response.json()


def batch_create_components(project_slug, repo_path):
    dir_path = repo_path

    repo = "weblate://{}/common".format(project_slug)
    file_format = "json-nested"
    language_code_style = "bcp_long"
    vcs = "git"
    source_language = {
        "code": "zh-CN",
        "name": "中文(zh-CN)",
        }

    for file in get_files_from_dir(dir_path):
        component_name = component_slug = file.rstrip('.json').replace('/', '_')
        filemask = 'src/locales/*/' + file
        template = 'src/locales/zh-CN/' + file

        try:
            wb.create_component(project=project_slug, name=component_name, slug=component_slug, repo=repo,
                                filemask=filemask, template=template, file_format=file_format, vcs=vcs,
                                language_code_style=language_code_style, source_language=source_language)

            add_component_addon(project_slug, component_slug)

            print("Successfully to create component {}".format(component_name))
            time.sleep(0.2)

        except Exception as e:
            logging.error("Failed to create component {}".format(component_name))

    return "Successfully to create all components"
