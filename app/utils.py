import json

from app.constants.code import *


def build_result(code=SUCCESS, **kwargs):
    result = {'code': code}
    for k, v in kwargs.items():
        result[k] = v
    return json.dumps(result)


def build_url(host_url, **args):
    url = host_url
    if len(args) > 0:
        url += '?'
    arg_list = [str(k)+'='+str(v) for k,v in args.items()]
    url += "&".join(arg_list)
    return url


if __name__ == '__main__':
    pass
