#!/bin/bash
echo "Starting Nginx log backup..."

DATE=$(date +%Y%m%d)

# 1. 用 sudo 权限把日志复制到 /tmp 临时目录
sudo cp /var/log/nginx/access.log /tmp/access.log

# 2. 关键一步！把复制出来的文件所有权改成你自己
sudo chown computer-user:computer-user /tmp/access.log

# 3. 用普通用户权限打包（这样就绝对不会再有 root 权限问题了）
tar -czf /home/computer-user/access_log_$DATE.tar.gz /tmp/access.log

# 4. 删掉临时文件
rm -f /tmp/access.log

echo "Backup completed! File: access_log_$DATE.tar.gz"

# 5. 清理旧备份（现在旧备份是你自己的了，可以正常删除了）
ls -t /home/computer-user/access_log_*.tar.gz | tail -n +2 | xargs rm -f

echo "Old backups cleaned up."
