from celery import Celery

# 生成celery应用
celery_app = Celery("caicai")
# 加载配置文件
celery_app.config_from_object('celery_tasks.config')
# 注册任务
celery_app.autodiscover_tasks(['celery_tasks.mytask'])  #
