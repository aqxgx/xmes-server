# xadmin-server

xadmin-基于Django+vue3的rbac权限管理系统

前端 [xadmin-client](https://github.com/nineaiyu/xadmin-client)

### 在线预览

[https://xadmin.dvcloud.xin/](https://xadmin.dvcloud.xin/)
账号密码：admin/admin123

## 开发部署文档

[https://docs.dvcloud.xin/](https://docs.dvcloud.xin/)

## [Centos 9 Stream 安装部署](https://docs.dvcloud.xin/guide/installation-local.html)
dnf install python3.12 python3.12-devel -y
dnf module switch-to postgresql:16 -y
dnf install postgresql-server -y
postgresql-setup --initdb
systemctl enable postgresql
echo -e '\n127.0.0.1 postgresql' >> /etc/hosts   # 用于添加postgresql本地解析
sed -i "/^host    all             all             127.0.0.1/d"  /var/lib/pgsql/data/pg_hba.conf
echo "host    all             all             127.0.0.1/32            md5" >> /var/lib/pgsql/data/pg_hba.conf
systemctl restart postgresql
su - postgres
cat <<EOF > create_and_permission.sql
-- 创建数据库
create database xadmin;

-- 创建用户并设置密码
CREATE USER server WITH PASSWORD 'KGzKjZpWBp4R4RSa';

-- 授予用户对数据库的所有权限
GRANT ALL PRIVILEGES ON DATABASE xadmin TO server;

-- 切换到xadmin数据库
\c xadmin;

-- 授予用户对 schema 的使用和创建权限
GRANT USAGE ON SCHEMA public TO server;
GRANT CREATE ON SCHEMA public TO server;

-- 授予用户对 schema 中现有对象（如表和序列）的权限
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO server;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO server;

-- 配置默认权限，确保未来创建的表和序列也授予用户权限
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO server;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO server;
EOF

psql -f create_and_permission.sql

exit
dnf module switch-to redis:7 -y
dnf install redis -y
echo -e '\nrequirepass nineven' >> /etc/redis/redis.conf   # 用于添加redis密码
echo -e '\n127.0.0.1 redis' >> /etc/hosts   # 用于添加redis本地解析
systemctl enable redis
systemctl restart redis
mkdir -pv /data/xadmin/
cd /data/xadmin/
python3.12 -m venv py312
dnf install git -y
cd /data/xadmin/
git clone https://github.com/aqxgx/xmes-server.git

sudo tee /etc/yum.repos.d/mariadb.repo <<'EOF'
[mariadb]
name = MariaDB
baseurl = https://mirrors.aliyun.com/mariadb/yum/10.11/rhel9-amd64
gpgkey = https://mirrors.aliyun.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck = 1
EOF
curl -sS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash
dnf install MariaDB-devel -y

source /data/xadmin/py312/bin/activate
pip install --upgrade pip
cd /data/xadmin/xadmin-server
pip install -r requirements.txt


## [Docker 容器化部署](https://docs.dvcloud.xin/guide/installation-docker.html)

# 附录

⚠️ Windows上面无法正常运行celery flower，导致任务监控无法正常使用，请使用Linux环境开发部署

## 启动程序(启动之前必须配置好Redis和数据库)

### A.一键执行命令【不支持windows平台，如果是Windows，请使用 手动执行命令】

```shell
python manage.py start all -d  # -d 参数是后台运行，如果去掉，则前台运行
```

### B.手动执行命令

#### 1.api服务

```shell
python manage.py runserver 0.0.0.0:8896
```

#### 2.定时任务

```shell
python -m celery -A server beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler --max-interval 60
python -m celery -A server worker -P threads -l INFO -c 10 -Q celery --heartbeat-interval 10 -n celery@%h --without-mingle
```

#### 3.任务监控[windows可能会异常]

```shell
python -m celery -A server flower -logging=info --url_prefix=api/flower --auto_refresh=False  --address=0.0.0.0 --port=5566
```

## 捐赠or鼓励

如果你觉得这个项目帮助到了你，你可以[star](https://github.com/nineaiyu/xadmin-server)表示鼓励，也可以帮作者买一杯果汁🍹表示鼓励。

| 微信                                                                                     | 支付宝                                                                                     |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <img src="http://qiniu.cdn.xadmin.dvcloud.xin/pay/wxpay.jpg" height="188" width="188"> | <img src="http://qiniu.cdn.xadmin.dvcloud.xin/pay/alipay.jpg" height="188" width="188"> |
