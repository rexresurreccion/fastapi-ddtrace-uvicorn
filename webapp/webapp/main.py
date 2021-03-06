import logging
import requests
import time
import os

from pythonjsonlogger import jsonlogger
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')

logHandler = logging.FileHandler(filename='/var/log/webapp/python/log.log')
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] %(message)s')
logHandler.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(logHandler)
log.setLevel(logging.DEBUG)


def write_notification():
    log.info("Testing Background Task", extra={"client_id": "1123"})
    response = requests.get(f"http://ec2-11-111-111-11.us-east-2.compute.amazonaws.com:8081/?timestamp={time.time()}")


@app.get("/")
async def root(background_tasks: BackgroundTasks):
    webapp = {"webapp": "Hello World"}
    log.debug("DD Env", extra={"ENVS": os.environ})
    log.info("Happy DD Logging!", extra={"client_id": "1123"})
    log.debug("Debug mode loggging", extra={"client_id": "1123"})
    log.error("Houston we have a problem", extra={"client_id": "1123"})
    background_tasks.add_task(write_notification)
    return webapp


