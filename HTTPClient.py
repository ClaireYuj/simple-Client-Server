# -*- coding = utf-8 -*-
# @Time : 2021/10/24 20:33
# @Author:Yu
# @File: HTTPClient.py
# @Software: PyCharm
import socket

host = "127.0.0.1"
port = 8500

# get the baidu request header
http_baidu_data = "GET /baidu.html HTTP/1.1\r\n \
                   Host: www.baidu.com\r\n \
                   Connection: keep-alive\r\n \
                   Cache-Control: max-age=0\r\n \
                   sec-ch-ua: 'Chromium';v='92', ' Not A;Brand';v='99', 'Google Chrome';v='92'\r\n \
                   sec-ch-ua-mobile: ?0\r\n \
                   Upgrade-Insecure-Requests: 1\r\n \
                   User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36\r\n \
                   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n \
                   Sec-Fetch-Site: none\r\n \
                   Sec-Fetch-Mode: navigate\r\n \
                   Sec-Fetch-User: ?1\r\n \
                   Sec-Fetch-Dest: document\r\n \
                   Accept-Encoding: gzip, deflate, br\r\n \
                   Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6\r\n \
                   Cookie: PSTM=1631087195; BD_UPN=12314753; BIDUPSID=E66112DB15348DDBE2D100D3A8970F44; __yjs_duid=1_c25e81e897da9f850dddaeb05eea48371631195019549; BDUSS=VuWjFGakxzLUQ2UjQ1bjljSEJEUmZzQUtDODlCaENUSmJSZFdBWFZob0ZzV0poRVFBQUFBJCQAAAAAAAAAAAEAAADNA2820rvR-dDEx-nQodPj19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUkO2EFJDthdX; BDUSS_BFESS=VuWjFGakxzLUQ2UjQ1bjljSEJEUmZzQUtDODlCaENUSmJSZFdBWFZob0ZzV0poRVFBQUFBJCQAAAAAAAAAAAEAAADNA2820rvR-dDEx-nQodPj19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUkO2EFJDthdX; BDSFRCVID_BFESS=81KOJeCAa6dnwmQHjimmhHXoOgKK0gOTH6HhZf-8kdApFdPVf0XQEG0PMx8g0KuMSJMcogKKymOTHuAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJAf_D-btC03fP36q4ofK4_WKUnh-I62aJ3R0nvvWJ5TMCo6bj5vD5-nM4882-v7yIO90hkEblcjShPC-tnGMUt1jGratJDt065vLPbm3l02Vb79e-t2ynLVjHLq24RMW238Wl7mWP5NsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjC5j5v-DaAOJjnE2I5b3RA8KJjEe-Kk-PnVeTvLyPnZKxJCKRcbWt3ELln8jJ6zMM7ihU4syP4jKMRnWnc7BUcDHCnOehjxQ4Om345QWbQ405OTB6-O0KJcbl66Ol6nhPJvynFDXnO7-xolXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtgDtVJO-KKCaMDDl3e; BAIDUID=45443A562A1AD0A3D8F3A02506EA09D4:FG=1; delPer=0; BD_CK_SAM=1; BAIDUID_BFESS=45443A562A1AD0A3D8F3A02506EA09D4:FG=1; BD_HOME=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; H_PS_645EC=98694BS4dRTaChr4CXGBHF3eUR1D%2BjkVmzRR7%2BUhgaV%2FDUW3YgX1EroCqPE; BDRCVFR[LjY4kjSi7r_]=mk3SLVN4HKm; H_PS_PSSID=35104_31253_35048_35064_34505_34917_34812_26350_34970_34868_35116; BA_HECTOR=81ag2l0104a00k0k4r1goqi210q\r\n\r\n"

def client(port):

    # initial the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client to the server
    s.connect((host, port))

    # send the request to get baidu_header to server
    s.sendall(http_baidu_data.encode("utf-8"))

    #get the response
    response_data = s.recv(1024)
    print(response_data)
    s.close()

if __name__ == "__main__":
    port = int(input("please input the post:")) # 8500
    client(port)



