# NJU-API

#### 希望能造福可爱的小开发者们...



### 地址

123.206.187.246:666

### 小百合
|               接口               |       说明       |  类型  |                   请求参数                   |
| :----------------------------: | :------------: | :--: | :--------------------------------------: |
|         /bbs/get_tabs          |     获取所有标签     | GET  |                    /                     |
|         /bbs/get_top10         |   获取校园十大文章列表   | GET  |                    /                     |
|    /bbs/get_bbs_board_top20    |   获取热门讨论区列表    | GET  |                    /                     |
|        /bbs/get_bbs_all        |    获取全部讨论区     | GET  |                    /                     |
|      /bbs/get_bbs_top_all      | 获取今日各区热门话题文章列表 | GET  |                    /                     |
|        /bbs/get_bbs_not        |     获取进版画面     | GET  |               board（板块名称）                |
| /bbs/get_article_list_by_board |   获取板块内文章列表    | GET  |           board（板块名称）、page（页数）           |
|      /bbs/search_article       |   搜索文章（未测试）    | POST | user（作者名称含有）、title（标题含有）、title2（标题含有2）、title_without（标题不含）、from_now_begin（距离现在a天）、from_now_end（到距离现在b天，a<=b） |

