# NJU-API

<code>NJU-API</code> 是尽可能编写和收集所有南大开发相关的内容，希望至少能为可爱的开发者们提供一个思路（比如正则和内容的筛选），也期待更多基于此的小程序或App的出现 ☺️

如果你有希望加入的内容源或接口改进的建议，欢迎ISSUE或邮件告诉我哟！



## 使用方式

   * 接口地址（丐中丐服务器）：http://www.aneureka.cn/api
   * 部署在自己的服务器上，部署方式和步骤见下面的说明。



## 接口

### 小百合BBS

所有的标签 <code>GET</code> http://www.aneureka.cn/api/bbs/sections

```json
{
	code: 0,
	sections: [
		"本站系统",
		"南京大学",
		"乡情校谊",
		"电脑技术",
		"学术科学",
		"文化艺术",
		"体育娱乐",
		"感性休闲",
		"新闻信息",
		"百合广角",
		"校务信箱",
		"社团群体"
	]
}
```

全部板块 <code>GET</code> http://www.aneureka.cn/api/bbs/boards

热门板块 <code>GET</code> http://www.aneureka.cn/api/bbs/boards/top20

```json
{
	code: 0,
	boards: [
		{
			seq: "1",
			url: "http://bbs.nju.edu.cn/bbsdoc?board=1937_12_13",
			board: "1937_12_13",
			type: "社科",
			description: "南京大屠杀",
			moderator: "诚征版主中"
		},
		{
			seq: "2",
			url: "http://bbs.nju.edu.cn/bbsdoc?board=7th_Art",
			board: "7th_Art",
			type: "艺术",
			description: "第七艺术",
			moderator: "诚征版主中"
		},
		{
			seq: "6",
			url: "http://bbs.nju.edu.cn/bbsdoc?board=Actuary",
			board: "Actuary",
			type: "学术",
			description: "保险精算",
			moderator: "诚征版主中"
		},
        ...
    ]
}
```

进版画面 <code>GET</code> http://www.aneureka.cn/api/bbs/boards/not?board=1937_12_13

（这里显示效果很丑嘤嘤嘤）

```
{
code: 0,
board_not: " 一切都成为历史了，历史更有必要为后人所知。 至于未来，那是我们现在要为之努力的。 ┌─────────────────────────┐ │┏━━━ ┏━╋┓ ━┳━ ┏┳┻┳┓ ┳┻━ �v━┓│ │┃━╋┓ ┗━╋┛ ┃┃ �u�u�v�v ┗┳━ ┓┏┛│ │┃ �u ┃ ━�u━ �u ┃�v ┏━━┓ ┃�v�u�v �u┃┃│ │/ [1;31m １９３７・１２・１３ [37m ┗┛│ │ │ │ 中 ━╋━ ━┻━ ┃ ┏━━┓ �v�u │ │ 华 ┃ ┏━┓ ┃ ┃━━┛ �u�v │ │ 儿 ┃━━━┃ ┗━┛ ━╋━ ┃━╋�u �u ┃ �v │ │ 女 ┃ �v�u ┃ ┃ ┃ ┃━�u━ ━╋━ │ │ 勿 ┃━┳━┃�u ┃�v �u ┃�u━┫ �u┃�v │ │ 忘 ┃━╋━┃ �v �u �v ┃┣━┫ �u �v �v │ │ │ └──────────────── BBS.NJU.EDU.CN ─┘ 遭�y者 遇难者 VICTIMS ３ ０ ０ ０ ０ ０ "
}
```

某个板块的帖子 <code>GET</code> http://www.aneureka.cn/api/bbs/articles?board=1937_12_13&pages=2

<code>pages</code> 可选参数，表示需要获取几页的帖子（时间从近到远）

```
{
	code: 0,
	articles: [
		{
			author: "aryan",
			time: "Aug 22 19:04",
			url: "bbstcon%3Fboard%3D1937_12_13%26file%3DM.1093172649.A",
			title: "○ 全球购买日货榜！2003年数据",
			reply: "641字节",
			hot: "9486"
		},
		{
			author: "Shelley",
			time: "Aug 24 21:22",
			url: "bbstcon%3Fboard%3D1937_12_13%26file%3DM.1093353745.A",
			title: "○ [转载] [授权转载] 关于二代身份证的制造公司",
			reply: "7.2K",
			hot: "5918"
		},
		{
			author: "woaixuexiao",
			time: "Aug 27 09:22",
			url: "bbstcon%3Fboard%3D1937_12_13%26file%3DM.1093569726.A",
			title: "○ （转载）浙大学子的抗日文化衫",
			reply: "463字节",
			hot: "7913"
		},
		...
	]
}
```

校园十大 <code>GET</code> http://www.aneureka.cn/api/bbs/articles/top10

```
{
	code: 0,
	articles: [
		{
			board: "Girls",
			url: "bbstcon%3Fboard%3DGirls%26file%3DM.1538485021.A",
			title: "这波房价上涨",
			author: "kaoya2010",
			follower: "16"
		},
		{
			board: "Pictures",
			url: "bbstcon%3Fboard%3DPictures%26file%3DM.1538536620.A",
			title: "【随拍】国庆节只有此景不堵",
			author: "mifengwang",
			follower: "6"
		},
		...
	]
}
```

今日各区热门话题文章 <code>GET</code> http://www.aneureka.cn/api/bbs/articles/hot

```
{
	code: 0,
	articles: [
		{
			url: "bbstcon%3Fboard%3DNJUExpress%26file%3DM.1538558289.A",
			title: "自行车被偷了",
			board: "NJUExpress"
		},
		{
			url: "bbstcon%3Fboard%3DGirls%26file%3DM.1538485021.A",
			title: "这波房价上涨",
			board: "Girls"
		},
		{
			url: "bbstcon%3Fboard%3DPictures%26file%3DM.1538488207.A",
			title: "对胃口好的女生很有好感",
			board: "Pictures"
		},
		...
	]
}
```

查看文章具体内容 <code>GET</code> http://www.aneureka.cn/api/bbs/articles?url=bbstcon%3Fboard%3DNJUExpress%26file%3DM.1538558289.A

```
{
	code: 0,
	discussion: [
	{
        author: "天元",
        board: "NJUExpress",
        title: "自行车被偷了",
        created_at: "Wed Oct 3 17:18:09 2018",
        content: "昨天晚上停在鼓楼南园四舍楼下车棚，今天下午就找不到了。附近地方也找过了，不会是停到别处记错了。用拇指粗细的锁锁着的，不过对于贼来说，恐怕再粗也没用吧。之前因为很多时候急用共享单车找不到，就买了车自己骑，不过没想到会被偷这个缺点。骑了一年了，这个车骑起来很省力，还是很喜欢这车的。感觉报警也没用，南京这么大，找回来的难度就像大海捞针。只能自认倒霉了吗？"
	},
	{
		author: "让真相飞一会",
		board: "NJUExpress",
		title: "Re: 自行车被偷了",
		created_at: "Wed Oct 3 17:35:05 2018",
		content: "你找个留学生帮你报案，准给你找回来"
	}
	]
}
```

搜索文章 <code>GET</code>  http://www.aneureka.cn/api/bbs/articles/search?author=deliver&keyword=ID&days=6

<code>author</code> 可选参数，文章作者ID

<code>keyword</code> 可选参数，关键词

<code>days</code> 可选参数，距离现在多少天

```
{
	code: 0,
	articles: [
		{
			author: "deliver",
			date: "Sep 28",
			url: "bbscon%3Fboard%3Dnotepad%26file%3DM.1538085603.A%26num%3D11994",
			title: "以下ID已于今日消逝在风中 [共27人]"
		},
		{
			author: "deliver",
			date: "Sep 29",
			url: "bbscon%3Fboard%3Dnotepad%26file%3DM.1538172002.A%26num%3D11995",
			title: "以下ID已于今日消逝在风中 [共27人]"
		},
		{
			author: "deliver",
			date: "Sep 30",
			url: "bbscon%3Fboard%3Dnotepad%26file%3DM.1538258403.A%26num%3D11996",
			title: "以下ID已于今日消逝在风中 [共22人]"
		},
		...
	]
}
```

```
可能发生的情况（等待十秒左右）
{
	code: 3003,
	err_msg: "The operation is too frequently. Try again later."
}
```



### 校务

登录 <code>POST</code> http://www.aneureka.cn/api/core/login

<code>Content-Type</code> application/x-www-form-urlencoded

<code>data</code> <code>{ username: '151xxxxxx', password: 'secret'}</code> [南京大学统一认证平台](http://cer.nju.edu.cn/amserver/UI/Login)的学号密码

登录获取 <code>token</code> 之后才能请求需要身份认证的内容

```
{
    code: 0,
    user_info: {
        sid: "151xxxxxx",
        name: "郭xx",
        phone: "131xxxx6787",
        email: "",
        gender: "1",
        department_id: "2xx",
        dormitory: "",
        groups: "bks"
    },
    token: "eyJpUGxhb...."
}
```

图书馆借书情况 <code>GET</code> http://www.aneureka.cn/api/core/book_borrow_info?token=eyJpUGxhbxxx

```
{
	code: 0,
	book_borrow_info: {
		accumulation: 45,
		max: 50,
		violation: 0,
		arrears: 0
	}
}
```

校园卡交易记录 <code>GET</code> http://www.aneureka.cn/api/core/trans_list?token=eyJpUGxhbxxx

```
{
	code: 0,
	trans_list: [
		{
			trans_time: "18-09-23 22:23",
			trans_name: "POS消费",
			amount: "-2.7",
			balance: 17.07,
			address: "鼓楼男浴室208"
		},
		{
			trans_time: "18-09-22 22:33",
			trans_name: "POS消费",
			amount: "-0.02",
			balance: 19.77,
			address: "鼓楼男浴室181"
		},
		{
			trans_time: "18-09-22 22:22",
			trans_name: "POS消费",
			amount: "-2.29",
			balance: 19.79,
			address: "鼓楼男浴室181"
		},
		...
	]
}
```

校园各部门办公电话 <code>GET</code> http://www.aneureka.cn/api/core/tel_book?department_id=102

<code>department_id</code> 部门ID，可选参数，可以由 <code>http://www.aneureka.cn/api/core/tel_book</code> 获得最根部的部门

```
{
	code: 0,
	tel_book: [
		{
			id: 102,
			name: "党委办公室"
		},
		{
			id: 1154,
			name: "校长办公室"
		},
		{
			id: 333,
			name: "纪委、监察处"
		},
		...
	]
}
```



## 部署

1. <code>git clone git@github\.com:Aneureka/njuapi.git</code>
2. <code>cd</code> 到项目目录下， <code>virtualenv venv</code>在项目目录下创建一个python虚拟环境（python3.6，如果没有该命令的话先安装）
3. 安装所需要的依赖包：<code>pip install -r requirements</code>
4. 将 <code>start.sh.default</code> 和 <code>instance/config.py.default</code> 的 <code>.default</code> 去掉，你也可以自己添加一些环境变量或配置
5. 修改 <code>start.sh</code> 中的一些参数，执行！

