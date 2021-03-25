from collections import Counter

import requests

# hyper param
base_url = "https://osu.ppy.sh/api/v2"

# returns beatmap preference by nations
def lookup_beatmap(token, beatmap_id = -1,):
    country_count = []
    count_count = []
    count_count_count = 0
    
    headers = {
        "Authorization": "Bearer " + token
    }
    
    r = requests.get(base_url+"/beatmapsets/{beatmap_id}".format(beatmap_id = beatmap_id) ,
                     headers = headers)
    
    if r.status_code == 200:
        about = r.json()
        recent_favourites = about['recent_favourites']
        for r in recent_favourites:
            country_count.append(r['country_code'])
            if r['country_code'] not in count_count:
                count_count_count += 1
                count_count.append(r['country_code'])
                
        country = sorted(country_count,key=Counter(country_count).get, reverse=True)
        bins = count_count_count*2 -1
        return country, bins
    


if __name__ == "__main__":
    token = ""
    lookup_beatmap(token, beatmap_id = -1)