# -*- coding: utf-8 -*-
from decimal import Decimal
import random
# try something like

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    counter = 2
    while counter < num-1:
        if num%counter == 0:
            return False
        counter = counter + 1
    return True

def random_number():
    x = random.randint(2,1000)
    result = isPrime(x)
    return locals()

def request_object():
    app = request.application
    cntr = request.controller
    fx = request.function
    ext = request.extension
    folder = request.folder
    now = request.now
    client = request.client
    isSecure = request.is_https
    return locals()

def request_vars():
    num1 = 0
    num2 = 0
    total = 0
    if request.post_vars:
        num1 = Decimal(request.post_vars.num1)
        num2 = Decimal(request.post_vars.num2)
        total = num1 + num2
        response.flash = T('The total is ' + str(total))
    return locals()

def request_args():
    arg1 = Decimal(request.args(0))
    arg2 = Decimal(request.args(1))
    total = arg1 + arg2
    return locals()


def index(): 
    return dict(message="hello from basics.py")

def helloworld():
    msg = "Hello from the Controller!"
    return locals()
