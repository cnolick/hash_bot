import requests
import json
import random
import sys


def Inst(diez):
    try:
        print('start')
        r = requests.get("""https://www.instagram.com/explore/tags/{diez}/""".format(diez=diez))
        text = r.text.encode('utf-8')
        text = text.decode()
        i = 1
        text = text.split('\n')
        for element in text:
            if '<script type="text/javascript">window._sharedData =' in element:
                Dict = element[63:-10]
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
                                Dict = element[63:-10]
                                Dict = json.loads(Dict)
                                #print(Dict)
                                videoUrl = Dict["entry_data"]['PostPage'][0]['graphql']['shortcode_media']['video_url']
                                #print(videoUrl)
                                videoComment = diez
                                #print(videoComment)
                                photoDict.append(videoUrl+"||"+videoComment)
                    else:
                        photoDict.append(x['thumbnail_src'] + "||" + x['caption'])
        b = random.randint(0, len(photoDict)-1)
        return (photoDict[b])
    except Exception as e:
        print("Unexpected error:", sys.exc_info()[0])
        return "Oooops, #{} - Not Found".format(diez)



print(Inst("boobs"))