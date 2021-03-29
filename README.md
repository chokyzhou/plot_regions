# plot_regions
Plot regions of one beatmap is favored by.

# load.py
简历一个load文件，包含id，secret用来获取token。
注：请不要泄露secret

from get_token import get_token
from lookup_beatmap import lookup_beatmap

def load():
    id = NULL
    secret = NULL
    grant_type = 'client_credentials'
    return id,secret,grant_type
