import logging

bind = "0.0.0.0:80"
workers = 1
worker_class = "uvicorn.workers.UvicornWorker"
errorlog = "-"
accesslog = "-"
loglevel = 'info'
capture_output = True