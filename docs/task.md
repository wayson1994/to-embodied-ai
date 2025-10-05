| 序号   | 任务名称           | 任务细节                                       | 输入/输出                          | 交付物                         |
| ---- | -------------- | ------------------------------------------ | ------------------------------ | --------------------------- |
| 1-1  | 彩色 Hello       | 终端打印红色 Hello World                         | 无 → 红字                         | hello\_color.{c,cpp,py}     |
| 1-2  | 时间戳 Hello      | 打印带时间戳的 Hello                              | 无 → \[%Y-%m-%d %H:%M:%S] Hello | hello\_ts.{c,cpp,py}        |
| 1-3  | 刷新版 Hello      | 同一行每秒刷新计数 10 次                             | 无 → 动态计数                       | hello\_live.{c,cpp,py}      |
| 2-1  | 秒表 0-10 s      | 每隔 1 s 打印 elapsed                          | 无 → 10 行时间                     | stopwatch\_basic.{c,cpp,py} |
| 2-2  | 纳秒精度           | 使用 clock\_gettime/chrono/perf\_counter\_ns | 无 → ns 数字                      | stopwatch\_ns.{c,cpp,py}    |
| 2-3  | 多函数计时          | 测 memcpy/chunk\_copy 耗时                    | 1 MB → 耗时表                     | stopwatch\_funcs.{c,cpp,py} |
| 3-1  | 写日志文件          | 追加 100 行 INFO                              | 无 → app.log                    | log\_basic.{c,cpp,py}       |
| 3-2  | 轮转日志           | 超 1 kB 自动切割为 app.log.x                     | 循环写 → 多文件                      | log\_rotate.{c,cpp,py}      |
| 3-3  | 异步日志队列         | 生产者线程写，消费者刷盘                               | 双线程 → 无丢行                      | log\_async.{c,cpp,py}       |
| 4-1  | 数组版环 buf       | 64 int 环，push/pop                          | 命令行 → 空/满提示                    | ring\_basic.{c,cpp,py}      |
| 4-2  | 零拷贝读取          | 返回 span/memoryview 不复制                     | 写 1 k → 读 1 k                  | ring\_zero\_copy.{c,cpp,py} |
| 4-3  | MT 环 buf       | 多生产者/消费者锁-free                             | 线程 → 无冲突                       | ring\_mt.{c,cpp,py}         |
| 5-1  | 单线程 echo       | 最简阻塞 TCP 回显                                | telnet → 回显行                   | tcp\_echo\_basic.{c,cpp,py} |
| 5-2  | 多进程并发          | 每连接 fork()                                 | 100 连接 → 无串话                   | tcp\_echo\_fork.{c,cpp}     |
| 5-3  | 协程并发           | asyncio/asio 单线程                           | 100 连接 → 单线程                   | tcp\_echo\_coro.{cpp,py}    |
| 6-1  | assert 最小测试    | assert(add(2,2)==4)                        | 无 → PASS/FAIL                  | test\_minimal.{c,cpp,py}    |
| 6-2  | 框架测试           | Unity/Catch2/pytest 5 用例                   | 5 case → 绿色                    | test\_framework.{c,cpp,py}  |
| 6-3  | mock 测试        | mock 文件读/网络收                               | 假输入 → 真输出                      | test\_mock.{c,cpp,py}       |
| 7-1  | CI 一键过         | GitHub Actions 三语言编译                       | push → 绿 badge                 | .github/workflows/ci.yml    |
| 7-2  | 文档自动生成         | pydoc + doxygen + sphinx                   | 注释 → html                      | docs/                       |
| 7-3  | 周复盘视频          | 1 min 录屏展示亮点                               | 口述 → mp4                       | week1.mp4                   |
| 8-1  | 单线程下载          | wget 等价下载                                  | URL → 文件                       | dl\_single.{c,cpp,py}       |
| 8-2  | 进程池下载          | 4 进程并发                                     | URL 列表 → 4×速度                  | dl\_pool.{c,cpp,py}         |
| 8-3  | 断点续传           | Range 头支持续传                                | 半文件 → 完整文件                     | dl\_resume.{c,cpp,py}       |
| 9-1  | 共享内存写读         | 写 "Hello" → 读出来                            | 无 → Hello                      | shm\_basic.{c,cpp,py}       |
| 9-2  | 信号量同步          | 生产-消费 1 单元                                 | 交替 → 无竞争                       | shm\_sem.{c,cpp,py}         |
| 9-3  | 速率压测           | 1 GB 拷贝计时                                  | 1 GB → 带宽 MB/s                 | shm\_bench.{c,cpp,py}       |
| 10-1 | SIGINT 捕获      | Ctrl+C 打印优雅退出                              | ^C → 再见                        | signal\_int.{c,cpp,py}      |
| 10-2 | 信号屏蔽临界区        | sigprocmask 屏蔽 5 s                         | SIGUSR1 → 延迟处理                 | signal\_block.{c,cpp}       |
| 10-3 | 实时信号排队         | SIGRTMIN + 带数据                             | 发送指针 → 收到指针                    | signal\_rt.{c,cpp}          |
| 11-1 | sleep 循环       | 每秒打印 tick                                  | 10 s → 10 tick                 | timer\_sleep.{c,cpp,py}     |
| 11-2 | timerfd        | 1 ms 周期读取                                  | 无 → 1000 次/秒                   | timer\_fd.c                 |
| 11-3 | 并发定时池          | 10 个不同间隔回调                                 | 多线程 → 无漂移                      | timer\_pool.{c,cpp,py}      |
| 12-1 | 单向 pipe        | 父写子读                                       | 字符串 → 回显                       | pipe\_hello.{c,cpp,py}      |
| 12-2 | epoll LT       | 监听 pipe + 终端                               | 多 fd → 可读提示                    | epoll\_lt.c                 |
| 12-3 | epoll ET + 非阻塞 | 任意长度流                                      | 变长包 → 无阻塞                      | epoll\_et\_nb.c             |
| 13-1 | 手写解析           | 提取 { "name": "tom" }                       | JSON → tom                     | json\_minimal.{c,cpp,py}    |
| 13-2 | 库解析 + 绘图       | 解析复杂文件画饼图                                  | .json → .png                   | json\_plot.{cpp,py}         |
| 13-3 | 解析速率 PK        | 对比 cJSON / nlohmann / orjson               | 1 MB → ops/sec                 | json\_bench.{c,cpp,py}      |
| 14-1 | 覆盖率报告          | gcov + lcov + pytest-cov                   | 源码 → html                      | coverage/                   |
| 14-2 | pre-commit 钩子  | black/isort/cppcheck                       | commit → 0 warning             | .pre-commit-config.yaml     |
| 14-3 | 双周复盘视频         | 2 min 全任务闪回                                | 口述 → mp4                       | week2.mp4                   |
| 15-1 | 常量定义           | #define / const / enum                     | 无 → 打印常量                       | const\_demo.{c,cpp,py}      |
| 15-2 | 宏函数 VS inline  | 交换两数测耗时                                    | 100 万次 → 时间差                   | macro\_vs\_inline.{c,cpp}   |
| 15-3 | 条件编译           | #ifdef DEBUG 打印                            | 编译开关 → 不同行为                    | cond\_compile.{c,cpp}       |
| 16-1 | 位运算            | 置位/清位/取反                                   | hex → hex                      | bitmask.{c,cpp,py}          |
| 16-2 | 位段结构           | 控制 LED 3 色位段                               | 位段 → 状态                        | bit\_field.{c,cpp}          |
| 16-3 | 大小端探测          | union + 0x1234                             | 无 → Little/Big                 | endian\_detect.{c,cpp,py}   |
| 17-1 | 一维数组逆序         | reverse  inplace                           | arr\[] → 逆序                    | reverse\_arr.{c,cpp,py}     |
| 17-2 | 二维数组转置         | 行列交换                                       | mat → 转置                       | transpose.{c,cpp,py}        |
| 17-3 | 动态矩阵           | malloc/vector/list 二维                      | row,col → 矩阵                   | dyn\_mat.{c,cpp,py}         |
| 18-1 | 字符串长度          | 手写 strlen                                  | char\* → len                   | my\_strlen.{c,cpp,py}       |
| 18-2 | 字符串拷贝          | 手写 strcpy                                  | src → dst                      | my\_strcpy.{c,cpp,py}       |
| 18-3 | 字符串分割          | 手写 strtok                                  | "a,b,c" → \["a","b","c"]       | my\_strtok.{c,cpp,py}       |
| 19-1 | struct 学生      | 姓名+年龄                                      | 数据 → 打印                        | student.{c,cpp,py}          |
| 19-2 | struct 对齐      | 打印对齐后大小                                    | struct → size                  | align.{c,cpp}               |
| 19-3 | union 高低字节     | uint16 拆两 uint8                            | 0x1234 → 0x12 0x34             | union\_split.{c,cpp,py}     |
| 20-1 | 递归阶乘           | n! 递归                                      | 5 → 120                        | fact\_rec.{c,cpp,py}        |
| 20-2 | 递归汉诺塔          | 打印步骤                                       | n=3 → 步骤                       | hanoi\_rec.{c,cpp,py}       |
| 20-3 | 尾递归优化          | 对比耗时                                       | 1e6 → 时间差                      | tail\_rec.{c,cpp}           |
| 21-1 | 可变参数 sum       | va\_list 实现                                | 1,2,3 → 6                      | var\_sum.{c,cpp}            |
| 21-2 | 宏函数交换          | 宏实现 swap                                   | a,b → swapped                  | macro\_swap.{c,cpp}         |
| 21-3 | 内联函数对比         | inline vs 宏测速                              | 百万次 → 时间差                      | inline\_test.{c,cpp}        |
| 22-1 | const 指针       | const int \* vs int \* const               | 代码 → 编译错误                      | const\_ptr.{c,cpp}          |
| 22-2 | static 计数      | 函数调用计数                                     | 多次调用 → 计数                      | static\_cnt.{c,cpp}         |
| 22-3 | volatile 测试    | 防止优化 flag                                  | flag → 汇编可见                    | vola\_test.{c,cpp}          |
| 23-1 | 文件读写           | fprintf/fscanf                             | text → 拷贝                      | file\_io.{c,cpp,py}         |
| 23-2 | 二进制读写          | fread/fwrite                               | bmp → dat                      | bin\_io.{c,cpp,py}          |
| 23-3 | 随机访问           | fseek/ftell                                | 任意偏移 → 数据                      | random\_access.{c,cpp,py}   |
| 24-1 | 逐行读取           | fgets/getline                              | .txt → 行列表                     | readline.{c,cpp,py}         |
| 24-2 | getline 自动扩容   | 任意长行                                       | 长行 → 无溢出                       | getline\_demo.{c,cpp}       |
| 24-3 | 日志 printf 封装   | vfprintf 可变参                               | fmt... → 文件                    | log\_printf.{c,cpp}         |
| 25-1 | Makefile 基础    | 多文件编译                                      | src/\*.c → main                | Makefile\_basic             |
| 25-2 | Makefile 变量    | 自动找源文件                                     | 增删源 → 免改                       | Makefile\_auto              |
| 25-3 | CMake 基础       | add\_executable + 子目录                      | CMakeLists.txt → build         | CMakeLists.txt              |
| 26-1 | 静态库            | ar rcs libmath.a                           | .o → .a                        | libmath.a                   |
| 26-2 | 动态库            | gcc -shared                                | .o → .so                       | libmath.so                  |
| 26-3 | 库链接测试          | 调静态/动态库                                    | main → 运行                      | link\_test.c                |
| 27-1 | 单链表创建          | 头插法                                        | n → 链表                         | slist\_create.{c,cpp,py}    |
| 27-2 | 单链表打印          | 遍历输出                                       | 链表 → 数据                        | slist\_print.{c,cpp,py}     |
| 27-3 | 单链表反转          | 迭代法                                        | 链表 → 反转                        | slist\_reverse.{c,cpp,py}   |
| 28-1 | 双链表创建          | 尾插法                                        | n → DList                      | dlist\_create.{c,cpp,py}    |
| 28-2 | 双链表遍历          | 前后向                                        | DList → 数据                     | dlist\_iter.{c,cpp,py}      |
| 28-3 | 双链表排序          | 插入排序                                       | DList → 有序                     | dlist\_sort.{c,cpp,py}      |
| 29-1 | 内存池固定块         | malloc 一次拆块                                | 块大小 → 池                        | mempool.c                   |
| 29-2 | 内存池对齐          | align 64B                                  | align → 加速                     | mempool\_align.c            |
| 29-3 | 内存泄漏检测         | 宏包裹 malloc                                 | 泄漏 → 行号                        | leak\_detector.c            |
| 30-1 | 环形缓冲区          | 生产者-消费者                                    | 速率 → 无丢包                       | ringbuf.c                   |
| 30-2 | 位图索引           | 位图管理空闲块                                    | 块号 → 0/1                       | bitmap.c                    |
| 30-3 | 状态机解析          | 串口协议解包                                     | 字节流 → 包                        | fsm\_parser.c               |
| 31-1 | CRC16 计算       | 查表法                                        | data\[] → crc                  | crc16.c                     |
| 31-2 | 串口 printf      | 重定向 UART                                   | printf → 串口                    | uart\_printf.c              |
| 31-3 | 高精度延时          | NOP 校准                                     | us → 波形                        | delay\_us.c                 |
| 32-1 | 看门狗演示          | 独立看门狗复位                                    | 溢出 → 复位                        | wdt\_demo.c                 |
| 32-2 | DMA 内存拷贝       | 寄存器级                                       | src → dst                      | dma\_copy.c                 |
| 32-3 | ADC 采样         | 连续转换                                       | 引脚 → 电压                        | adc\_demo.c                 |
| 33-1 | PWM 呼吸灯        | 占空比渐变                                      | 周期 → LED 渐变                    | pwm\_breathe.c              |
| 33-2 | PWM 输入捕获       | 测频率                                        | 方波 → Hz                        | pwm\_capture.c              |
| 33-3 | I2C 扫描         | 寄存器级                                       | 无 → 地址表                        | i2c\_scan.c                 |
| 34-1 | SPI 闪存 ID      | 读取 JEDEC ID                                | CS → ID                        | spi\_flash\_id.c            |
| 34-2 | CAN 发送         | 寄存器级                                       | ID+data → 波形                   | can\_send.c                 |
| 34-3 | RTC 日历         | 设置/读取                                      | 时间戳 → 日历                       | rtc\_demo.c                 |
| 35-1 | Bootloader 入口  | 向量表重映射                                     | 按键 → 跳 APP                     | bootloader.c                |
| 35-2 | OTA 升级         | YMODEM 协议                                  | .bin → Flash                   | ymodem\_ota.c               |
| 35-3 | 字体点阵           | 8×8 字母                                     | 字母 → 点阵                        | font8x8.c                   |
| 36-1 | 图片取模           | BMP→数组                                     | bmp → .h                       | bmp2array.c                 |
| 36-2 | 滑窗平均           | 温度滤波                                       | 采样值 → 滤波值                      | sliding\_avg.c              |
| 36-3 | 一阶 IIR         | 低通滤波                                       | 噪声 → 平滑                        | iir\_1st.c                  |
| 37-1 | PID 控制器        | 位置式                                        | 设定值 → PWM                      | pid\_pos.c                  |
| 37-2 | PID 调参工具       | 串口曲线                                       | Kp,Ki,Kd → 图像                  | pid\_tuner.c                |
| 37-3 | 轮速计算           | 编码器计数                                      | 脉冲 → RPM                       | speed\_encoder.c            |
| 38-1 | 电机闭环           | PID+编码器稳速                                  | 目标RPM → 稳速                     | motor闭环.c                   |
| 38-2 | 红外遥控           | NEC 解码                                     | IR 信号 → 键值                     | nec\_decode.c               |
| 38-3 | 超声波测距          | HC-SR04                                    | Echo → cm                      | hcsr04.c                    |
| 39-1 | 温度传感器          | DS18B20                                    | DQ → 温度                        | ds18b20.c                   |
| 39-2 | 角度传感器          | MPU6050                                    | I2C → 弧度                       | mpu6050.c                   |
| 39-3 | 气压传感器          | BMP280                                     | I2C → Pa                       | bmp280.c                    |
| 40-1 | 颜色识别           | TCS3200                                    | 频率 → RGB                       | tcs3200.c                   |
| 40-2 | 蜂鸣器音乐          | 音阶频率                                       | 简谱 → 音乐                        | buzzer\_music.c             |
| 40-3 | 按键消抖           | 状态机                                        | 按键 → 稳定                        | debounce.c                  |
| 41-1 | 长按/短按          | 计时区分                                       | 按键 → 事件                        | key\_event.c                |
| 41-2 | LED 流水         | GPIO 翻转                                    | 模式 → 流水                        | led\_flow\.c                |
| 41-3 | 七段数码管          | 动态扫描                                       | 数字 → 显示                        | seg7.c                      |
| 42-1 | LCD1602        | 并口驱动                                       | 字符串 → 显示                       | lcd1602.c                   |
| 42-2 | OLED 显示        | I2C 128×64                                 | 字符串 → 显示                       | oled\_i2c.c                 |
| 42-3 | 触摸按键           | TTP223                                     | Touch → 键值                     | ttp223.c                    |
| 43-1 | 舵机控制           | PWM 20ms                                   | 角度 → 舵机                        | servo.c                     |
| 43-2 | 步进电机           | 四相八拍                                       | 步数 → 转动                        | stepper.c                   |
| 43-3 | 智能小车           | 直线+转弯                                      | 速度 → 动作                        | smart\_car.c                |
| 44-1 | 电子时钟           | RTC+LCD                                    | 无 → 时间显示                       | clock\_lcd.c                |
| 44-2 | 数据记录           | CSV 存储                                     | 传感器 → .csv                     | data\_logger.c              |
| 44-3 | 串口 CLI         | 命令解析                                       | 串口 → 应答                        | cli\_uart.c                 |
| 45-1 | 蓝牙透传           | HC-05                                      | 蓝牙 → 串口                        | bt\_pass.c                  |
| 45-2 | Wi-Fi 透传       | ESP8266 AT                                 | AT → 数据                        | wifi\_esp.c                 |
| 45-3 | JSON 生成        | 手写打印机                                      | 结构体 → JSON                     | json\_print.c               |
| 46-1 | JSON 解析        | 手写解析器                                      | JSON → 结构体                     | json\_parse.c               |
| 46-2 | Base64 编码      | 手写实现                                       | 二进制 → ASCII                    | base64.c                    |
| 46-3 | AES-128 ECB    | 手写加密                                       | 明文 → 密文                        | aes128.c                    |
| 47-1 | 随机数生成          | LFSR                                       | 种子 → 序列                        | lfsr.c                      |
| 47-2 | 软件定时器          | 多回调                                        | ms → 标志                        | soft\_timer.c               |
| 47-3 | 事件总线           | 订阅发布                                       | 事件 → 回调                        | event\_bus.c                |
| 48-1 | 消息队列           | FIFO 队列                                    | 消息 → 处理                        | msg\_queue.c                |
| 48-2 | 信号量            | 计数信号量                                      | take/release → 计数              | semaphore.c                 |
| 48-3 | 互斥锁            | 临界区                                        | lock/unlock → 安全               | mutex.c                     |
| 49-1 | 软件看门狗          | 多任务监视                                      | 心跳 → 复位                        | sw\_wdt.c                   |
| 49-2 | 链式回调           | 回调链表                                       | 注册 → 调用                        | callback\_chain.c           |
| 49-3 | 表驱动法           | 状态跳转表                                      | 状态 → 动作                        | table\_drive.c              |
| 50-1 | 单元测试框架         | Unity 集成                                   | test → PASS/FAIL               | unity\_test.c               |
| 50-2 | 性能剖析           | 分段计时                                       | 函数 → 耗时                        | profile.c                   |
| 50-3 | 代码覆盖率          | gcov 集成                                    | .c → .gcov                     | coverage.sh                 |
| 51-1 | 静态分析           | cppcheck                                   | .c → 报告                        | static.sh                   |
| 51-2 | Git Hook       | pre-commit 格式检查                            | 提交 → 提示                        | pre-commit                  |
| 51-3 | CMake 基础       | 多文件编译                                      | src/\*.c → main                | CMakeLists.txt              |
| 52-1 | CMake 测试       | add\_test                                  | test → PASS                    | CTest                       |
| 52-2 | Docker 镜像      | 编译环境容器化                                    | Dockerfile → 镜像                | Dockerfile                  |
| 52-3 | 交叉编译           | arm-linux-gcc                              | .c → ARM elf                   | cross.cmake                 |
| 53-1 | OOP 封装         | 结构体+函数指针                                   | 思想 → .c/.h                     | oop\_demo.c                 |
| 53-2 | 继承模拟           | 结构体嵌套                                      | 基类 → 派生类                       | inherit.c                   |
| 53-3 | 多态模拟           | 函数指针表                                      | 基类指针 → 派生行为                    | polymorph.c                 |
| 54-1 | 链表迭代器          | 封装 next                                    | 链表 → 迭代器                       | list\_iter.c                |
| 54-2 | 事件驱动           | 回调+循环                                      | 事件 → 处理                        | event\_loop.c               |
| 54-3 | 综合大作业          | FaceCSV 完整项目                               | .jpg → labels.csv              | 交付物①完成                      |
| 55-1 | 内存映射文件         | mmap 修改大文件原地                               | 1 GB → 修改后                     | mmap\_rewrite.c             |
| 55-2 | 映射匿名页          | MAP\_ANONYMOUS 大页                          | 2 MB → 地址                      | mmap\_anon.c                |
| 55-3 | 文件锁            | fcntl 记录锁多进程写                              | 偏移 → 无损坏                       | flock\_record.c             |
| 56-1 | exec 族         | execlp/execv 替换自身                          | 参数 → 新程序                       | my\_exec.c                  |
| 56-2 | fork+exec 管道   | popen 等价实现                                 | 命令 → 结果串                       | fork\_exec\_pipe.c          |
| 56-3 | daemon 化       | 自写 daemon() 步骤                             | 前台 → 后台+sid                    | my\_daemon.c                |
| 57-1 | capset         | 降权删除 CAP\_NET\_RAW                         | root → 无权限                     | cap\_drop.c                 |
| 57-2 | prlimit        | 运行时改最大文件句柄                                 | 新值 → 生效                        | prlimit\_fd.c               |
| 57-3 | event 库封装      | 封装 epoll+timerfd 为 mini-lib                | 回调 → 事件循环                      | mini\_event.h               |
| 58-1 | 异步日志           | 无锁队列+epoll 写盘                              | 多线程日志 → 文件                     | async\_log.c                |
| 58-2 | 系统监控           | /proc/loadavg 实时刷新                         | 无 → 终端动态                       | proc\_top.c                 |
| 58-3 | 温度监控           | hwmon 读取 CPU 温度绘图                          | 传感器 → png                      | temp\_plot.py               |
| 59-1 | 内存泄漏 hunting   | valgrind 基本用法                              | 泄漏 → 报告                        | valgrind\_basic.c           |
| 59-2 | perf 火焰图       | perf record + flamegraph                   | CPU → svg                      | flame.py                    |
| 59-3 | gdb 脚本         | .gdbinit 自动断点                              | 运行 → 断点                        | auto\_gdb.sh                |
| 60-1 | 综合测验           | 30 道笔试题+现场写代码                              | 题目 → 得分                        | exam/                       |
| 60-2 | 项目答辩           | 录 10 min 英文 demo 视频                        | B 站+YouTube 双语字幕               | demo\_video.mp4             |
| 60-3 | 简历打包           | 一键生成 PDF 作品集                               | markdown → pdf                 | resume\_export.py           |
