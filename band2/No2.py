import requests
import chardet
import re

def mydetect():
    res = requests.get("http://finance.sina.com.cn/roll/index.d.html?cid=56934&page=1")
    cs = chardet.detect(res.content)
    info = res.content.decode(cs['encoding'])
    result = re.findall("<a href=\"(.*?)\".*?>(.*?)</a>",info)
    for item in result:
        print(item)

def findword():
    info = "1d23dddffddfg7888ddddd88"
    result = re.findall("d{2,3}", info)
    for item in result:
        print(item)


def findhouse():
    info = '<div class="lists">\
										        	<div class="list"><a  class="lianjie"  href="https://fz.58.com/jianzhifwy/43661099699087x.shtml?tjfrom=jz_pc_bigcate__108671422209861806362676390__208662084789796864__tj__null__null__null__null__eyJyIjp7ImluZm9pZCI6IjQzNjYxMDk5Njk5MDg3Iiwic2xvdCI6IjE3NCIsInR5cGUiOiIxNDgiLCJzaWQiOiIxMDg2NzE0MjIyMDk4NjE4MDYzNjI2NzYzOTAifSwidCI6MSwidiI6MX0%3D" target="_blank"><h3>\
             	                	<span>最新</span>\
                    	                       			ktv服务员兼职</h3>\
                            		<p class="detail">\
                                			<span>连江-县城&nbsp;&nbsp;|&nbsp;&nbsp;服务员&nbsp;&nbsp;|&nbsp;&nbsp;8人看过</span></p>\
                            			<div class="bq">\
                            			                            			<span>营业执照</span>\
                            			                            			                            			<span>月结</span>\
\
                         </div>\
                      <div class="price"><span>15</span>元/小时</div>\
                    </a>\
         	</div>\
            	<div class="list"><a  class="lianjie"  href="https://fz.58.com/fachuandan/43651334817429x.shtml?tjfrom=jz_pc_bigcate__108671422209861806362676390__208662084789796864__tj__null__null__null__null__eyJyIjp7ImluZm9pZCI6IjQzNjUxMzM0ODE3NDI5Iiwic2xvdCI6IjE3NCIsInR5cGUiOiIxNDgiLCJzaWQiOiIxMDg2NzE0MjIyMDk4NjE4MDYzNjI2NzYzOTAifSwidCI6MSwidiI6MX0%3D" target="_blank"><h3>\
             	                	<span>最新</span>\
                    	                       			聘兼职工作220</h3>\
                            		<p class="detail">\
                                			<span>福州-仓山&nbsp;&nbsp;|&nbsp;&nbsp;传单派发&nbsp;&nbsp;|&nbsp;&nbsp;197人看过</span></p>\
                            			<div class="bq">\
                            			                            			<span>营业执照</span>\
                            			                            			                            			<span>日结</span>\
\
                         </div>\
                      <div class="price"><span>34</span>元/小时</div>\
                    </a>\
         	</div>'
    result = re.findall("<h3>.*?</span>(.*?)</h3>.*<div class=\"price\"><span>(.*)</span>元/小时</div>",info)
    for item in result:
        print(item)

if __name__ == '__main__':
    findhouse()