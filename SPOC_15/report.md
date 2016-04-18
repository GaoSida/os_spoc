# Stride处理机调度算法 实验报告
计35  高思达  2013011413

#### 1、实现要点说明
* 自定义了任务类Job。其中主要保存的信息是任务的pid，优先级，需要执行的时间，当前的剩余执行时间（即进度）。为了支持Stride算法，需要保存Stride。同时，为了方便统计，同时保存进程的响应时间和等待时间。
* 注意，由于进程的优先级是可以动态变化的，因此`Pass = BigStride / Priority`并不能作为任务的属性，而需要在调度时现计算。
* 算法的主要流程是：每次上一进程的时间片结束后，选择所有就绪进程中Stride最小的进程调度。对于被调度的进程，更新其Stride的值为`Old_Stride + Pass`，其中`Pass = BigStride / Priority`。
* 相应时间的计算方法为：如果调度时发现该进程的剩余时间还是总的执行时间，则表明这是第一次调度。于是当前进程的等待时间就是响应时间。
* 对于没有被调度的进程，把当前时间片累加到他们的等待时间中。
* 轮转时间 = 执行时间 + 等待时间。 

#### 2、结果分析
为了方便检查算法的正确性，我们打印出每次进程调度时的任务列表和他们的Stride的值。算法的基本参数BigStride，参照ucore设置为0x7FFFFFFF，时间片长度为10。当输入三个任务，需要的时间分别为58，78，48；对应的优先级分别为40，70，60时，输出结果如下所示：
```
current job list: 
job 1: stride 0
job 2: stride 0
job 3: stride 0
Run proc 1 for 10
-------------------------------
current job list: 
job 1: stride 53687091
job 2: stride 0
job 3: stride 0
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 53687091
job 2: stride 30678337
job 3: stride 0
Run proc 3 for 10
-------------------------------
current job list: 
job 1: stride 53687091
job 2: stride 30678337
job 3: stride 35791394
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 53687091
job 2: stride 61356674
job 3: stride 35791394
Run proc 3 for 10
-------------------------------
current job list: 
job 1: stride 53687091
job 2: stride 61356674
job 3: stride 71582788
Run proc 1 for 10
-------------------------------
current job list: 
job 1: stride 107374182
job 2: stride 61356674
job 3: stride 71582788
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 107374182
job 2: stride 92035011
job 3: stride 71582788
Run proc 3 for 10
-------------------------------
current job list: 
job 1: stride 107374182
job 2: stride 92035011
job 3: stride 107374182
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 107374182
job 2: stride 122713348
job 3: stride 107374182
Run proc 1 for 10
-------------------------------
current job list: 
job 1: stride 161061273
job 2: stride 122713348
job 3: stride 107374182
Run proc 3 for 10
-------------------------------
current job list: 
job 1: stride 161061273
job 2: stride 122713348
job 3: stride 143165576
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 161061273
job 2: stride 153391685
job 3: stride 143165576
Run job 3 for 8 and DONE!
-------------------------------
current job list: 
job 1: stride 161061273
job 2: stride 153391685
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 161061273
job 2: stride 184070022
Run proc 1 for 10
-------------------------------
current job list: 
job 1: stride 214748364
job 2: stride 184070022
Run proc 2 for 10
-------------------------------
current job list: 
job 1: stride 214748364
job 2: stride 214748359
Run job 2 for 8 and DONE!
-------------------------------
current job list: 
job 1: stride 214748364
Run proc 1 for 10
-------------------------------
current job list: 
job 1: stride 268435455
Run job 1 for 8 and DONE!
-------------------------------
stats: 
Job 3 -- Response: 20  Turnaround: 128 Wait: 80
Job 2 -- Response: 10  Turnaround: 166 Wait: 88
Job 1 -- Response: 0  Turnaround: 184 Wait: 126
Average -- Response: 10.0  Turnaround: 159.333333333 Wait: 98.0
```
从上面的统计结果中可以看出，优先级更高的进程会被优先调度，会有更短的等待时间（相对执行时间而言的比例更短）。而优先级较低的进程，即便本身所需的执行时间较短，最终也会因为等待高优先级的进程先执行，而较晚做完。这是符合我们对于优先级的要求的，可以看到Stride算法的调度效果。

#### 3、算法实现的不足
当前并没有考虑Stride溢出时的比较大小方式。这一完善将留到Lab6中在实际的ucore代码中完成。
