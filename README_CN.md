# 简介
这是一个简单的为了应付Python课程设计的**前后端分离+云容器部署**的web项目。

# 主要技术栈
前端：Vue  ElementUI  D2Admin<br>
后端：Python   Flask   MySQL<br>
部署：docker & docker-compose

# 主要功能
1.查看所有可供销售的汽车信息并可售出；<br>
2.显示所有未售出汽车信息，并提供删除和修改信息的功能；<br>
3.录入汽车信息；<br>
4.查看所有已售出的汽车详细信息；<br>
5.并提供一些售后分析数据，比如汽车类型分析等。<br>

# 需要什么
一个带有docker&docker-compose的Linux服务器。

# 怎样使用
```
git clone https://github.com/ZhaoHengheng123-star/asms.git
```
根据实际情况修改`commit`为`optimize js code`的js文件中所有的`IP`（公网IP）：
```javascript
var api = "http://172.19.0.2:5000/getinfo";
      Axios.post(api, JSON.stringify({ gettype: 0 }), {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Accept: "application/json"
        }
      })
```

编排容器并启动：
```
docker-compose up -d
```
<br><br>
如果帮助到你，请给个star支持作者。