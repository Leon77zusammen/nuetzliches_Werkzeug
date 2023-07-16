from urllib import robotparser
import requests

web_list = [
"https://scjgj.sh.gov.cn",
"http://cyds.shtic.com",
"https://www.ndrc.gov.cn",
"https://www.miit.gov.cn",
"https://zwgk.mct.gov.cn",
# "https://www.most.gov.cn",
"https://www.nosta.gov.cn",
"https://www.cac.gov.cn",
# "https://www.wenming.cn",
"https://www.isc.org.cn",
"https://www.acftu.org",
"https://www.shzgh.org",
"https://www.12371.cn",
"https://www.taobao.com",
"https://fgw.sh.gov.cn",
"https://whlyj.sh.gov.cn",
"https://sww.sh.gov.cn",
"https://stcsm.sh.gov.cn",
"https://www.sheitc.sh.gov.cn",
"https://sfj.sh.gov.cn",
# "http://www.shccio.com",
"https://sipa.sh.gov.cn",
"http://218.78.53.157:90",
"http://whzf.whlyj.sh.gov.cn"
]

def check_robots_valid(web_url):

    rp = robotparser.RobotFileParser()
    rp.set_url(web_url + "/robots.txt")
    rp.read()
    # can_fetch = rp.can_fetch("*", web_url + "/some_page.html")
    can_fetch = rp.can_fetch("*", web_url)
    x = requests.get(web_url + "/robots.txt")
    # print(can_fetch, web_url)
    text = x.text
    if "Disallow" in text:
        result = True
    else:
        result = False
    print("have aggrement:{}, status_code:{}, can_fetch:{}, web_url:{}".format(result, x.status_code, can_fetch, web_url))
    # print("have aggrement:{}, status_code:{}, web_url:{}".format(result, x.status_code, web_url))

for web in web_list:
    check_robots_valid(web)
