from queue import Queue
class QueueCircular:
    def __init__(self, size):
        self.items = [None] * size
        self.MAX = size
        self.front = -1
        self.back = -1
        
    def enqueue(self, item):
        if (self.back + 1) % self.MAX == self.front :
            print('The circular queue is full')
        elif self.back == -1:
            self.front = 0
            self.back = 0
            self.items[self.back] = item
        else:
            self.back = (self.back + 1) % self.MAX
            self.items[self.back] = item
    def dequeue(self):
        if self.front == -1:
            print('The circular queue is empty')            
        elif self.front == self.back:
            now = self.items[self.front] #???????????????????????????
            self.front = -1
            self.back = -1
            self.items[self.back] = now #????????????????????????????
        else:
            now = self.items[self.front]
            self.front = (self.front + 1) % self.MAX
            #return now
    def __repr__(self):
        return ('front: {} points({}), back: {} points({})'. format(self.front, self.items[self.front], self.back, self.items[self.back]))
    def __str__(self):
        if self.front == -1:
            return ('QueueCircular([])')
        else:
            return ('QueueCircular({})'.format(self.items[self.front:self.back+1])) #???????????????????????????
    
if __name__ == '__main__':
    q = QueueCircular(4)
    print('1:',q)
    q.enqueue(12)  
    q.enqueue(17) 
    q.enqueue(25)  
    q.enqueue(11)  
    q.enqueue(30) 
    print('4: ',q)
    q.dequeue()  
    q.dequeue()  
    print('5: ',q)
