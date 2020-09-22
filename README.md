# asms
automobile-sales-management-system 汽车销售管理系统 Python Vue

[中文版README](README_CN.md)
# Brief Introduction
This is a simple Web project designed to cope with Python course design: **front-end separation + cloud container deployment**.

# Main Technology Stack
Front-End：Vue  ElementUI  D2Admin<br>
Back-End：Python   Flask   MySQL<br>
Deploy：docker & docker-compose

# Main Function
1. View all available automobile information and sell them;<br>
2. Display all unsold car information, and provide the function of deleting and modifying information;<br>
3. Input car information;<br>
4. View details of all sold cars;<br>
5. Provide some after-sales analysis data, such as car type analysis.<br>

# What Is Needed
A Linux server with Docker & Docker-Compose.

# How To Use
```
git clone https://github.com/ZhaoHengheng123-star/asms.git
```
Modify the `commit` as `optimize js code` for all the `IP`s in the JS file (public network IP):
```javascript
var api = "http://IP:5000/getinfo";
      Axios.post(api, JSON.stringify({ gettype: 0 }), {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Accept: "application/json"
        }
      })
```

```
docker-compose up -d
```
<br><br>
If it helps you, please give a star support author.
