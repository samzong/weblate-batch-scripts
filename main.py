# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""
import logging
import os
import shutil

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.components import create_first_component, batch_create_components, create_wb_project
from src.daogit import get_project_name, check_weblate_branch, create_branch, clone_project, get_project_url, \
    get_project_clone_url, remove_clone_project

app = FastAPI(
    title="weblate-batch-scripts",
    version="0.0.2",
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

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = open("templates/home.html", 'r').read()
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/project_info/{project_id}")
async def project_info(request: Request, project_id: int):
    try:
        project_name = get_project_name(project_id)
        project_url = get_project_url(project_id)

        data = {
            "request": request,
            "project_id": project_id,
            "project_name": project_name,
            "message": "Project info {}".format(project_url)

            }

        return templates.TemplateResponse(name="project_info.html", context=data)
    except Exception as e:
        logging.error(e)
        data = {
            "request": request,
            "project_id": None,
            "project_name": None,
            "message": "404 Project Not Found"

            }
        return templates.TemplateResponse(name="project_info.html", context=data)


@app.get("/project_info/create_branch/{project_id}")
async def create_wb_branch(request: Request, project_id: int):
    project_name = get_project_name(project_id)
    if not check_weblate_branch(project_id):
        create_branch(project_id)
        logging.info(f'create branch weblate for project {project_name}')

        data = {
            "request": request,
            "project_id": project_id,
            "project_name": project_name,
            "message": "项目 weblate 分支创建成功"

            }

        return templates.TemplateResponse(name="project_info.html", context=data)
    else:
        data = {
            "request": request,
            "project_id": project_id,
            "project_name": project_name,
            "message": "项目 weblate 分支仍旧存在，请确认已完成合并后,删除分支,再次尝试刷新项目"

            }

        return templates.TemplateResponse(name="project_info.html", context=data)


@app.get("/project_info/clone_project/{project_id}")
async def clone_wb_project(request: Request, project_id: int):
    project_name = get_project_name(project_id)
    repo_path = clone_project(project_id)
    logging.info(f'clone project {project_name} to {repo_path}')

    data = {
        "request": request,
        "project_id": project_id,
        "project_name": project_name,
        "message": "Clone 项目成功，路径在 {}".format({repo_path})

        }

    return templates.TemplateResponse(name="project_info.html", context=data)


@app.get("/project_info/create_common_component/{project_id}")
async def create_common_component(request: Request, project_id: int):
    project_name = get_project_name(project_id)
    create_first_component(project_slug=project_name,
                           repo_url=get_project_clone_url(project_id))
    logging.info(f'create first component for project {project_name}')

    data = {
        "request": request,
        "project_id": project_id,
        "project_name": project_name,
        "message": "Common component 创建成功，现在可以创建其他组件"

        }

    return templates.TemplateResponse(name="project_info.html", context=data)


@app.get("/project_info/create_all_components/{project_id}")
async def create_all_components(request: Request, project_id: int):
    project_name = get_project_name(project_id)
    repo_path = os.path.abspath(os.path.join('cache_repo/', project_name))

    if not os.path.exists(repo_path):
        data = {
            "request": request,
            "project_id": project_id,
            "project_name": project_name,
            "message": "项目代码目前没有 Clone，请先点击 Clone 代码 到本地"

            }

        return templates.TemplateResponse(name="project_info.html", context=data)

    batch_create_components(
        project_slug=project_name,
        repo_path=os.path.join(repo_path, "src/locales/zh-CN/")
        )

    data = {
        "request": request,
        "project_id": project_id,
        "project_name": project_name,
        "message": "所有组件创建成功"

        }

    return templates.TemplateResponse(name="project_info.html", context=data)


@app.get("/project_info/create_wb_project/{project_id}")
async def wb_project(request: Request, project_id: int):
    project_name = get_project_name(project_id)
    project_url = get_project_url(project_id)

    resp = create_wb_project(name=project_name, url=project_url)

    data = {
        "request": request,
        "project_id": project_id,
        "project_name": project_name,
        "message": "weblate 项目创建成功，使用 gitlab 项目名称作为 web 项目名称\n{}".format(resp)

        }

    return templates.TemplateResponse(name="project_info.html", context=data)


@app.get("/project_info/remove_clone_file/{project_id}")
async def remove_clone_file(request: Request, project_id: int):
    project_name = get_project_name(project_id)

    resp = remove_clone_project(project_name)

    data = {
        "request": request,
        "project_id": project_id,
        "project_name": project_name,
        "message": "{}".format(resp)

        }

    return templates.TemplateResponse(name="project_info.html", context=data)
