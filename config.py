# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""


class Config(object):
    WEBLATE_API_URL = "https:weblate.org/api"
    WEBLATE_API_TOKEN = "Token $uToken"


class DaoConfig(Config):
    WEBLATE_API_URL = "http://10.6.229.10:8080/api"
    WEBLATE_API_TOKEN = "Token $uToken"


class ProjectConfig(Config):
    project_slug = 'mspider-ui'
    repo = 'weblate://mspider-ui/common'
    filemask_pre = 'src/locales/*/'
    new_base_pre = 'src/locales/zh-CN/'
    dir_path = '/mspider-ui/src/locales/zh-CN/'
