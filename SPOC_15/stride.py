# coding:utf-8
# 实现stride算法

class Job:
    def __init__(self, pid, total_lenth, priority):
        self.pid = pid
        self.total_lenth = total_lenth
        self.remain = total_lenth
        self.priority = priority
        self.stride = 0
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
        while (len(self.job_list) != 0):
            # 选择当前stride最小的任务执行
            min_stride = self.job_list[0].stride
            job2exec = self.job_list[0]
            for job in self.job_list:
                if job.stride < min_stride:
                    min_stride = job.stride
                    job2exec = job

            # 执行
            job2exec.remain -= self.time_slice
            if (job2exec.remain < 0):
                print "Run proc " + str(job2exec.pid) + " for " + str(job2exec.remain + self.time_slice)
                self.job_list.remove(job2exec)
            else:
                print "Run proc " + str(job2exec.pid) + " for " + str(self.time_slice)
                job2exec.stride += self.big_stride / job2exec.priority






if __name__ == '__main__':
    stride = Stride(0x7FFFFFFF, 10)
    stride.add_job(Job(1, 288, 40))
    stride.add_job(Job(2, 288, 80))
    stride.add_job(Job(3, 288, 60))
    stride.run()





