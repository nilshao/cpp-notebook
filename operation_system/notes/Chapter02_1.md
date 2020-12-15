# 第二章 第一节 进程和线程

## 进程的定义，组成，组织方式，特征

* 在计算机发展史上，“进程”是为了解决什么问题而被引入的？

* 每个进程由哪些部分组成

* 系统中各个进程之间是如何被组织起来的？

* 相比于程序，进程有哪些特征

## 进程的定义，进程与程序

程序：就是一个指令序列

早期的计算机只支持单道程序，内存：程序的代码放在程序段内，低地址，程序运行过程处理的数据放在数据段内（如变量），高地址。

**多道程序技术：** 引入多道程序技术后：内存中同时放入多道程序，各个程序的代码，运算数据存放的位置不同，操作系统如何找到各个程序的存放位置？


**PCB：** 系统为每个运行的程序配置一个数据结构，称为进程控制块（PCB），用来描述进程的各种信息（如程序代码存放位置）

为了方便操作系统管理，完成各个程序并发执行，引入了进程、进程实体的概念。PCB、程序段、数据段三部分构成进程实体（进程映像），一般情况下，我们把进程实体就简称为进程，例如，所谓创建进程，实质上是创建进程实体中的PCB；而撤销进程，实质上是撤销进程实体中的PCB。

PCB是进程存在的唯一标志！！！

进程的典型定义方式：“动态性”

1. 进程是程序的一次执行过程

2. 进程是一个程序及其数据在处理机上顺序执行时所发生的活动

3. 进程是具有独立功能的程序在数据集合上运行的过程，它是系统进行资源分配和调度的一个独立单位

引入进程实体的概念后，可把进程定义为：进程是进程实体的运行过程，是系统进行资源分配和调度的一个独立单位。

严格来说，进程实体和进程并不一样，进程实体是静态的，进程则是动态的，不过一般也不区分。

### PCB的组成：

进程描述信息

![PCB组成](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/PCB组成.jpeg)

进程标识符PID：当进程被创建时，操作系统会为该进程分配一个唯一的、不重复的ID，用于区分不同的进程（类似于身份证号）

寄存器值：当进程切换时需要把进程当前的运行情况记录下来保存在PCB中，如程序计数器的值表示当前程序执行到哪一句

## 进程的组织

在一个系统中通常有数十数百个PCB，如何有效组织多个线程

![进程的组织方式](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/进程的组织方式.jpeg)

### 链接方式

1. 执行指针：指向当前处于运行状态（执行态）的进程

2. 就绪队列指针：指向当前处于就绪态的进程，通常会把优先级高的进程放在队头

3. 阻塞队列指针：指向当前处于阻塞态的进程，很多操作系统还会根据阻塞原因不同，再分为多个阻塞队列

### 索引方式

建立相应功能的索引表

![索引方式](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/索引方式.jpeg)

## 进程的特征

![进程的基本特征](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/进程的基本特征.jpg)

动态性是进程最基本的特征

进程是资源分配，接受调度的基本单位

异步性会导致并发程序执行结果的不确定性

## 进程的状态

进程是运行的一次执行，在这个执行过程中，有时进程正在被CPU处理，有时等待CPU服务，可见进程状态会发生变化，为了方便对各个进程的管理，操作系统需要将进程合理划分为多种状态。

1. **运行状态Running（三种基本状态）：** 占有CPU，在CPU上运行。

    单核处理机环境下，则每一时刻最多只有一个进程处于运行态，双核则可以同时有两个进程处于运行态。。。

2. **就绪态Ready（三种基本状态）：** 已经具备运行条件，但由于没有空闲CPU，暂时不能运行。

    就绪态下进程已经拥有了除处理机之外所有需要的资源，一旦获得处理机，即可立即进入运行态开始运行。

3. **阻塞态（等待态）Waiting/Blocked（三种基本状态）：** 因等待某一事件暂时不能运行。

    等待操作系统分配打印机，读写操作等，由于CPU资源最宝贵，所以处理完别的先再进入就绪态等待

4. **创建态：New** 操作系统需要完成创建进程，操作系统为该进程分配所需的内存空间等系统资源，并为其创建、初始化PCB

5. **终止态：Terminated** 进程运行结束，操作系统需要完成撤销进程相关的工作，完成将分配给进程的资源回收，撤销PCB等操作

## 进程状态的转换

![进程状态的转换](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/进程状态的转换.jpeg)



![](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/.jpeg)

![](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/.jpg)

![](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/.JPG)

![](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter2/.png)





















