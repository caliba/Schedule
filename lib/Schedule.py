#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/4 2:57 PM
# @Author  : Agonsle
# @Site    : 
# @File    : Schedule.py
# @Software: PyCharm

from queue import Queue
import threading
import time

class Schedule:

    def __init__(self, policy, config, server_port,queue):
        self.policy = policy
        self.config = config
        self.queue = queue
        self.server_port = server_port
        self.list_q = []

        for i in range(len(self.config)):
            self.list_q.append([])

    def RoundRobin(self):
        """
        每个workload给一个请求
        :return:
        """
        index = 0
        print("--- Scheduling policy RoundRobin ---")
        while True:
            while not self.queue.empty():

                self.list_q[index].append(self.queue.get())
                print(" index {} len {}".format(index,len(self.list_q[index])))
                if len(self.list_q[index]) == self.config[self.server_port[index]]:
                    self.list_q[index].clear()
                index = (index + 1) % len(self.config)

    def FullBatch(self):
        """
        每个请求都收集到一个batch再传送
        :return:
        """

        pass
    def generate_request(self):
        for i in range(5):
            self.queue.put(1)
            time.sleep(1)


    def run(self):
        t1 = threading.Thread(target=self.generate_request)
        t2 = threading.Thread(target=self.RoundRobin)

        t1.start()
        t2.start()

def main():
    config = {'50002': 2, '50003': 2}
    server_port = ['50002','50003']
    s = Schedule(config=config,server_port=server_port,policy=1,queue=Queue())
    s.run()




main()