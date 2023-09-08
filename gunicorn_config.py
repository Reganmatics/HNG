# gunicorn_config.py

# Bind to localhost and port 8000
bind = "127.0.0.1:8000"

# Specify the number of worker processes
workers = 4  # You can adjust this based on your system's resources

# Set the worker class for ASGI applications
worker_class = "uvicorn.workers.UvicornWorker"
