import random

import redis

redis_client=redis.StrictRedis(host='localhost',port=6379,db=1)

def generate_email_code(email):
    code=random.randrange(100000,999999)
    redis_client.set(email,code)
    return code
def get_email_info(email):
    code=redis_client.get(email)
    code=int(code.decode())
    return code
def del_email_code(email):
    redis_client.delete(email)
def generate_sms_code(sms):
    code=random.randrange(100000,999999)
    redis_client.set(sms,code)
    return code
def get_sms_info(sms):
    code=redis_client.get(sms)
    code=int(code.decode())
    return code
def del_sms_code(sms):
    redis_client.delete(sms)