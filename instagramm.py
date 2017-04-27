import requests
import json
import random
import re

def Inst(diez):
    try:
        r = requests.get("""https://www.instagram.com/explore/tags/{diez}/""".format(diez=diez))
        text = r.text.encode('utf-8')
        text = text.decode()
        i = 1
        text = text.split('\n')
        for element in text:
            if '<script type="text/javascript">window._sharedData =' in element:
                Dict = element[52:-10]
                Dict = json.loads(Dict)
                photoDict = []
                Dict = Dict["entry_data"]['TagPage'][0]['tag']['top_posts']['nodes']
                for x in Dict:
                    if x['is_video'] == True:
                       r =requests.get("""https://www.instagram.com/p/{code}""".format(code=x['code']))
                       text = r.text.encode('utf-8')
                       text = text.decode()
                       i = 1
                       text = text.split('\n')
                       for element in text:
                            if '<script type="text/javascript">window._sharedData =' in element:
                                Dict = element[52:-10]
                                Dict = json.loads(Dict)
                                videoUrl = Dict["entry_data"]['PostPage'][0]['media']['video_url']
                                videoComment = Dict["entry_data"]['PostPage'][0]['media']['caption']
                                photoDict.append(videoUrl+"||"+videoComment)
                    else:
                        photoDict.append(x['thumbnail_src']+"||"+x['caption'])
                b = random.randint(0, len(photoDict)-1)
                print(photoDict[b])
                return (photoDict[b])
    except Exception as e:
        return "Oooops, #{} - Not Found".format(diez)


#Inst('boobs')
