from get_token import get_token
from lookup_beatmap import lookup_beatmap
from load import load
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def calc(country,bins):
    print(country)
    plt.hist(country,bins = bins)
    plt.xlabel('Countries')
    plt.ylabel('Fav Count')
    plt.show()         


if __name__ == "__main__":
    beatmap_id = input('Enter Beatmap ID: ')
    id, secret, grant_type = load()
    token = get_token(grant_type = grant_type,id = id,secret = secret)
    country,bins = lookup_beatmap(token, beatmap_id = beatmap_id)
    calc(country,bins)