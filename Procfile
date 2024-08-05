web: gunicorn task_scheduler.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn task_scheduler.wsgi