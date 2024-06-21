#!/usr/bin/3
from scrypt.utils.thread import set_thread_available

from scrypt.myapp import init_app

set_thread_available(1)

print('Start ' + __name__)

app = init_app()











