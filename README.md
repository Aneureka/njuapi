# NJU-API

<code>NJU-API</code> 的理想是尽可能编写和收集所有南大内容开发相关的接口，希望能为可爱的开发者们提供一个稳定的数据来源和后台保证。



## 使用方式

   * 试用：调用 http://www.aneureka.cn/api（可能有时候会挂😆）
   * 部署在自己的服务器上 



## 接口

### 小百合BBS

|         接口         |           说明           | 类型 |                             参数                             |                             示例                             |
| :------------------: | :----------------------: | :--: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    /bbs/sections     |       获取所有标签       | GET  |                              /                               |                              /                               |
|     /bbs/boards      |       获取全部板块       | GET  |                              /                               |                              /                               |
|  /bbs/boards/top20   |       获取热门板块       | GET  |                              /                               |                              /                               |
|   /bbs/boards/not    |       获取进板画面       | GET  |                       board：板块代号                        |               /bbs/boards/not?board=D_Physics                |
|    /bbs/articles     |   获取某篇文章具体内容   | GET  |         url：文章URL<br/>（URL需要先进行百分号编码）         | /bbs/articles?<br/>url=http://bbs.nju.edu.cn/bbstcon%3F<br/>board%3DV_Suggestions<br/>%26file%3DM.1537578669.A |
|    /bbs/articles     |      获取板块内文章      | GET  |     board：板块代号<br/>pages：需要获取的文章页数，可选      |          /bbs/articles?<br/>board=D_Physics&pages=2          |
|  /bbs/articles/hot   | 获取今日各区热门话题文章 | GET  |                              /                               |                              /                               |
| /bbs/articles/top10  |     获取校园十大文章     | GET  |                              /                               |                              /                               |
| /bbs/articles/search |         搜索文章         | GET  | user：作者名字关键词，可选<br/>keyword：标题关键词，可选<br/>days_from_now：多少天以内，可选 | /bbs/articles/search?<br/>user=Hiki&keyword=Handsome<br/>&days_from_now=7 |



## 部署

1. <code>git clone git@github.com:Aneureka/njuapi.git</code>
2. <code>cd</code> 到项目目录下， <code>virtualenv venv</code>在项目目录下创建一个python虚拟环境（python3.6，如果没有该命令的话先安装）
3. 安装所需要的依赖包：<code>pip install -r requirements</code>
4. 将 <code>start.sh.default</code> 和 <code>instance/config.py.default</code> 的 <code>.default</code> 去掉，你也可以自己添加一些环境变量或配置
5. 修改 <code>start.sh</code> 中的一些参数，执行！

