# coding:utf-8
# 实现stride算法

class Job:
    def __init__(self, pid, total_lenth, priority):
        self.pid = pid
        self.total_lenth = total_lenth
        self.priority = priority
        self.stride = 0
        # 由于优先级是变化的，所以需要
        # self.Pass = 0

class Stride:
    def __init__(self, big_stride, time_slice):
        self.big_stride = big_stride
        self.time_slice = time_slice
        self.job_list = []

    def add_job(self, job):
        job.stride = 0
        self.job_list.append(job)




if __name__ == '__main__':





