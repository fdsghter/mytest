from celery.result import AsyncResult
from celery_tasks.main import celery_app

res = AsyncResult("8a522eea-e17a-453d-9ab6-034064174fc4")  # 参数为task id
print(res.result)
