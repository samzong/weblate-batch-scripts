## weblate-batch-scripts

- batch create new components from another one.

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

- 确认配置是否生效  http://127.0.0.1:8000/test_config
- 执行批量添加     http://127.0.0.1:8000/batch_create_components