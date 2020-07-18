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
需要npm环境重新生成前端html文件；<br>
一个带有docker&docker-compose的Linux服务器。

# 怎样使用
```
git clone https://github.com/ZhaoHengheng123-star/asms.git
```
因为前端我没有使用nginx代理，所以前端接口是直接访问的服务器完全URL，也就是公网IP。所以需要修改前端访问`IP`，端口5000是Flask的默认端口。
```javascript
var api = "http://IP:5000/getinfo";
      Axios.post(api, JSON.stringify({ gettype: 0 }), {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Accept: "application/json"
        }
      })
```
因为前端文件使用`npm run build`生成，所以不太容易修改，我把前端的源码放在`demo`文件夹下，修改之后使用npm重新进行编译。

```
docker-compose up -d
```
<br><br>
如果帮助到你，请给个star支持作者。