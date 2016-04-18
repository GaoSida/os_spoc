# coding:utf-8
# 实现stride算法

class Job:
    def __init__(self, pid, total_lenth, priority):
        self.pid = pid
        self.total_lenth = total_lenth
        self.remain = total_lenth
        self.priority = priority
        self.stride = 0
        self.wait = 0     # 等待时间。等待时间 + 执行时间 = 周转时间
        self.response = 0  # 响应时间。如果执行时发现是第一次执行，则当前等待时间是响应时间
        # 由于优先级是变化的，所以需要每次现算，不能提前算完存着
        # self.Pass = 0

class Stride:
    def __init__(self, big_stride, time_slice):
        self.big_stride = big_stride
        self.time_slice = time_slice
        self.job_list = []

    def add_job(self, job):
        job.stride = 0
        self.job_list.append(job)

    def run(self):
        job_done = []
        while (len(self.job_list) != 0):
            # 选择当前stride最小的任务执行
            min_stride = self.job_list[0].stride
            job2exec = self.job_list[0]
            print "current job list: "
            for job in self.job_list:
                print "job " + str(job.pid) + ": stride " + str(job.stride)
                if job.stride < min_stride:
                    min_stride = job.stride
                    job2exec = job

            # 执行这个进程
            if (job2exec.remain == job2exec.total_lenth):  # 如果是第一次执行，则得到了响应时间
                job2exec.response = job2exec.wait
            job2exec.remain -= self.time_slice
            current_time_slice = self.time_slice
            if (job2exec.remain <= 0):
                current_time_slice = job2exec.remain + self.time_slice
                print "Run job " + str(job2exec.pid) + " for " + str(current_time_slice) + " and DONE!"
                self.job_list.remove(job2exec)
                job_done.append(job2exec)
            else:
                print "Run proc " + str(job2exec.pid) + " for " + str(self.time_slice)
                job2exec.stride += self.big_stride / job2exec.priority

            # 更新其余进程的等待时间
            for job in self.job_list:
                if job != job2exec:
                    job.wait += current_time_slice

            print "-------------------------------"
        # 打印所有任务的统计情况
        print "stats: "
        for job in job_done:
            print "Job " + str(job.pid) + " -- Response: " + str(job.response) + \
                "  Turnaround: " + str(job.total_lenth + job.wait) + " Wait: " + str(job.wait)






if __name__ == '__main__':
    stride = Stride(0x7FFFFFFF, 10)
    stride.add_job(Job(1, 58, 40))
    stride.add_job(Job(2, 78, 70))
    stride.add_job(Job(3, 48, 60))
    stride.run()





