from fastapi import FastAPI, Request
import os
import socket

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    hostname = socket.gethostname()
    ip_address = request.client.host
    author = os.getenv("AUTHOR", "Unknown")

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "author": author
    }
