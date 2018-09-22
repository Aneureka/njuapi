# NJU-API

<code>NJU-API</code> 的理想是尽可能编写和收集所有南大内容开发相关的接口，希望能为可爱的开发者们提供一个稳定的数据来源和后台保证。



## 使用方式

   * 直接调用 http://api.aneureka.cn （但毕竟服务器资源有限，可能不是很稳定）
   * 部署在自己的服务器上（推荐方式）



## 接口

### 小百合BBS

|         接口         |           说明           | 类型 |                             参数                             |                             示例                             |
| :------------------: | :----------------------: | :--: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    /bbs/sections     |       获取所有标签       | GET  |                              /                               |                              /                               |
|     /bbs/boards      |       获取全部板块       | GET  |                              /                               |                              /                               |
|  /bbs/boards/top20   |       获取热门板块       | GET  |                              /                               |                              /                               |
|   /bbs/boards/not    |       获取进板画面       | GET  |                       board：板块代号                        |               /bbs/boards/not?board=D_Physics                |
|    /bbs/articles     |   获取某篇文章具体内容   | GET  |           url：文章URL（URL需要先进行百分号编码）            | /bbs/articles?url=http://bbs.nju.edu.cn/bbstcon%3Fboard%3DV_Suggestions%26file%3DM.1537578669.A |
|    /bbs/articles     |      获取板块内文章      | GET  | board：板块代号； pages：需要获取的文章页数（一页有20+篇文章，从现在往前回溯），可选 |          /bbs/articles?<br/>board=D_Physics&pages=2          |
|  /bbs/articles/hot   | 获取今日各区热门话题文章 | GET  |                              /                               |                              /                               |
| /bbs/articles/top10  |     获取校园十大文章     | GET  |                              /                               |                              /                               |
| /bbs/articles/search |         搜索文章         | GET  | user：作者名字关键词，可选；keyword：标题关键词，可选；days_from_now：多少天以内，可选 | /bbs/articles/search?user=Hiki&keyword=handsome<br/>&days_from_now=7 |



## 部署

1. Clone 这份代码
2. 使用 <code>virtualenv</code>在项目目录下创建一个python虚拟环境（python3.6），
3. 安装所需要的依赖包：pip install -r requirements
4. 执行 run.py （推荐写一个运行脚本，提前设置环境变量）