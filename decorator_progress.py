import time, threading
import sys



class MyTqdm:
    def __init__(self, func, start='|', trace='๑', pose1='ʅ（´◔౪◔）ʃ', pose2='<（´◔౪◔）>', end='|'):
        self.func = func
        self.start = start
        self.trace = trace
        self.pose1 = pose1
        self.pose2 = pose2
        self.res = []
        self.end = end


    def progress(self):
        while self.executing:
            percent = self.percentage
            a = (int(percent)+1)//5
            b = 20-a
            
            sys.stdout.write('\r%s%s%s%s%.2f%% lasting time:%.2fs'%(self.start, a*self.trace+self.pose1, b*' ', self.end, percent,(time.time()-self.time_start)))
            time.sleep(.1)
            sys.stdout.write('\r%s%s%s%s%.2f%% lasting time:%.2fs'%(self.start, a*self.trace+self.pose2, b*' ', self.end, percent,(time.time()-self.time_start)))
            sys.stdout.flush()
            time.sleep(.1)

        a = 20
        b = 0 
        sys.stdout.write('\r%s%s%s%s%.2f%% lasting time:%.2fs\n'%(self.start, a*self.trace+self.pose2, b*' ', self.end, 100.00 ,(time.time()-self.time_start)))



    def countPackaging(self):


        for count,item in enumerate(self.items,1):
            self.res.append(self.func(item))
            self.percentage = count*100/len(self.items)
        self.executing = False
        self.percentage = 0

    def init_process(self):
        self.executing = True
        self.percentage = 0
        self.time_start = time.time()
        t1 = threading.Thread(target=self.progress)
        t2 = threading.Thread(target=self.countPackaging)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        

    def __call__(self,items):
        self.items = tuple(items)
        self.res.clear()
        self.init_process()
        return self.res

      

@MyTqdm
def job(item):
    time.sleep(1/(item+1))
    return item

@MyTqdm
def fac(n):
    def inner(num):
        if num <= 1:
            return 1
        else:
            return n * inner(num-1)
    
    return inner(n)



# @MyTqdm
# def fibo(n):
#     def inner(num):
#         if num <= 2:
#             return 1
#         else:
#             return inner(n-1) + inner(n-2)
    
#     return inner(n)
        

if __name__ == '__main__':
    results = job(range(100))
    print(results)
