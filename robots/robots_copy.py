from urllib import robotparser
import requests

# web_list = [
# "https://scjgj.sh.gov.cn/1170/",
# "http://cyds.shtic.com/index.php?r=notice/index",
# "https://www.ndrc.gov.cn/xxgk/",
# "https://www.miit.gov.cn/search/wjfb.html?websiteid=110000000000000&pg=&p=&tpl=14&category=51&q=",
# "https://zwgk.mct.gov.cn/zfxxgkml/503/510/index_3081.html",
# # "https://www.most.gov.cn/index.html",
# "https://www.nosta.gov.cn/web/list.aspx?menuID=25",
# "http://www.cac.gov.cn/zcfg/gfxwj/A090905index_1.htm",
# "http://www.cac.gov.cn/zcfg/zcwj/A090906index_1.htm",
# "http://www.cac.gov.cn/zcfg/xzfg/A090902index_1.htm",
# "http://www.cac.gov.cn/zcfg/bmgz/A090903index_1.htm",
# # "http://www.wenming.cn/wmsjk/zcwj_53730/",
# "https://www.isc.org.cn/category/7429.html",
# "https://www.acftu.org/wjzl/wjzlzcwj/?7OkeOa4k=qAcPcAc2m7RaUVGycpXSn2djSbNyxONdKxMvZA7eRk7qqWmPunixqAqqIG",
# "https://www.shzgh.org/ghwj/ghwj.html",
# "https://www.12371.cn/",
# "https://www.taobao.com/",
# "https://fgw.sh.gov.cn/fgw_zxxxgk/index.html",
# "https://whlyj.sh.gov.cn/jqxxgk/index.html",
# "https://sww.sh.gov.cn/zxxxgk/",
# "https://stcsm.sh.gov.cn/zwgk/zxgk/",
# # "https://www.sheitc.sh.gov.cn/zxgkxx/index.html",
# # "https://sfj.sh.gov.cn/2020zxgkxx/",
# # "http://www.shccio.com/home/policy",
# "https://sipa.sh.gov.cn/zwgk_zxxxgk/",
# "http://218.78.53.157:90/main.action",
# "http://whzf.whlyj.sh.gov.cn/info/main"
# ]

web_list = [
"https://scjgj.sh.gov.cn",
"http://cyds.shtic.com",
"https://www.ndrc.gov.cn",
"https://www.miit.gov.cn",
"https://zwgk.mct.gov.cn",
# "https://www.most.gov.cn",
"https://www.nosta.gov.cn",
"https://www.cac.gov.cn",
# "http://www.cac.gov.cn/zcfg/zcwj/A090906index_1.htm",
# "http://www.cac.gov.cn/zcfg/xzfg/A090902index_1.htm",
# "http://www.cac.gov.cn/zcfg/bmgz/A090903index_1.htm",
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

    # print("have aggrement:{}, status_code:{}, can_fetch:{}, web_url:{}".format(result, x.status_code, can_fetch, web_url))
    print("have aggrement:{}, status_code:{}, web_url:{}".format(result, x.status_code, web_url))


# check_robots_valid(web_list[0])
# check_robots_valid(web_list[-1])

for web in web_list:
    check_robots_valid(web)
