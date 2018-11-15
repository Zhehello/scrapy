# scrapy
实现，下载http://www.angelimg.com/该网站的所有的图片集

系统：centos 7
python版本：3.6

第一步安装 python
第二步安装 scrapy 使用 pip install scrapy

然后写一个spider继承CrawlSpider
图片使用管道进行下载，item文件定义两个类容，一个是图片url的保存，一个是下载图片管道时候需要的存放的变量
下载器需要去settings文件里面注册，img文件夹会自动生成

ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 300,
    #'angel.pipelines.AngelPipeline': 300,
}
IMAGES_STORE = 'img'

更管代理需要去middlewares中实现，我们写一个类实现process_request方法，再到对应的settings的下载中间件注册
import request,json,random,datetime
class AngelspiderProxyIPLoadMiddleware(object):
  def __init__(self):
    self.proxy = ""
    self.expire_datetime=datetime.datetime.now()-datetime.timedelta(minutes=1)
    #self._get_proxyip()    

  def _get_proxyip(self):
    f=open("proxy.txt")
    proxys= f.read().split("\n")
    p = random.sample(proxys,1)[0]
    print("proxy:",p)
    self.proxy = p
    self.expire_datetime = datetime.datetime.now()+datetime.timedelta(minutes=1)
 
  def _check_expire(self):
    if datetime.datetime.now() >= self.expire_datetime:
       self._get_proxyip()
       print("切换ip")

  def process_request(self,spider,request):
    self._check_expire()
    request.meta['proxy']="http://"+self.proxy
    

DOWNLOADER_MIDDLEWARES = {
    'angel.middlewares.AngelspiderProxyIPLoadMiddleware': 543
    #'angel.middlewares.AngelDownloaderMiddleware': 543,
}




