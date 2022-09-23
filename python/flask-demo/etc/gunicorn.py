import multiprocessing

bind = "0.0.0.0:5000"
workers = 1
threads = multiprocessing.cpu_count() * 2
worker_class = 'gevent'
backlog = 2048
pidfile = "@work_dir@/pid"
accesslog = "@log_dir@/info.log"
errorlog = "@log_dir@/debug.log"
timeout = 600
debug = False
