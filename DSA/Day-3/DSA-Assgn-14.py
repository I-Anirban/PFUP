#DSA-Assgn-14

#This assignment needs DataStructures.py file in your package, you can get it from resources page

"""*********************Queue*****************************"""
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg



def check_numbers(number_queue):
    #write your logic here
    solution_queue1 = Queue(number_queue.get_max_size())
    while not (number_queue.is_empty()):
        pop = number_queue.dequeue()
        count = 0
        for x in range (1,11):
            if pop%x == 0:
                count+=1
        if count == 10:
            solution_queue1.enqueue(pop)
    return solution_queue1

#Add different values to the queue and test your program
number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
check_numbers(number_queue)