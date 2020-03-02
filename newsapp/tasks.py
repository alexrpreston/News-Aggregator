from celery import Celery

app = Celery('newsapp', broker='pyamqp://guest@localhost//')

@app.task
def add(x,y):
    return x + y