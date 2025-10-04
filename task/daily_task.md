Week 1 & Week 2 每日细表（每天 3 大任务块，共 10 h，含具体步骤与交付物）
格式：Day-X　任务名　｜　任务内容（分步）　｜　交付物（必须可验）
────────── Week 1 ──────────
Day-1　Ubuntu 开发环境安装与终端入门
下载 Ubuntu 22.04 LTS → 用 Rufus 制作启动盘 → 物理机或 VM 安装（选英文目录）
换清华源 → 更新 sudo apt update && upgrade → 安装 build-essential gdb git vim curl
完成 vimtutor（25 min）→ 记录 20 条常用命令速记卡片
交付物：① 安装截图 4 张（磁盘分区/桌面/源列表/升级完成）② vimtutor 完成界面截图 ③ 命令卡片 markdown 推 GitHub
Day-2　Linux 文件系统与权限精讲
实操：mkdir ~/linux101 → 在里创建 3 级子目录 → touch/rm/mv/cp 各 10 次
权限实验：chmod 644/755/600 → 用 stat 查看 inode → 用 ls -l 解释每列
硬链接 vs 软链接：ln 硬链接计数观察；ln -s 相对路径软链接
交付物：① 目录树 tree 输出截图 ② stat 对比图 ③ 博客 Day-2.md（含命令记录）
Day-3　gcc 四阶段与 Makefile 初体验
写 hello.c → gcc -E -S -c -o 分步生成文件 → 用 file 命令查看类型
同一项目手写 Makefile（目标：hello）支持 clean/rebuild
加入变量 CC/CFLAGS，实现 -Wall -g 选项
交付物：① 四阶段中间文件截图 ② Makefile 源码 ③ make & ./hello 成功录屏 10 s
Day-4　gdb 调试基础实战
故意编写段错误程序 bad.c → gcc -g 编译 → gdb ./bad → backtrace → 定位行号
使用 tbreak/break/n/step/print 跟踪变量变化
保存 .gdbinit 自动打印栈
交付物：① gdb 会话文本 log（bt 结果）② .gdbinit 源码 ③ 调试过程 30 s 录屏
Day-5　git 本地与远程三板斧
git config --global 设置用户名/邮箱 → 初始化 linux101 仓库
添加 Day-1~4 所有 .md 与 Makefile → commit 消息遵循 Conventional Commits
GitHub 新建空仓库 → push 本地 master → 启用 README 自动渲染
交付物：① GitHub 仓库链接 ② commit 历史截图（≥4 条）③ .gitignore 示例文件
Day-6　Shell 脚本入门与自动化
写 backup.sh：tar + date 命名备份 ~/linux101 → 加入判断目录存在
赋可执行权限 → 运行一次 → 检查 tar 包完整性
用 cron -e 设定每日 02:00 执行，日志重定向 >> backup.log
交付物：① backup.sh 源码 ② tar -tf 查看截图 ③ crontab -l 截图 + 日志文件
Day-7　Week1 复盘与速查表输出
整理 6 天笔记 → 合并成 Week1.md → 画思维导图（XMind 或 draw.io）
导出 PDF 速查表 A4 双面（命令+快捷键+gdb 速查）
推 GitHub Release 打 tag v1.0，写 Release Note
交付物：① Week1.md ② PDF 速查表 ③ GitHub Release 截图
────────── Week 2 ──────────
Day-8　C 指针与内存管理强化
写 swap_int() 宏与函数双版本 → 用 gdb 观察地址变化
实现动态内存链表（增删改查）→ valgrind 检查无泄漏
博客图解指针与数组名区别
交付物：① list.c + valgrind 0 error 截图 ② 博客 Day-8.md ③ 代码推 GitHub
Day-9　Makefile 多级目录实战
把链表项目拆 src/include/build 三目录
手写 Makefile 支持自动找 .c→.o，可 make clean/make test
加入 -MMD 自动生成依赖，改动头文件后增量编译验证
交付物：① 目录 tree 截图 ② Makefile 源码 ③ make test 通过录屏
Day-10　gdb 高级技巧与脚本化
写 .gdbinit 自动设置 tbreak main → 打印链表长度变量 → continue
使用 watch 监控全局变量变化
生成 core dump → gdb ./a.out core 事后调试
交付物：① .gdbinit 源码 ② core dump 调试会话 log ③ 录屏 30 s
Day-11　Shell 文本处理三剑客
用 grep -E 找出所有 .c 文件中的 malloc → 统计次数
sed 批量把 printf 改为 LOG_DEBUG
awk 统计每个 .c 行数并输出报表
交付物：① 命令行结果截图 ② 脚本 tristat.sh ③ 报表 CSV 文件
Day-12　cmake 入门与迁移
把 Day-9 的 Makefile 项目改写 CMakeLists.txt
创建 build 文件夹 → cmake .. && make → 生成可执行文件
加入 option(BUILD_TEST) 条件编译测试
交付物：① CMakeLists.txt ② 构建成功截图 ③ build/ 下 tree 输出
Day-13　单元测试框架 Unity 移植
下载 Unity 源码 → 移植到 Day-9 项目
写 10 个链表 UT → 覆盖率 gcov ≥ 85 %
lcov 生成 html 报告 → 发布 GitHub Pages
交付物：① html 报告首页截图 ② coverage badge ③ GitHub Pages 链接
Day-14　Week2 总结与 Release
合并所有笔记 → Week2.md → 输出 PDF 速查表（cmake、gdb、sed/awk）
打 tag v2.0 → 写 Release Note 含覆盖率 badge
直播/录屏 5 min 演示：clone→cmake→make test→coverage 一键完成
交付物：① Week2.md ② PDF 速查表 ③ GitHub Release v2.0 截图 + 录屏链接
──────────
执行守则：
每日 22:30 前 commit & push，commit 消息格式：Day-X: 简短说明
日志写在 docs/dayX.md，截图放 docs/imgs/dayX/
每周日打 tag 并推送远程，保证绿格不间断。

