# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

from fastapi import FastAPI

import time
import os

from src.utils import get_files_from_dir, test_config
from src.components import create_components

from config import ProjectConfig

app = FastAPI(
    title="weblate-batch-scripts",
    version="0.0.1",
    terms_of_service="https://github.com/samzong/webalte-batch-scripts",
    contact={
        "name": "samzong",
        "url": "https://github.com/samzong",
        "email": "samzong.lu@gmail.com",
        },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        }
    )


@app.get("/")
async def root():
    return {"message": "Hi Man ~"}


@app.get("/test_config")
async def test_test():
    return test_config()


@app.get("/batch_create_components")
async def batch_create_components():
    project_slug = ProjectConfig.project_slug
    repo = ProjectConfig.repo
    filemask_pre = ProjectConfig.filemask_pre
    new_base_pre = ProjectConfig.new_base_pre
    dir_path = ProjectConfig.dir_path
    language_code_style = ProjectConfig.language_code_style

    for file in get_files_from_dir(dir_path):
        if os.platform == 'darwin':
            component_name = component_slug = file.rstrip('.json').replace('\\', '_')
            filemask = filemask_pre + file.replace('\\', '/')
            new_base = new_base_pre + file.replace('\\', '/')
        elif os.platform == 'win':
            component_name = component_slug = file.rstrip('.json').replace('/', '_')
            filemask = filemask_pre + file
            new_base = new_base_pre + file
        else:
            return {"message": "no support system!"}

        print("components_name: ", component_name)
        print("components_slug: ", component_slug)
        print("filemask: ", filemask)
        print("new_base: ", new_base)

        create_components(project_slug, repo, component_name, component_slug, filemask, new_base, language_code_style)

        # too hard. need sleep
        time.sleep(1)

    return {"message": "pls check components at weblate"}
