# weblate-batch-scripts

> 新增依赖安装

```bash
# poetry
poetry add wlc python-gitlab gitpython jinja2

# pip
pip3 install wlc python-gitlab gitpython jinja2
```

> 生成配置文件 `config.py`

请替换自己的 Key

```python
WEBLATE_API_URL = ""
WEBLATE_API_TOKEN = ""
GITLAB_URL = ""
GITLAB_PERSON_TOKEN = ''
GITLAB_CLONE_URL = "https://oauth2:xxxxxxxxxx@gitlab."
```

## run in k8s

提供了模板配置文件 [run_in_k8s.yaml](run_in_k8s.yaml)，直接 apply yaml 文件，即可完成应用的部署.

```bash
kubectl -n your_namespace apply -f run_in_k8s.yaml
```

> 增加新的 project ，**本次最大的更新部分**，只需要更新 configmap 即可完成项目更新

1. 修改 ConfigMap weblate-projects，完成配置文件更新 `kubectl edit cm weblate-projects`
2. 重启 weblate-batch-scripts pod，完成项目更新 `kubectl rollout restart deployment weblate-batch-scripts`

## 使用 docker 的方式运行

使用 Dockerfile 自行编译

## v0.2

- 支持根据一个前端仓库地址，自动化创建项目并同步所有组件
- 支持点击更新项目待翻译内容
    - 接口获取项目列表
    - 选择项目，通过 gitapi 来创建分支，同步最新的翻译进度
    - 同步全部部件的更新
- 页面展示对应的徽章

## v0.1

- batch create new components from another one.
- batch create new components from a template.

### Configure

1. clone translate project to local
2. find files in repo . like project_name`/src/locales/zh-CN/`
3. run `cp config.py.example config.py` and modify ProjectConfig class
4. find u API_TOKEN
   at `/account/profile`  ![](<img src='http://ipic-typora-samzong.oss-cn-qingdao.aliyuncs.com//uPic/IrmmXG.jpg?x-oss-process=image/resize,w_960,m_lfit' alt='resize,w_960,m_lfit'/>)

### Running

```shell
- pip install -r requirements.txt
- make serve
```

### Web

- 确认配置是否生效  <http://127.0.0.1:8000/test_config>
- 执行批量添加     <http://127.0.0.1:8000/batch_create_components>

### Feature

- 支持网页输入代码仓库
- 支持自动上传
