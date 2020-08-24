import random
processor_count = 5 #processor count
processor = []
time = []
#assigning random loads and time-to-sync for invoking algorithm
for i in range(k):
    processor.append(random.randrange(100,10000))
    time.append(random.randrange(100,1000))
print(processor,time,sep='\n')
i = 100 #multiples of when algorithm should be invoked, starting cycle value

while i<1000000:#max number of cycles
	#exit condition for checking if balanced
    if max(processor)-min(processor)<=1000:
        print(i)
        break

    for j in range(len(time)):
        #condition of invoke balancing algorithm
        if i%time[j]==0:
            if (processor[(j-1)%processor_count]+processor[(j+1)%k])//2 <= processor[j]:
                time[j] = random.randrange(100, 1000)

                if processor[(j-1)%processor_count] < processor[j]:
                    processor[(j - 1) % processor_count] += ((processor[(j-1)%processor_count]+processor[j])//2) - processor[(j - 1) % processor_count]

                elif processor[(j+1)%processor_count] < processor[j]:
                    processor[(j + 1) % processor_count] += ((processor[(j + 1)%processor_count] + processor[j]) // 2) - processor[(j + 1) % processor_count]


    i+=1
    print(processor,i)

#new comment





# a =  random.randint(10,1000)

# print(processor,time,sep='\n')
