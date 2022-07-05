import time
from celery_tasks.mytask.tasks import seed

r = seed.delay()
# celery -A celery_tasks.main worker --pool=solo -l info
time.sleep(3)
print(r.result, r.status)
from celery.result import AsyncResult
