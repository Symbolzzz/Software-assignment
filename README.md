# 财务管理系统

## 已实现：

1. 财务审计登录

5. 员工登录

8. 管理员登录
9. 管理员查找信息 
10. 管理员修改信息 
11. 管理员删除信息 
12. 管理员删库

**TODO**：

1. 财务审计阅读财务审计信息 

2. 财务审计筛选查找 
3. 财务审计详细信息查看

4. 员⼯查找 
5. 员⼯报账

## 项目目录

```
|—— sql     # 存放相关数据库sql语句

|—— static    # 存放静态资源文件

|—— |—— css   

|—— |—— images

|—— |—— js

|—— |—— lib

|—— templates  # 存放html文件

|—— |—— *.html

|—— utils    # 存放一些功能函数

|—— config.py

|—— main.py # 主函数
```

## 部署：

1. 进入/sql目录，将xey.sql导入本地；

2. 修改config.py：

   ```python
   config = {
       'default': Config,
       'MYSQL_PASSWORD': '3333', # 改成你的数据库密码
       'DATABASE_NAME': 'Finances'
   }
   ```

3. 安装库：

   ```
   pip install Flask
   ```

4. 运行main.py：

   ```
   python main.py
   ```

5. 在浏览器中打开localhost:5000。

数据库的数据还需要插入多一点，**管理员账号密码均为学号**；

员工和财务审计目前数据库中只插入我的信息：

```

账号：xxxxxx

密码：xxxxx

```
