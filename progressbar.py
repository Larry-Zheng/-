import time, threading
import sys



class MyTqdm:
    def __init__(self, func, items, start='|', trace='๑', pose1='ʅ（´◔౪◔）ʃ', pose2='<（´◔౪◔）>', end='|'):
        self.func = func
        self.items = items
        self.start = start
        self.trace = trace
        self.pose1 = pose1
        self.pose2 = pose2
        self.end = end

        self.count = 0

        t1 = threading.Thread(target=self.progress)
        t2 = threading.Thread(target=self.countPackaging)
        self.executing = True
        t1.start()
        t2.start()
        t1.join()
        t2.join()


    def progress(self):
        while self.executing:
            percent = self.count*100/len(self.items)
            a = (int(percent)+1)//5
            b = 20-a


            sys.stdout.write('\r%s%s%s%s%.2f%%'%(self.start, a*self.trace+self.pose1, b*' ', self.end, percent))
            time.sleep(.1)
            sys.stdout.write('\r%s%s%s%s%.2f%%'%(self.start, a*self.trace+self.pose2, b*' ', self.end, percent))
            sys.stdout.flush()
            time.sleep(.1)

        sys.stdout.write('\r%s%s%s%s%.2f%%'%(self.start, a*self.trace+self.pose2, b*' ', self.end, 100.00 ))



    def countPackaging(self):
        for item in self.items:
            self.func(item)
            self.count += 1
        self.executing = False



def job(item):
    time.sleep(item/500)

if __name__ == '__main__':
    numbers = [ i for i in range(100,0,-1)]
    MyTqdm(job, numbers, \
            pose1='ʅ（´◔౪◔）ʃ', pose2='<（´◔౪◔）>', trace='๑', end='♥')



   
