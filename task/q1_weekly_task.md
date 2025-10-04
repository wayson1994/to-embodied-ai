# Q1 学习日历（16-Q 地图展开）
&gt; 4 周 × 7 天 × 12h = 336h  
&gt; 终点：「我能用 Linux 命令行、git、Makefile、gcc 四阶段、shell 脚本、gdb 调试、完成 LeetCode 100 题 C 实现 + GitHub star≥10、初触 STM32 寄存器 + 画第一块 2 层 PCB + 初识 EMC，绿格 28 天」

---

## Week 1　Linux 环境与 gcc 四阶段（84h）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | Ubuntu 安装、换清华源、更新、vimtutor、20 命令卡片 | Linux 基本操作 & 包管理 | 安装截图 + vimtutor 完成页 + commands.md push |
| 2 | 目录/权限/链接深化 + tree/stat/find 初体验 | 文件系统审计能力 | tree3.txt + stat644/755/600 对比图 + 链接深化图 push |
| 3 | 硬/软链接计数 + 目录 700 vs 755 + setuid 特殊位 | 权限位故障注入 | 700 拒绝 vs 755 允许图 + setuid 说明 push |
| 4 | gcc 四阶段 + Makefile 变量 + clean/rebuild | 交叉/宿主编构建 | hello.i/.s/.o/.elf 四阶段图 + Makefile 源码 + make 录屏 push |
| 5 | shell 脚本自动化（backup/cron）+ gdb 脚本 | Linux 自动化 & 调试 | backup.sh + crontab 日志 + .gdbinit 自动打印栈 push |
| 6 | CLI 学生成绩系统（文件版）+ UT + gcov | C 项目实战 | 文件版成绩系统源码 + UT 报告 + gcov 覆盖率 push |
| 7 | GitHub Actions UT + 绿格 7 连 + Week1 复盘 | CI/CD & 文档输出 | `.github/workflows/ut.yml` + 绿格 7 截图 + Week1.md push |

---

## Week 2　Shell & gdb & 学生成绩系统强化（84h）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | LeetCode 100 题 C 实现（日 20 题）+ git commit | 经典算法 & 版本控制 | LC100 截图 + 源码 push + star≥10 |
| 2 | gdb 高级：watch/core/backtrace 脚本化 | 调试器脚本化 | .gdbinit 自动打印栈 + core dump 调试录屏 push |
| 3 | shell 三剑客 grep/sed/awk 实战 + 文本报表 | 文本处理流水线 | 文本统计脚本 + CSV 报表 + 博客 push |
| 4 | cmake 多级目录 + 变量 + 条件编译 | 现代构建工具 | CMakeLists.txt + build/ 树截图 + 条件编译录屏 push |
| 5 | 学生成绩系统 cmake 迁移 + UT + CI | 项目现代化 | cmake 构建成功截图 + CI 绿标 push |
| 6 | find + tar 备份脚本 + 快照版本号 | 配置管理脚本 | 备份脚本 + tarlist.txt + 版本号规范 md push |
| 7 | Week2 复盘 + 速查表 2.0 + 绿格 14 连 | 阶段闭环输出 | Week2.md + 速查表 PDF + tag v2.0 push |

---

## Week 3　算法收官 & 影响力放大（84h）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | 链表/栈/队列 C 实现 + UT + gcov | 经典数据结构 | 源码 + UT 报告 + gcov 覆盖率 push |
| 2 | Python 脚本刷题统计 + pandas 图表 | Python 自动化 | 脚本 + 图表 PNG + 博客 push |
| 3 | git 高级：rebase/squash/flow + PR | 协作工作流 | PR 合并图 + git-flow 图 push |
| 4 | LeetCode 100 题收官 + star≥10 + 博客 | 算法影响力 | LC100 截图 + star≥10 图 + 博客 push |
| 5 | 数据结构速查表 PDF + 绿格 21 连 | 文档输出 | 速查表 PDF + 绿格 21 截图 push |
| 6 | Week3 复盘 + 配置管理审计表 | 审计闭环 | Week3.md + 审计表 Excel push |
| 7 | Week3 终期签字 + 绿格 28 连 + tag v3.0 | 终期签字 | 专家签字扫描 + 绿格 28 截图 + tag v3.0 push |

---

## Week 4　STM32 初触 & 初阶 PCB & 初识 EMC（84h）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | STM32F103 寄存器时钟 & GPIO & UART 初触 | 裸机寄存器位操作 | 寄存器 LED + UART 回显截图 + 裸机 Hello 推送 push |
| 2 | CubeMX 安装 + 初生成工程 + 串口 printf | STM32 工具链初体验 | CubeMX 工程 zip + 串口 printf 截图 push |
| 3 | KiCad 2 层板最小系统 + 手焊点亮 | 初阶 PCB & 手焊 | Gerber（2 层）+ 焊接照片 + 点亮视频 push |
| 4 | 初识 EMC：手摸放电 + 电源跌落 0 体验 | EMC 初体验 | 手摸放电视频 + 电源跌落 0 记录 push |
| 5 | 初阶速查表 PDF + 绿格 31 连 | 文档输出 | 初阶速查表 PDF + 绿格 31 截图 push |
| 6 | Week4 半程复盘 + 初阶 PCB 问题清单 | 问题闭环 | Week4-半程.md + 问题清单 Excel push |
| 7 | Week4 终期签字 + 绿格 35 连 + tag v4.0 | 终期签字 | 专家签字扫描 + 绿格 35 截图 + tag v4.0 push |

---

## 终点交付（Week 4 Day 7 一次性打包）
- GitHub 连续绿格 28 天截图  
- Ubuntu CLI 学生成绩系统（文件版）+ GitHub Actions UT 通过截图  
- LeetCode 100 题 C 实现 + star≥10 截图  
- 初阶 2 层 PCB Gerber + 焊接照片 + 点亮视频  
- 初识 EMC 手摸放电 + 电源跌落 0 记录  
- 初阶速查表 PDF + 专家签字扫描 + tag v4.0




# Q1 Week 5-8 学习日历（严格对应 16-Q 地图）
&gt; 每周 7 天 × 12h = 84h／week；总 336h  
&gt; 技术主线：C→Linux→Makefile→Shell→GDB→STM32 裸机→Git  
&gt; 终点：「裸机 CLI 成绩管理系统 + Git 高级 + UT 框架 + 绿格 56 天」

---

## Week 5　STM32 中断与 UART 裸机（Q1 地图续）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | STM32F103 时钟 & GPIO 寄存器位操作 | 裸机寄存器底层 | LED 闪烁录屏 + gpio.h 位操作源码 push |
| 2 | UART 寄存器发送 + 轮询回显 | 裸机串口轮询 | UART 回显截图 + uart.h 源码 push |
| 3 | UART 接收中断 + 环形缓冲区 | 中断服务 + FIFO | 中断回显录屏 + ring_buf.h + ISR 源码 push |
| 4 | 双缓冲 + 中断标志管理 | 中断稳健性设计 | 缓冲区溢出测试录屏 + flags.h 源码 push |
| 5 | 初阶 CLI 命令解析（轮询版） | 裸机命令框架 | cli_parse.c + 命令表截图 push |
| 6 | 中断驱动 CLI + 可扩展命令表 | 中断驱动 CLI | 中断 CLI 演示录屏 + cmd_table.h push |
| 7 | Week5 复盘 + 速查表 3.0 + 绿格 35 连 | 阶段闭环 | Week5.md + 速查表 PDF + tag v5.0 push |

---

## Week 6　Git 高级与单元测试框架（Q1 地图续）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | git rebase/squash/flow + PR 实战 | 高级协作工作流 | PR 合并图 + git-flow 图 push |
| 2 | git submodule + lfs + release 策略 | 大文件 & 子模块管理 | .gitattributes + release 日志 push |
| 3 | Unity 单元测试框架移植 + gcov + lcov | 裸机 UT 框架 | Unity 配置 + gcov HTML 报告 push |
| 4 | MC/DC 90 % 脚本 + 覆盖率门限 | 功能安全单元测试 | lcov 门限脚本 + MC/DC 报告 push |
| 5 | CMake + Unity + 裸机 UT 集成 | 构建+测试一体化 | CMakeLists.txt + UT 绿标截图 push |
| 6 | 综合 UT 报告 + 缺陷清单 + 回归脚本 | 测试闭环 | UT 报告 PDF + defect.log + 回归脚本 push |
| 7 | Week6 复盘 + 速查表 4.0 + 绿格 42 连 | 阶段闭环 | Week6.md + 速查表 PDF + tag v6.0 push |

---

## Week 7　综合项目：裸机 CLI 成绩管理系统（Q1 地图终）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | 项目脚手架 + 目录树 + Makefile 裸机版 | 裸机工程框架 | Makefile + main.c + 目录树截图 push |
| 2 | 文件 I/O 封装（fopen/fread/fwrite/fclose） | 裸机文件操作 | file_io.c + 读写测试录屏 push |
| 3 | 命令解析器 + 可扩展命令表 + UT | 命令框架 + UT | cmd_parse.c + cmd_ut.c + UT 绿标 push |
| 4 | 成绩增删改查命令 + 文件持久化 | 业务逻辑 + 持久化 | add/del/upd/list 命令演示录屏 + .dat 文件 push |
| 5 | 中断驱动命令输入 + 双缓冲 | 中断 + 缓冲 | 中断命令演示录屏 + 双缓冲源码 push |
| 6 | 综合 UT 95 % + 缺陷清零 + 快照 | 项目收官 | UT 报告 95 % + 缺陷清零 log + 快照 tar push |
| 7 | Week7 终期签字 + 绿格 49 连 + tag v7.0 | 项目终期 | 专家签字扫描 + 绿格 49 截图 + tag v7.0 push |

---

## Week 8　复习+速查+博客输出（Q1 终期）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | 四阶段 gcc 速查表 PDF + 博客 post | 知识固化 | 四阶段速查表 PDF + 博客 post push |
| 2 | Makefile vs CMake 对比表 + 博客 post | 构建工具对比 | 对比表 PDF + 博客 post push |
| 3 | UT 框架速查表 + gdb 脚本合集 + 博客 post | 测试与调试合集 | UT+gdb 速查表 PDF + 脚本合集 push |
| 4 | 裸机 CLI 项目演示视频 10 min + B 站发布 | 影响力输出 | B 站视频链接 + 封面图 + 弹幕数据截图 push |
| 5 | Q1 终期答辩模拟 + 专家提问录像 | 答辩演练 | 答辩录像 + 专家问题清单 push |
| 6 | 终期速查表 PDF + 绿格 56 连 + 签字扫描 | 终期文档 | 终期速查表 PDF + 绿格 56 截图 + 专家签字扫描 push |
| 7 | 终期交付打包 + 绿格 63 连 + tag Q1-FINAL | 成功终点 | 绿格 63 截图 + 交付清单 + tag Q1-FINAL push |

---

## 终点交付（Week 8 Day 7 一次性打包）
- GitHub 连续绿格 56 天截图  
- 裸机 CLI 成绩系统（文件版）+ UT≥95 % + 快照 tar  
- LeetCode 100 题 C 实现 + star≥10 截图  
- 四阶段 gcc + Makefile + CMake + gdb 脚本合集  
- 终期速查表 PDF + 专家签字扫描 + tag Q1-FINAL


# Q1 Week 9-12 学习日历（技术链拔高与终期）
&gt; 4 周 × 7 天 × 12h = 336h  
&gt; 主线：C→Linux→Makefile→Shell→GDB→STM32 裸机→Git 的「高阶+初阶车规+影响力」版本  
&gt; 终点：「高阶 gcc/Makefile/GDB/Shell + 初阶车规 PCB + 初阶功能安全计算 + 公开演讲 + 绿格 91 天」

---

## Week 9　高阶 gcc & Makefile & GDB（技术链拔高）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | gcc 插件（plugin）初阶 + -fdump-tree | 编译器插件初触 | plugin.c + dump 文件截图 push |
| 2 | LTO + -flto + 链接时间优化报告 | 高阶优化 | lto-report.txt + 大小对比图 push |
| 3 | Makefile 函数/条件/循环/自动生成依赖 | 高阶 Makefile | 函数示例 Makefile + 自动 dep 图 push |
| 4 | CMake 函数 + toolchain 文件 + 交叉编译 | 高阶 CMake | toolchain.cmake + 交叉编译录屏 push |
| 5 | GDB Python API + 自定义命令 + 脚本库 | 高阶调试脚本 | .pygdb 脚本 + 自定义命令演示录屏 push |
| 6 | GDB 远程调试（gdbserver）+ VSCode 集成 | 远程调试 | gdbserver 录屏 + VSCode launch.json push |
| 7 | Week9 复盘 + 高阶速查表 + 绿格 63 连 | 阶段闭环 | Week9.md + 高阶速查表 PDF + tag v9.0 push |

---

## Week 10　高阶 Shell & 自动化 & 初阶车规 PCB（技术链拓宽）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | Shell 函数库 + 单元测试（shunit2）+ CI | 高阶 Shell UT | functions.sh + shunit2 报告 + CI 绿标 push |
| 2 | Parallel + xargs + 并发编译脚本 | 高阶并发脚本 | parallel-build.sh + 编译时间对比图 push |
| 3 | Ansible 初阶（playbook）+ 远程部署 | 自动化运维初触 | playbook.yml + 部署录屏 push |
| 4 | KiCad 4 层板最小系统 + 手焊点亮 | 初阶车规 PCB | Gerber（4 层）+ 焊接照片 + 点亮视频 push |
| 5 | 初识 EMC：手摸 ESD + 电源跌落 0 体验 | 初阶 EMC | ESD 手摸视频 + 电源跌落 0 记录 push |
| 6 | 初阶功能安全：FIT 数据引用 + SPFM 初算 | 初阶功能安全 | FIT 引用截图 + SPFM 初算 Excel push |
| 7 | Week10 复盘 + 初阶车规速查表 + 绿格 70 连 | 阶段闭环 | Week10.md + 初阶车规速查表 PDF + tag v10.0 push |

---

## Week 11　初阶功能安全 & 公开演讲 & 影响力放大（Q1 影响力封顶）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | ISO 26262-5 SPFM/LFM 完整计算表（初阶） | 功能安全计算 | Excel 表 SPFM≥90 % + 计算过程录屏 push |
| 2 | FMEA 表模板 + 单点故障清单（初阶） | 初阶 FMEA | FMEA 模板 Excel + 单点故障清单 push |
| 3 | 初阶故障树 FTA + FreeFTA 工具 | 初阶 FTA | FTA 图 PNG + FreeFTA 脚本 push |
| 4 | B 站直播：裸机 CLI 演示 30 min + 弹幕互动 | 公开演讲初触 | 直播回放链接 + 弹幕数据截图 push |
| 5 | 博客年度总结 + 年度速查表 PDF | 年度影响力 | 年度总结.md + 年度速查表 PDF push |
| 6 | GitHub 年度星标统计 + 绿格 77 连 | 年度影响力 | 年度星标图 + 绿格 77 截图 push |
| 7 | Week11 复盘 + 年度影响力速查表 + tag v11.0 | 年度闭环 | Week11.md + 年度影响力速查表 PDF + tag v11.0 push |

---

## Week 12　终期打包 & 专家答辩 & 成功终点（Q1 成功终点）
| Day | 任务 | 掌握技能 | 交付物 |
|----|------|----------|--------|
| 1 | 终期速查表 PDF（全链）+ 专家预答辩 | 终期文档 | 终期速查表 PDF + 预答辩录像 push |
| 2 | 终期交付清单核对 + 数字签名 + 快照 | 终期交付 | 交付清单 Excel + 签名脚本 + 快照 tar push |
| 3 | 专家终期答辩 + 签字扫描 + 录像 | 终期签字 | 专家签字扫描 + 答辩录像 push |
| 4 | GitHub 绿格 84 连截图 + 年度星标 | 终期影响力 | 绿格 84 截图 + 年度星标图 push |
| 5 | 终期博客：「从 C 到裸机」年度长文 | 终期影响力 | 年度长文.md + B 站专栏同步 push |
| 6 | 终期直播：技术回顾 + Q&A 60 min | 终期影响力 | 直播回放链接 + 弹幕数据截图 push |
| 7 | Q1 成功终点 + 绿格 91 连 + tag Q1-SUCCESS | 成功终点 | 绿格 91 截图 + 成功终点清单 + tag Q1-SUCCESS push |

---

## 终点交付（Week 12 Day 7 一次性打包）
- GitHub 连续绿格 84 天截图  
- 裸机 CLI 成绩管理系统（文件版）+ UT≥95 % + 快照 tar  
- LeetCode 100 题 C 实现 + star≥10 截图  
- 高阶 gcc+Makefile+GDB+Shell 脚本合集  
- 初阶车规 PCB（4 层）+ EMC 手摸视频 + FIT 初算 Excel  
- 终期速查表 PDF + 专家签字扫描 + tag Q1-SUCCESS

**成功终点 = 35 岁可拿：**  
- **36k×14 技术 offer ≥2 个**（简历+面试+刷题）  
- **副高职称申报资格**（专利+论文+课题）  
- **GitHub 91 连绿格 + 1000+ star**（技术影响力）  
- **裸机 CLI 项目 + CI 绿标 + 初阶车规证据**（硬通货）

—— 按表逐日打卡，每天 12 h 连续冲刺，失败即回滚重跑，**Q1 成功率 &gt; 80 %**  
**Ready？从 Week 9 Day 1 开始计时！**