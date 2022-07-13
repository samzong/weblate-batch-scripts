# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import requests
import json
from config import DaoConfig


def create_components(project_slug: str, repo: str, component_name: str, component_slug: str, filemask: str,
                      new_base: str):
    url = DaoConfig.WEBLATE_API_URL + "/projects/{}/components/".format(project_slug)

    payload = json.dumps({
        "file_format": "json-nested",
        "filemask": filemask,  # "src/locales/*/common.json"
        "name": component_name,
        "slug": component_slug,
        "repo": repo,
        "template": "",
        "new_base": new_base,
        "vcs": "git"
        })

    headers = {
        "Authorization": DaoConfig.WEBLATE_API_TOKEN,
        "Accept": "application/json, text/javascript",
        "Content-Type": "application/json"
        }

    response = requests.request("POST", url, headers=headers, data=payload, allow_redirects=False, timeout=10)

    return response.json()


def find_components(project_slug: str, component_slug: str):
    url = DaoConfig.WEBLATE_API_URL + "/components/{}/{}/".format(project_slug, component_slug)
    headers = {
        "Authorization": DaoConfig.WEBLATE_API_TOKEN,
        "Accept": "application/json, text/javascript",
        "Content-Type": "application/json"
        }

    response = requests.request("GET", url, headers=headers, allow_redirects=False, timeout=10)

    return response.json()
