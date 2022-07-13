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
    WEBLATE_API_TOKEN = "Token wlu_5cZxPaKhbn6JItFKUNPRxQt4Wu6qpShRkW7r"
