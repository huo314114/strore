from threading import Thread
import time

kep = 0


class chef(Thread):
    chef_name = ''
    kep_sum = 0

    def run(self) -> None:
        global kep
        start = time.time()
        while True:
            end = time.time()
            if (end - start) < 60:
                if kep < 500:
                    self.kep_sum = self.kep_sum + 1
                    kep = kep + 1
                else:
                    time.sleep(3)
            else:
                break
        return self.kep_sum


class client(Thread):
    client_name = ''
    money = 5000.0
    egg = 0

    def run(self) -> None:
        global kep
        start = time.time()
        while True:
            end = time.time()
            if end - start < 60:
                if kep > 0:
                    if self.money >= 3:
                        self.money = self.money - 3
                        kep = kep - 1
                        self.egg = self.egg + 1
                    else:
                        break

                else:
                    time.sleep(2)

            else:
                break
        print(self.client_name, '一共做了抢了', self.egg, '个蛋挞')
        return self.egg


'''调用厨师类'''
chef1 = chef()
chef1.chef_name = '厨师1'

chef2 = chef()
chef2.chef_name = '厨师2'

chef3 = chef()
chef3.chef_name = '厨师3'

'''调用顾客类'''
client1 = client()
client1.client_name = '顾客1'

client2 = client()
client2.client_name = '顾客2'

client3 = client()
client3.client_name = '顾客3'

client4 = client()
client4.client_name = '顾客4'

client5 = client()
client5.client_name = '顾客5'

client6 = client()
client6.client_name = '顾客6'

'''运行线程'''
chef1.start()
chef2.start()
chef3.start()
client1.start()
client2.start()
client3.start()
client4.start()
client5.start()
client6.start()
'''闭塞线程'''
chef1.join()
chef2.join()
chef3.join()
client1.join()
client2.join()
client3.join()
client4.join()
client5.join()
client6.join()
'''会计结算'''
print(chef1.chef_name, '一共做了', chef1.kep_sum, '个蛋挞', '工资', chef1.kep_sum * 1.5)
print(chef2.chef_name, '一共做了', chef2.kep_sum, '个蛋挞', '工资', chef2.kep_sum * 1.5)
print(chef3.chef_name, '一共做了', chef3.kep_sum, '个蛋挞', '工资', chef3.kep_sum * 1.5)