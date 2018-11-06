# from datetime import datetime
#
# import requests
# import json
#
# def get_all():
#     url='https://api-kovan.etherscan.io/api?module=account&action=tokentx&address=0x35ab109dc26bb5a68bbd4255dc4bb6660a6c8b0f'
#     res=requests.get(url).json()
#     gas=[int(x['gasPrice'])*int(x['gasUsed'])*pow(10,-18) for x in res['result'] if x['from']=='0x35ab109dc26bb5a68bbd4255dc4bb6660a6c8b0f']
#     print(sum(gas))
#     print(datetime.fromtimestamp(int(res['result'][0]['timeStamp'])))
#     print(res['result'])


#
# if __name__=='__main__':
#     get_all()

from qrcode import QRCode,constants



qr=QRCode(
    version=1,
    error_correction=constants.ERROR_CORRECT_L,
    box_size=10,
    border=4.
)
qr.add_data('http://www.baidu.com')
qr.make(fit=True)
img=qr.make_image()
print(img)
img.save('124.png')