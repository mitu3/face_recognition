import requests
import sys
import base64





class face_shi:


    def __init__(self ):

        self.App_key = 'pRNGOcheobW841i7OeoExSpt'
        self.Secret_key = 'dDhLQvEWubNzOeugDRsnP8jiGc5eiWrM'
        self.access_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(self.App_key, self.Secret_key)
        self.add_url = 'https://aip.baidubce.com/rest/2.0/face/v2/faceset/user/add'
        self.recognition_url = "https://aip.baidubce.com/rest/2.0/face/v2/identify"




    def get_token(self):
        url = self.access_token_url
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        req = requests.get(url, headers=headers)
        return req.json()['access_token']



    def add_user(self, imgfile, uid, user_info, group_id, token):

        with open(imgfile, 'rb') as f:
            img = base64.b64encode(f.read())

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = {"group_id":group_id,"images": img ,
                  "uid": uid,"user_info":user_info}

        url = self.add_url + "?access_token=" + token

        req = requests.post(url, data=params, headers=headers)

        print(req.json())


    def recognition(self, imgfile, group_id, token):
        url = self.recognition_url + "?access_token=" + token


        with open(imgfile, 'rb') as f:
            img = base64.b64encode(f.read())

        params = {"face_top_num":"1","group_id": group_id,"images": img, "user_top_num": "1"}

        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}

        req = requests.post(url,data=params, headers=headers)
        print(req)

        return req.json()['result'][0]['user_info']












r = face_shi()
e = r.get_token()
imgfile = 'C:\\Users\\chufusheng\\Desktop\\test.jpg'
r.add_user( imgfile, '002', '刘亦菲', '003', e)
ee = r.recognition(imgfile, '003', e)
print(ee)

