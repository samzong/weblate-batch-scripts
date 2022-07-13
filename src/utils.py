# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""
import logging
import os
import requests
from config import DaoConfig


def get_files_from_dir(dir_path: str):
    file_list = []
    if os.path.exists(dir_path):
        os.chdir(dir_path)
        for root, dirs, files in os.walk('.'):
            for name in files:
                file = os.path.join(root, name)
                if file.split('.')[-1] == 'json':
                    file_list.append(file.lstrip('./'))

        return file_list


def test_config():
    url = DaoConfig.WEBLATE_API_URL + '/'
    headers = {
        "Authorization": DaoConfig.WEBLATE_API_TOKEN,
        "Accept": "application/json, text/javascript",
        "Content-Type": "application/json"
        }

    response = requests.request("GET", url, headers=headers, allow_redirects=False, timeout=10)

    return response.json()
