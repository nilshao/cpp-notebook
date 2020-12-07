## 第三章 数据链路层

### abstract 

+ 链路层功能

+ 链路层的两种信道

+ 局域网，广域网

+ 链路层设备

### 数据链路层功能概述

数据链路层的研究思想：加头加尾 给物理层

### 基本概念

结点： 主机、路由器

*链路*：网络中两个结点之间的物理通道，

数据链路：网络中两个结点之间的逻辑通道，把实现控制数据传输协议的硬件和软件加到链路上就构成数据链路。

帧：链路层的协议数据单元，封装网络层数据报。

数据链路层负责通过一条链路从一个结点向另一个物理链路直接相连的相邻结点传送数据报。

### 功能概述

数据链路层在物理层提供服务的基础上向网络层提供服务，其最基本的服务是将源自网络层来的数据可靠地传输到相邻结点的目标机网络层。
其主要作用是加强物理层传输原始比特流的功能，将物理层提供的可能出错的物理连接改造成为逻辑上无差错的数据链路，使之对网络层表现为一条无差错的链路。

+ 功能一：为网络层提供服务，无确认无连接服务，有确认无连接服务，有确认面向连接服务。

+ 功能二：链路管理，即连接的建立、维持、释放（用于面向的服务）。

+ 功能三：组帧。

+ 功能四：流量控制：限制发送方。

+ 功能五：差错控制（帧错/位错）

### 封装成帧

封装成帧就是在一段数据的前后部分添加首部和尾部，这样就构成了一个帧。接收端在收到物理层上交的比特流后，就能根据首部和尾部的标记，从收到的比特流中识别帧的开始和结束。

首部和尾部包含许多的控制信息，他们的一个重要作用：帧定界（确定帧的界限）

+ 帧同步：接收方应该能从接收到的二进制比特流中区分出帧的起始和终止

+ 四种方法：字符计数法，字符（字节）填充法，零比特填充法，违规编码法

（图片）![avatar](http://baidu.com/pic/doge.png)

#### 透明传输

透明传输是指不管所传数据是什么样的比特组合都应该能够在链路上传送。因此链路层就“看不见”有什么妨碍数据传输的东西。

当所传数据中比特组合恰好与某个控制信息完全一样时，就必须采取适当的措施，使得接收方不会将这样的数据误认为是某种控制信息，这样才能保证数据链路层的传输是透明的。

#### 字符计数法

帧首部用一个计数字段（第一个字节，八位）来标明帧内字符数。

#### 字符填充法

帧的三个部分：

（图片![avatar](http://baidu.com/pic/doge.png)

+ SOH（start of header）00000001

+ 帧中的数据部分

+ EOT（end oftransmission）00000100

应用：传送文件是由文本文件组成时（文本文件字符都是从键盘上输入的，可用ascii码表达）。当传送的帧是由非ascii码的文本文件组成时（程序/图像等）就不行。可能在
信息中有和eot字段相同的组合，这时候就要采用字符填充的方法实现透明传输。

（图片![avatar](http://baidu.com/pic/doge.png)

在与eot相同的字段前加转义字符esc作为字节填充，与转义字符esc相同的前面也要添加

#### 零比特填充法

操作：5-1-1-0 

+ 在发送端，扫描整个信息字段，只要连续5个1，就立即填入1个0

+ 在接收端收到一个帧时，先找到标志字段确定边界，再用硬件对 比特流 进行扫描。发现连续5个1时，就把后面的0删除。

保证了透明传输：在传送的比特流中可以传送任意比特组合，而不会引起对帧边界的判断错误。

#### 违规编码法  

如曼彻斯特编码中：前高后低是1，前低后高是0。所以可以用高-高，低-低来定界帧的起始和终止。

由于字节计数法中count字段的脆弱性，及字符填充实现上的复杂性和不兼容性，目前较普遍使用的帧同步法是比特填充和违规编码法。

### 差错控制

#### 差错从何而来

概括来说，传输中的差错都是由于噪声引起的。

全局性 

1. 由于线路本身电气特性所产生的随机噪声，是信道固有，随机存在的。

解决办法：提高信噪比来避免干扰

2. 外界特定的短暂原因所造成的冲击噪声，是产生差错的主要原因。解决办法：编码技术

差错：

+ 位错：比特位出错，1变0，0变1。

+ 帧错：丢失，重复，失序

#### 如何差错控制

比特错：

+ 检错编码：奇偶校验码，循环冗余编码CRC

+ 纠错编码：海明码

编码vs编码：

数据链路层编码和物理层数据编码与调制不同。物理层编码针对的是单个比特，解决传输过程中比特的同步等问题，如曼彻斯特编码。
而数据链路层的编码针对的是一组比特。他通过冗余码的技术实现一组二进制比特串在传输过程中是否出现了差错。

冗余编码：在数据发送之前，先按某种关系附加上一定的冗余位, 构成一个符合一定规则的码字再发送。
接收端根据收到码字是否仍符合原规则，来判断是否出错

#### 奇偶校验码

奇偶校验码：n-1位信息元，1位校验元。

+ 奇校验码：X..... n位：“1”的个数为奇数

+ 偶校验码反之

注意是加完校验码后，n长信息串中1的个数为奇数/偶数。and校验码在前面

奇偶校验码特点：只能检测出发生奇数个比特错误时的差错。

#### CRC循环冗余码

（图片）![avatar](http://baidu.com/pic/doge.png)

最终发送的数据是要发送的数据+帧检验数列FCS

总结：在数据链路层仅仅使用循环冗余检验CRC差错检测技术，只能做到对帧的无差错接收，即“凡是接收端数据链路层接受的帧，
都能以接近于1的概率认为这些帧在传输过程中没有产生差错”，接收端丢弃的帧虽然收到了，但是最终还是因为有差错被丢弃。

*凡是接收端数据链路层接受的帧均无差错*

不一定是“可靠传输”，可靠传输是指数据链路层发送端发送什么，接收端就收到什么。

链路层使用CRC检验，能够实现无比特差错的传输，但这还不是可靠传输。

#### 检错编码——————海明码

海明码：发现双比特错，纠正单比特错。

*工作流程*：

确定校验码位数r -> 确定校验码和数据的位置 -> 求出校验码的值 -> 捡错纠错

##### 确定校验码位数r

海明不等式

2的r次方 > k+r+1，r为冗余信息位，k为信息位

要发送的数据：D=101101

数据的位数k=6，满足不等式的最小r为4，也就是D=101101的海明码应该有6+4=10位，其中原数据6位，校验码4位。

##### 确定校验码和数据的位置。

（图片or自己写个表格）![avatar](http://baidu.com/pic/doge.png)

放在2的几次方的位置

##### 求校验码的值

令所有要校验的位异或 = 0。

##### 检测并纠错

找出错误的位并纠错，令所有要校验的位异或运算。

### 流量控制与可靠传输机制

#### 流量控制

较高的发送速度和较低的接受能力不匹配，会造成传输出错，因此流量控制也是数据链路层的一项重要工作。

数据链路层的流量控制是点对点的，传输层的流量控制是端到端的。

传输层流量控制手段：接收端给发送端一个窗口公告。

数据链路层流量控制手段：接收方收不下就不回复确认。

##### 流量控制方法：

+ 停止-等待协议：每发送一个帧就停止发送，等待对方的确认，在收到确认后在发送下一个帧。
（图片![avatar](http://baidu.com/pic/doge.png)

+ 滑动窗口协议：后退N帧协议（GBN），选择重传协议（SR）

![avatar](http://baidu.com/pic/doge.png)

（图片  停止-等待协议也可看作窗口大小均为1的滑动窗口

对比：

停止-等待协议：发送窗口大小 = 1，接收窗口大小 = 1
GBN：发送窗口大小 > 1，接收窗口大小 = 1
SR：发送窗口大小 > 1，接收窗口大小 > 1

(发送窗口，接受窗口大小在发送过程中是固定值)

*回忆：*

可靠传输：发送端发啥 接收端收啥。

流量控制：控制发送速率，使得接收方有足够缓冲空间来接收每一个帧。

滑动窗口解决流量控制：收不下就不确认。

滑动窗口解决可靠传输：发送方自动重传。

### 停止-等待协议

#### 为什么要有停止-等待协议？

除了比特出差错，底层信道还会出现丢包问题。

丢包：物理线路问题，设备问题，路由信息错误等导致数据包丢失。

#### 研究停等协议的前提

虽然现在常用双工通信，为了讨论方便，仍划分为发送方，接收方。

停等，就是每发送完一个分组就停止发送，等待对方确认，在收到确认后发送下一个分组，

停等协议分为两种应用情况：有差错情况，无差错情况

#### 有差错情况

ACK：确认帧（1bit的1和0编号就够）
（图片）![avatar](http://baidu.com/pic/doge.png)

1. 数据帧丢失或检测到帧出错

![avatar](http://baidu.com/pic/doge.png)

（图片）RTT：往返传播时延round trip time

2. ACK丢失

（图片）![avatar](http://baidu.com/pic/doge.png)

3. ACK迟到

#### 性能分析

![avatar](http://baidu.com/pic/doge.png)

简单，信道利用率太低（图片），大部分时间都在路上

#### 信道利用率信道吞吐率

发送方在一个周期内有效地发送数据所需要的时间占整个发送周期的比率

信道利用率 = （L/C）/T

T内发送L比特数据；发送周期T：从开始发送数据，到收到第一个确认帧为止；C：发送方数据传输率

*信道吞吐率* = 信道利用率*发送方的发送速率

（例题图片![avatar](http://baidu.com/pic/doge.png)

#### 流水线技术

增加缓存空间（图片

![avatar](http://baidu.com/pic/doge.png)

### 后退N帧协议GBN

#### 滑动窗口

（图片![avatar](http://baidu.com/pic/doge.png)

+ 发送端要拷贝副本，万一帧错误or丢失

+ 收到某个帧的确认后发确认，发送端滑动窗口后移

#### GBN发送方必须相应的三件事：

1. 上层的调用

上层要发送数据时，发送方先检查发送窗口是否已满，如果未满，产生一个帧并发送，窗口已满时，发送方只需要将数据再返回给上层，
表明上层窗口已满，上层等一会儿在发送。实际中发送方可以缓存这些数据，窗口不满时再发送帧

2. 收到一个ack

gbn协议中，对n号帧采用累计确认方式，表明接收方已经收到n号帧和他之前的全部帧

3. 超时时间

后退n帧的名字，来源于出现丢失和时延过长时发送方的行为。就像停等协议中，定时器将再次用于恢复数据帧 或 确认帧的丢失。
如果出现超时，发送方重传所有已发送单位被确认的帧。

#### 接收方要做的事：

如果正确收到n号帧，并且按序，那么接收方为n帧发送一个ack，并将该帧中数据的部分交付给上层（网络层）。

其余情况都丢弃帧，并为最近按序接收的帧重新发送ack。接收方无需缓存任何失序帧，
只需要维护一个信息：expectedseqnum（下一个按序接收的帧序号）

#### 运行中的GBN

（图片![avatar](http://baidu.com/pic/doge.png)

#### 滑动窗口长度

若采用n个比特对帧编号，那么发送窗口的尺寸Wt应满足 1 <= Wt <= 2的n次方 -1。

若发送窗口尺寸过大，就会使得接收方无法区别新帧和旧帧

e.g. n = 2: 2的2次方 = 4

01230123，若发送窗口为大于3，可能有两个以上的0号帧

#### 重点：

1. 累计确认：n号和n号之前都收到

2. 接收方只按顺序接受帧，不按序的话就全部丢弃

3. 确认序列号最大的，按序到达的帧。（解释不明白就不要说），
发送方可能收到0，2，3的确认，这说明0，2，3在接收方中都已经按序收到并确认了。
1可能发出了，但是没有被发送方收到，因为1如果没被接收方收到是不会发出2和3的确认帧的。


4. 发送窗口最大为，接受窗口只能是1。

#### 性能分析：

pro：因为连续发送数据帧而提高了信道利用率

con：在重传时必须把原来已经正确传送的数据帧批量重传，使得传送效率降低（累计确认的优缺点）

### 选择重传协议SR

Selective Repeat：可不可以只重传出错的帧？

SR：设置单个确认，同时加大接收窗口，设置接收缓存，缓存乱序到达的帧。

#### 选择重传协议中的滑动窗口

（图片![avatar](http://baidu.com/pic/doge.png)

注意上下例子是分开的，不是同一个时序

#### SR发送方必须相应的三件事

1. 上层的调用：

从上层收到数据后，SR发送方检查下一个可用于该帧的序号，如果序号位于发送窗口内，则发送数据帧，否则就像gbn一样，
要么将数据缓存，要么返回上层之后重新传输

2. 收到一个ack

如果收到ack，加入该帧序号在窗口内，则sr发送方将那个被确认的帧标记为已经接收，如果该帧序号是窗口的下界（最左边第一个窗口的序号），
则窗口向前移动到具有最好序号的*未确认帧*处。如果窗口移动了并且有序号在窗口内的未发送帧，则发送这些帧。

3. 超时时间

每个帧都有自己的定时器，一个超时事件后只重传该帧一个帧。

#### 接收方要做的事

SR接收方将确认一个正确接收的帧而不管其是否按序。失序的帧将被缓存，并返回给发送方一个该帧的确认帧（收谁确认谁），
直到所有帧（即序号更小的帧）都被收到为止，这时才可以将一批帧按序交付给上层，然后向前移动滑动窗口。

#### 运行中的SR

（图片
![avatar](http://baidu.com/pic/doge.png)

#### 滑动窗口长度

1. 发送窗口最好等于接收窗口，大了会溢出，小了没意义

2. Wtmax = Wrmax = 2的（n-1）次方

#### 总结：

1. 对数据帧逐一确认，收一个确认一个

2. 只重传出错帧

3. 接收方有缓存 

### 信道划分 介质访问控制

+ 点对点链路：两个相邻结点通过一个链路相连，没有第三者。应用：ppp协议，常用于广域网

+ 广播式链路：
所有主机共享通信介质，应用：早起的总线以太网、无线局域网，常用于局域网。
典型拓扑结构：总线型，星型（逻辑总线型：中间的是集线器，通过集线器广播到连接的主机）

#### 介质访问控制

采取一定的措施，使得两对结点之间的通信不会发生互相干扰的情况。

静态划分信道，动态分配信道

（图片）![avatar](http://baidu.com/pic/doge.png)

#### 什么是信道划分介质访问控制

信道划分介质访问控制：MAC multiple access control（再查查，先不要说）

信道划分介质访问控制：将使用介质的每个设备与来自同一信道上的其他设备的通信隔离开，
把时域和频域资源合理地分配给网络上的设备。

（图片）![avatar](http://baidu.com/pic/doge.png)

多路复用技术：把多个信号组合在一条物理信道上进行传输，使得多个计算机或终端设备共享信道资源，提高信道利用率。

分用：把一条广播信道，逻辑上分成几条用于两个节点之间通信的互不干扰的子信道，实际就是把广播信道转化为点对点信道。

#### 静态信道划分

频分多路复用FDM，时分多路复用TDM，波分多路复用WDM，码分多路复用CDM

+ 频分复用：不同用户在同样的时间占用不同的带宽。充分利用传输介质带宽，系统效率较高；由于技术比较成熟，实现也比较容易。
（图片

![avatar](http://baidu.com/pic/doge.png)

+ 时分复用：一个周期中各个用户占有一个*固定序号*的时隙。

+ 改进的时分复用————统计时分复用STDM：集中器（图片）按需动态分配时隙。

![avatar](http://baidu.com/pic/doge.png)

+ 波分多路复用：光的频分多路复用。

+ 码分多路复用：码分多址（CDMA）是码分复用的一种方式。m一般为64或128。这里的8是方便讲解（图片）（自己再查一下）

![avatar](http://baidu.com/pic/doge.png)

#### 动态分配信道 ALOHA协议

    动态接入控制：信道并非在用户通信时固定地分配给用户。

##### 纯aloha协议

思想：不监听信道，不按时间槽发送，*随机*重发。（想发就发）T0:发送时间，包括传输时间和传播时间。（图片）

![avatar](http://baidu.com/pic/doge.png)

冲突如何检测：如果发生冲突，接收方就会检测出差错，然后不予确认，发送方在一定时间内收不到就判断发生了冲突。

冲突如何解决：超时候等一时间随机重传。重传重传直到收到确认帧

##### 时隙aloha协议

思想：把时间分成若干个相同的时间片，所有用户在时间片开始时刻同步接入网络信道，若发生冲突，
则必须等到下一个时间片开始时刻再发送。（控制了想发就发的随意性）

##### 总结

纯aloha吞吐量较低，吞吐量：一段时间内成功发送的平均帧数。

纯aloha：想发就发，时隙aloha只能在时间片开始时才能发。

#### 动态分配信道 CSMA协议

carrier sense multiple access载波监听多路访问协议CSMA

CS：载波监听/侦听，每一个站在发送数据之前要检测一下总线上是否有其他计算机在发送数据

当几个站同时在总线上发送数据时，总线上的信号电压摆动值将会增大（互相叠加）。当一个站检测到的信号电压摆动值超过一定门限值时，就认为总线上至少有两个站在同时发送数据，即发生冲突

MA：多点接入，即多个计算机以多点接入的方式连接在同一根总线上。

协议思想：发送帧之前监听信道。

监听结果：

信道空闲发送完整帧，有三个协议：1-坚持CSMA，非坚持CSMA，p-坚持CSMA

信道忙：推迟发送

##### 1-坚持csma

坚持指的是对于监听信道忙之后的坚持。

+ 1-坚持csma思想：如果一个主机要发送消息，那么先监听信道。空闲则直接传输，不必等待。忙则保持监听，空闲时马上传输。冲突（一段时间内未受到肯定回复），则等待一个随机长的时间后再监听，loop之前过程

+ 优点：只要媒体空闲，就马上发送，避免了媒体利用率的损失

+ 缺点：假如有两个或两个以上的站点有数据要发送，冲突就不可避免。

##### 非坚持csma

非坚持指的是对于监听信道忙就不继续监听。

+ 思想：如果一个主机要发送消息，那么先监听信道，空闲则直接传输，不必等待。忙则等待一个随机事件之后再监听。

+ 优点：采用随机的重发延迟时间可以减少冲突发生的可能性。

+ 缺点：可能存在大家都在延迟等待过程中，使得媒体仍可能处于空闲状态，媒体使用率降低。

##### p坚持csma

指的是对于监听信道空闲的处理。

+ 思想：如果一个主机要发送消息，那么先监听信道。*空闲*则以p概率直接传输，不必等待，1-p的概率等到下一个时间槽再传输。
*忙*则等待一个随机时间之后在进行监听。

+ 优点：既能像非坚持算法那样减少冲突，又能像1-坚持算法那样减少媒体空闲时间

+ 缺点：发生冲突后还是可能坚持把数据帧发送完，造成了浪费。

##### 对比

（图片，表格

![avatar](http://baidu.com/pic/doge.png)

#### 动态分配信道 CSMA-CD协议 (先听再说，边听边说)

carrier sense multiple access with collision detection

CS：载波监听/侦听，每一个站在发送数据之前要检测一下总线上是否有其他计算机在发送数据

MA：多点接入，即多个计算机以多点接入的方式连接在同一根总线上。

CD：碰撞检测（冲突检测），“边发送边监听”，适配器边发送数据边检测信道上信号电压的变化情况，以便判断自己在发送数据时其他站是否也在发送数据。

思考：为什么先听后发还会冲突？因为电磁波在总线上总是以有限的速率传播的：传播时延，在双工通信中两个互相发送会冲突碰撞（尽管是双工半双工，指的是两条逻辑通路，一个物理通路）。

##### 传播时延对载波监听的影响

（图片）![avatar](http://baidu.com/pic/doge.png)


冲突，碰撞
（图片2——

![avatar](http://baidu.com/pic/doge.png)

碰撞后信息发生叠加，可以检测出来。

最多是两倍的总线端到端的传播时延（2tao），总线的端到端往返传播时延，称为争用期/碰撞窗口/冲突窗口。

因此只要经过2tao时间还没有检测到碰撞，就能肯定这次发送不会发生碰撞。

##### 如何确定碰撞后的重传时机？

1. 确定基本退避（推迟）时间为争用期2tao。

2. 定义参数k，它等于重传参数，但k不超过10，即k=min（重传次数，10），当重传次数不超过10时，k等于重传次数，重传次数大于10时，k一直为10.

3. 从离散的整数集合[0,1,...,2的k次方 -1]中随即取出一个数r，重传所需要的退避时间就是r倍的*基本退避时间*，即2r*tao。

4. 当重传次数达到16次仍不能成功时，说明网络太拥挤，认为此帧永远无法正确发出，抛弃此帧并向高层报告出错。重传：截断二进制指数规避算法。
（图片

![avatar](http://baidu.com/pic/doge.png)

##### 总结

若连续多次冲突

##### 例题

（图片![avatar](http://baidu.com/pic/doge.png)

##### 最小帧长

发了一个帧，但是发生了碰撞，但是在发送完之后才检测到发生碰撞，但是无法停止因为已经发完了。因此要最小帧长。

真的传输时延至少要两倍于信号在总线中的传播时延。（公式图片——）但最小64B，不足则填充

![avatar](http://baidu.com/pic/doge.png)

#### 动态分配信道 CSMA-CA协议

CA：collision avoidance，不仅能检测，还能避免

场景：

CD：总线式以太网

CA：无线局域网：

+ 无法做到360度全面检测碰撞；

+ 隐蔽站：当终端A和C都检测不到信号，认为信道空闲时，同时向终端B发送数据帧，就会导致冲突

##### 工作原理

先听后说

空闲时则发出*RTS*（request to send），rts包括发射端的地址，接收端的地址，下一份数据将持续发送的时间等信息；信道忙则等待。

接收端收到RTS之后，将响应cts（clear to send）

发送端收到cts后，开始发送数据帧，同时预约信道：发送方告知其他站点自己要传多久数据。

接收端收到数据帧后，将用crc检验数据，正确则发送ack帧。

发送端收到ack后就可以进行下一个数据帧的发送，若没有则一直重传至规定重发次数为止（二进制指数退避）

*过程总结：*

1. 预约信道

2. ACK帧

3. RTS/CTS帧

##### csma/cd 与 csma/ca总结

（图片![avatar](http://baidu.com/pic/doge.png)

#### 轮询访问介质访问控制

既不产生冲突，又要发送时占全部带宽。

轮询协议，令牌传递协议。

##### 轮询协议

主节点轮流“邀请”从属结点发送数据。

问题：

+ 轮询开销

+ 等待延迟

+ 单点故障

##### 令牌传递协议

令牌：一个特殊格式的mac控制帧，不含任何信息。控制信道的使用，确保同一时刻只有一个结点独占信道。令牌环网无碰撞
（图片）![avatar](http://baidu.com/pic/doge.png)

每个节点都可以在一定时间内（令牌持有时间）获得发送数据的权利，不是无限制地持有令牌

问题：令牌开销，等待延迟，单点故障

只应用于（逻辑拓扑的）令牌环网，采用令牌传送的方式通常用于负载较重，通信量较大的网络中。

### 局域网

局域网LAN（local area network），是指在某一区域内多台计算机互连成的计算机组，使用广播信道。

+ 覆盖地理范围较小，只能在一个相对独立区域内联

+ 使用专门铺设的传输介质（双绞线，同轴电缆等）进行联网，数据传输速率高

+ 通信延迟时间短，误码率低，可靠性较高

+ 各站为平等关系，共享传输信道

+ 多采用分布式控制和广播式通信，能广播和组播

局域网的主要要素：网络拓扑，传输介质和介质访问控制方法

#### 拓扑结构

星型，总线型，环形，树形
（图片）![avatar](http://baidu.com/pic/doge.png)


#### 局域网介质访问控制方法

+ *csma-md*， 常用语总线型，也用于树形网络

+ *令牌总线*，常用于总线型，也用于树形网络。它是把总线型或树形网络中的各个工作站按照一定顺序如按接口地址大小排列形成一个逻辑环，只有令牌持有者才能控制总线，才有发送信息的权利。

+ *令牌环*，用于环形局域网，如令牌环网

注意：逻辑拓扑和物理拓扑可能不一样

#### 局域网分类

+ *以太网*：是应用最广泛的局域网，包括标准以太网，快速以太网，千兆以太网和10G以太网（--后期补全一下各个的速度）。逻辑拓扑是总线型，物理拓扑是星型或者拓展星型。使用csma-md

+ 令牌环网：物理上是星型拓扑，逻辑上是*环形*拓扑结构，所以现在很少了

+ fddi网（fiber distributed data interface）：物理上双环拓扑结构，逻辑上是环形拓扑，也很少

+ atm网（asynchronous transfer mode)：较新型的单元交换技术，使用53字节固定长度的单元进行交换（说不明白就别说了

+ *无线局域网wlan*（wireless local area network）：ieee802标准（了解即可）

#### mac子层和llc子层

ieee802标准所描述的局域网参考模型对应osi参考模型的数据链路层和物理层，它将数据链路层划分为逻辑链路层llc，和介质访问控制mac子层。（图片

![avatar](http://baidu.com/pic/doge.png)

+ llc负责识别网络层协议，然后对他们进行封装

+ mac子层


### 以太网Ethernet

是当今现有局域网采用的最通用的通信协议标准，使用csma-cd技术。

1. 造价低廉，以太网网卡不到100块

2. 是应用最广泛的局域网技术

3. 比令牌环网，atm网便宜，简单

4. 满足网络速度要求：标准以太网，快速以太网，千兆以太网和10G以太网 10mb/s到10gb/s

#### 无连接，不可靠的服务

无连接：发送方和接收方无握手过程

不可靠：不对发送方的数据帧编号，接收方不想发送方进行确认，差错帧直接丢弃，差错纠正由更高层（传输层或称运输层）负责

因此只能无差错接收，不实现可靠传输。

#### 拓扑结构的发展

总线型发展到星型

（图片
![avatar](http://baidu.com/pic/doge.png)

#### 10base-t以太网

#### 适配器和mac地址

计算机与外界局域网的连接是通过通信适配器进行的。“网卡”，适配器也有处理器和存储器，存储器包括rom和ram。

rom上有计算机硬件地址、物理地址、mac地址，是硬件的标识符。

mac地址：每个适配器有一个全球唯一的48位二进制地址，前24位代表厂家，由ieee规定，后24位厂家自己制定，常用6个十六进制数字表示。
如02-60-8c-e4-b1-21，在生产适配器时，这6字节MAC地址已被固化在适配器的ROM中，是全球唯一的。

#### 以太网mac帧

最常用的mac帧是以太网v2的格式。
（图片

![avatar](http://baidu.com/pic/doge.png)

注：数据长度范围：46-1500: 1500是mtu，最大数据传送单元，最小帧长64字节，之前有了18字节了，为了保证mac帧是有效帧。

#### 高速以太网

（图片
![avatar](http://baidu.com/pic/doge.png)

### 无线局域网wlan

wifi属于wlan

无线局域网通用标准：ieee802.11

#### 802.11的mac帧头格式

（图片![avatar](http://baidu.com/pic/doge.png)

#### 剩余在看一次3.6.3


### ppp协议，hdlc协议

广域网（WAN wide area network）通常跨界很大的物理范围，所覆盖的范围从几十公里到几千公里，能连接多个城市或国家，或者横跨几个周并能提供远距离通信，形成国际性的远程网络。

广域网的通信子网使用*分组交换技术*，广域网的通信子网可以利用公用分组交换网，微信通信网和无线分组交换网，将分布在各个地区的局域网或计算机系统互联起来，达到资源共享的目的。因特网是世界范围内最大的广域网。

#### ppp协议

点对点协议point-to-point protocol，是目前使用最广泛的数据链路层协议。用户使用拨号电话接入因特网时一般都用ppp协议。*只支持全双工链路*。

##### 应满足的要求：

+ *简单* 对于链路层的帧，无需纠错，无需序号，无需流量控制

+ *封装成帧* 帧定界符

+ *透明传输* 与帧定界符相同的比特组合数据时：异步线路用字节填充，同步线路用比特填充

+ *多种网络层协议* 封装的ip数据包可以采用多种协议

+ *多种类型链路* 串行/并行，同步/异步，电/光

+ *差错检测* 错就丢弃

+ *检测连接状态* 链路是否正常工作

+ *最大传送单元* 数据部分最大长度MTU

+ *网络层地址协商* 知道通信双方的网络层地址

##### 无需满足的要求

纠错，流量控制，序号，不支持多点线路

##### 三个组成部分

1. 一个将ip数据报封装到串行链路（同步串行/异步串行）的方法

2. 链路控制协议lcp：建立并维护数据链路连接（身份验证功能）

3. 网络控制协议ncp：ppp可支持多种网络层协议，每个不同的网络层协议都要一个相应的ncp来配置，为网络协议 建立和配置 逻辑链接。

##### 状态图 

（图片）![avatar](http://baidu.com/pic/doge.png)

##### ppp协议的帧格式

（图片）![avatar](http://baidu.com/pic/doge.png)

#### hdlc协议

高级数据链路控制（high level data link control),是一个在同步网上传输数据，面向比特的数据链路层协议

数据报文可以透明传输，用于实现透明传输的“0比特插入法”易于硬件实现。

##### 站

主战，从站，符合站

（图片）![avatar](http://baidu.com/pic/doge.png)

##### hdlc的帧格式

（图片）![hdlc的帧格式](http://baidu.com/pic/doge.png)

#### ppp协议和hdlc协议

hdlc，ppp都只支持全双工链路，都可以实现透明传输。都可以实现差错检测，但不纠正差错。

### 链路层设备

#### 物理层扩展以太网

光纤（光纤调制器，光纤解调器）。集线器（集线器下的计算机们构成冲突域，只能同时有一个设备发送；主干集线器）

#### 链路层扩展以太网

网桥或称交换机（在看一次）

把冲突域分隔开

**网段**

##### 透明网桥

透明 是指以太网上的站点并不知道所发送的帧将经过哪几个网桥，是一种即插即用设备（自学习）
（todo——[透明网桥](http://baidu.com/pic/doge.png)


##### 源路由网桥

在发送帧的时候把详细的最佳路由信息（路由最少/时间最短）放在帧的首部中

方法： 源站以广播的方式向欲通信的目的站发送一个发现帧。（看看别的资料）

##### 多接口网桥————以太网交换机

可以独占传输媒体带宽

##### 以太网交换机的两种交换方式

**直通式交换机** 查完目的地址（6B）就立刻转发。延迟小，可靠性低，无法支持具有不同速率的端口的交换。

**存储转发式交换机** 将帧放入高速缓存，并检查是否正确，正确则转发，错误则丢弃。延迟大，可靠性高，可以支持具有不同速率的端口的交换。

##### 冲突域和广播域

![冲突域和广播域](https://github.com/nilshao/cpp-notebook/blob/master/internet/pictures/%E5%86%B2%E7%AA%81%E5%9F%9F%E5%B9%BF%E6%92%AD%E5%9F%9F.JPG)

链路域设备（交换机） 每个接口分割一个冲突域。





























