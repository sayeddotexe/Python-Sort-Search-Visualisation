#Python 2.7 Bubble-Sort Visualization By Lucid Potato
import pygame
from random import randint
import winsound #Remove if on Linux.
import sys
import random

def visualisor():
    pygame.init()
    size = (1280,720)
    window = pygame.display.set_mode((size))
    pygame.display.set_caption("Pygame Bubble-Sort Visualization")
    black = pygame.Color(0,0,0)
    BLUE = (0,51,102)
    white = pygame.Color(255,255,255)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    GREEN = (200,255,0)
    clock = pygame.time.Clock()


    heightList = []
    listLength = 205
    xList,y,w = [],630,5
    tmpX = 0
    global isSorted
    global sortedCount
    global trackInt
    isSorted = False
    sortedCount = 0
    trackInt = 0

    global bubsort
    bubsort = False


    def update():
        pygame.display.update()

    def text_objects(text,font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
    
    def array_text(heightList):
        bfont = pygame.font.Font("freesansbold.ttf",40)
        font = pygame.font.Font("freesansbold.ttf",6)
        textSurf, textRect = text_objects("Array: ", bfont)
        textRect.center = (1280/2,30)
        window.blit(textSurf,textRect)
        textSurf, textRect = text_objects(str(heightList[102:]), font)
        textRect.center = (1280/2,65)
        window.blit(textSurf,textRect)
        textSurf, textRect = text_objects(str(heightList[:103]), font)
        textRect.center = (1280/2,75)
        window.blit(textSurf,textRect)

    



    def margins():
        pygame.draw.rect(window, BLUE, (0,80,1280,10))

        pygame.draw.rect(window, BLUE, (120,180,1030,10))
        pygame.draw.rect(window, BLUE, (120,630,1030,10))
        
        pygame.draw.rect(window, BLUE, (120,180,10,460))
        pygame.draw.rect(window, BLUE, (1150,180,10,460))

    for i in range(listLength):
        heightList.append(randint(0,400))
        xList.append(tmpX)
        tmpX += w
    

    global insertsort
    global inSorted
    global index
    global current
    global position
    global mergesort
    global quickSort
    global pivot
    global leftmark
    global LI
    global item
    

    insertsort= False
    inSorted = False
    index=1
    current = heightList[index]
    position = index

    mergesort = False
    quickSort = False
    pivot = heightList[0]
    leftmark=1

    Linearindex=-1
    
    LI=0
    found= False
    global LinearSearch
    LinearSearch= False
    global searchbox
    searchbox= False
    item=0
    global intsearch
    intsearch=[]
    global searchready
    searchready= False

    global BinarySearch
    BinarySearch = False
    bsearchsort= False
    global first,last
    found = False
    global Itemfound
    Itemfound = False
    indexBS = -1
    first = 0
    last = len(heightList)-1
    
    
    def draw(xList,y,heightList,trackInt,index):
        
        for i in range(listLength):
            pygame.draw.rect(window,BLUE,(125+xList[i],y,w,heightList[i]*-1),0)
        if insertsort == True:
            pygame.draw.rect(window,RED,(125+xList[position],y,w,heightList[position]*-1),0)
        if bubsort == True:
            pygame.draw.rect(window,RED,(125+xList[trackInt],y,w,heightList[trackInt]*-1),0)
        if quickSort == True and pivot < 205:
            pygame.draw.rect(window,RED,(125+xList[pivot],y,w,heightList[pivot]*-1),0)
        if quickSort == True and leftmark < 205:
            pygame.draw.rect(window,GREEN,(125+xList[leftmark],y,w,heightList[leftmark]*-1),0)
        if LinearSearch == True :
            pygame.draw.rect(window,GREEN,(125+xList[LI],y,w,heightList[LI]*-1),0)
        if BinarySearch == True :
            pygame.draw.rect(window,GREEN,(125+xList[first],y,w,heightList[first]*-1),0)
            pygame.draw.rect(window,GREEN,(125+xList[last],y,w,heightList[last]*-1),0)

                

            
                
        
        

        


            
    def draw_inputbox():
        global LI
        global searchbox
        global searchready
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font = pygame.font.Font("freesansbold.ttf",20)
        
        pygame.draw.rect(window, GREEN, (1050,120,100,50))
        if 1050+100 > mouse[0] > 1050 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (1050,120,100,50))
            if click[0] == 1:
                textSurf, textRect = text_objects("", font)
                textRect.center = ((1050+(100/2)),120+(50/2))
                window.blit(textSurf,textRect)
                searchready=True
                LI = 0

                

            else:
                textSurf, textRect = text_objects("Search", font)
                textRect.center = ((1050+(100/2)),120+(50/2))
                window.blit(textSurf,textRect)
            
                
                
        else:
            pygame.draw.rect(window, GREEN, (1050,120,100,50))

            textSurf, textRect = text_objects(str(intsearch), font)
            textRect.center = ((1050+(100/2)),120+(50/2))
            window.blit(textSurf,textRect)
        
            
        textSurf, textRect = text_objects("Found:"+str(Itemfound), font)
        textRect.center = ((10+(100/2)),300+(50/2))
        window.blit(textSurf,textRect)
        textSurf, textRect = text_objects("index: "+ str(indexBS), font)
        textRect.center = ((15+(100/2)),350+(50/2))
        window.blit(textSurf,textRect)
         

    def draw_buttons(listlength,heightList,xList,tmpx,w):
        global bubsort
        global isSorted
        global sortedCount
        global trackInt
        global mergesort
        global quickSort
        global BinarySearch

        global insertsort
        global inSorted
        global index
        global current
        global position

        global LinearSearch
        global first,last,Itemfound
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        font = pygame.font.Font("freesansbold.ttf",20)

        

        pygame.draw.rect(window, GREEN, (150,120,100,50))
        if 150+100 > mouse[0] > 150 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (150,120,100,50))
            if click[0] == 1:
                
                bubsort = True
                
               
                
        else:
            pygame.draw.rect(window, GREEN, (150,120,100,50))

        textSurf, textRect = text_objects("Bubble", font)
        textRect.center = ((150+(100/2)),120+(50/2))
        window.blit(textSurf,textRect)

        pygame.draw.rect(window, GREEN, (300,120,100,50))
        if 300+100 > mouse[0] > 300 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (300,120,100,50))
            if click[0] == 1:
                insertsort= True
        else:
            pygame.draw.rect(window, GREEN, (300,120,100,50))

        textSurf, textRect = text_objects("Insertion", font)
        textRect.center = ((300+(100/2)),120+(50/2))
        window.blit(textSurf,textRect)

        pygame.draw.rect(window, GREEN, (450,120,100,50))
        if 450+100 > mouse[0] > 450 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (450,120,100,50))
            if click[0] == 1:
                mergesort = True
        else:
            pygame.draw.rect(window, GREEN, (450,120,100,50))

        textSurf, textRect = text_objects("Merge", font)
        textRect.center = ((450+(100/2)),120+(50/2))
        window.blit(textSurf,textRect)

        if 600+100 > mouse[0] > 600 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (600,120,100,50))
            if click[0] == 1:
                quickSort = True
        else:
            pygame.draw.rect(window, GREEN, (600,120,100,50))

        textSurf, textRect = text_objects("Quick", font)
        textRect.center = ((600+(100/2)),120+(50/2))
        window.blit(textSurf,textRect)

        if 750+100 > mouse[0] > 750 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (750,120,100,50))
            if click[0] == 1:
                LinearSearch = True
        else:
            pygame.draw.rect(window, (255,0,255), (750,120,100,50))

        textSurf, textRect = text_objects("Linear", font)
        textRect.center = ((750+(100/2)),120+(50/2))
        window.blit(textSurf,textRect)

        if 900+100 > mouse[0] > 900 and 120+50 > mouse[1] > 120:
            pygame.draw.rect(window, YELLOW, (900,120,100,50))
            if click[0] == 1:
                BinarySearch = True
        else:
            pygame.draw.rect(window, (255,0,255), (900,120,100,50))

        textSurf, textRect = text_objects("Binary", font)
        textRect.center = ((900+(100/2)),120+(50/2))
        window.blit(textSurf,textRect)

		# pygame.draw.rect(window, GREEN, (450,120,100,50)) MERGE
		# pygame.draw.rect(window, GREEN, (600,120,100,50)) QUICK


        pygame.draw.rect(window, GREEN, (580,650,100,50))#RESET BUTTON
        if 580+100 > mouse[0] > 580 and 650+50 > mouse[1] > 650:
            pygame.draw.rect(window, YELLOW, (580,650,100,50))
            if click[0] == 1:
                for i in range(listLength):
                    heightList[i] = randint(0,400)
                isSorted = False
                sortedCount = 0
                trackInt = 0
                bubsort = False

                insertsort= False
                inSorted = False
                index=1
                current = heightList[index]
                position = index

                
                BinarySearch = False
                bsearchsort= False
                found = False
                Itemfound = False
                indexBS = -1
                first = 0
                last = len(heightList)-1

                    
                
               
                
        else:
            pygame.draw.rect(window, GREEN, (580,650,100,50))

        textSurf, textRect = text_objects("Random", font)
        textRect.center = ((580+(100/2)),(650+(50/2)))
        window.blit(textSurf,textRect)

    def displayupdate(xList,y,heightList,trackInt,index,listLength,tmpX,w):
        
        draw_buttons(listLength,heightList,xList,tmpX,w)
        margins()
        array_text(heightList)
        draw(xList,y,heightList,trackInt,index)
        update()
    


    def mergeSort(heightList,xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2):
        if len(heightList) > 1:
            

            mid = len(heightList) // 2
            left = heightList[:mid]
            right = heightList[mid:]
            
            
            mergeSort(left,xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
            
            mergeSort(right,xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
            displayupdate(xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
            i = 0
            j = 0
            k = 0

    
            while i < len(left) and j < len(right):
                if left[i] < right[j]:     
                  heightList[k] = left[i]
                  i += 1
                  
                  displayupdate(xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
                  
                  
                else:
                    heightList[k] = right[j]
                    j += 1
                    
                    displayupdate(xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
                
                    
                k += 1
                
                displayupdate(xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
                

            while i < len(left):
                heightList[k] = left[i]
                i += 1
                k += 1
                
                displayupdate(xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)
                
                
                

            while j < len(right):
                heightList[k]=right[j]
                j += 1
                k += 1
                
                displayupdate(xList2,y2,heightList2,trackInt2,index2,listLength2,tmpX2,w2)

            update()   

    def partition(arr,start,end):
        global pivot
        global leftmark
        
        
        pivot = arr[start]
        leftmark = start+1
        rightmark = end
        done = False
        while done == False:
            while leftmark <= rightmark and arr[leftmark] <= pivot:
                leftmark = leftmark+1
            while arr[rightmark] >= pivot and rightmark >= leftmark:
                rightmark = rightmark -1
            if rightmark < leftmark:
                done = True
            else:
                temp = arr[leftmark]
                arr[leftmark] = arr[rightmark]
                arr[rightmark] = temp
        temp = arr[start]
        arr[start] = arr[rightmark]
        arr[rightmark] = temp
        
        return rightmark
        
    def Bsearch_sort(arr):
        length = len(arr)
       
        for i in range (length-1):
            for j in range (length-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp

    while True:
        window.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                BinarySearch = False
                bsearchsort= False
                found = False
                Itemfound = False
                indexBS = -1
                first = 0
                last = len(heightList)-1

                if len(intsearch)>2:
                    intsearch = []
                else:
                    if event.key == pygame.K_0:
                        intsearch.append(0)
                    if event.key == pygame.K_1:
                        intsearch.append(1)
                    if event.key == pygame.K_2:
                        intsearch.append(2)
                    if event.key == pygame.K_3:
                        intsearch.append(3)
                    if event.key == pygame.K_4:
                        intsearch.append(4)
                    if event.key == pygame.K_5:
                        intsearch.append(5)
                    if event.key == pygame.K_6:
                        intsearch.append(6)
                    if event.key == pygame.K_7:
                        intsearch.append(7)
                    if event.key == pygame.K_8:
                        intsearch.append(8)
                    if event.key == pygame.K_9:
                        intsearch.append(9)
                    
        
     
        

        if bubsort == True:
            
            if trackInt == listLength-1:
                trackInt = 0
            if sortedCount > listLength and isSorted == False:
                
                
                isSorted = True
            if heightList[trackInt] > heightList[trackInt+1] and isSorted == False:
                tmp = heightList[trackInt+1]
                heightList[trackInt+1],heightList[trackInt] = heightList[trackInt],tmp
                sortedCount = 0
                trackInt += 1
                winsound.Beep(heightList[trackInt] + 2000,10) #Remove if on Linux
            else:
                sortedCount += 1
                trackInt += 1
                winsound.Beep(1000,5) #Remove if on Linux
            
        
        
        if insertsort == True:
            if index == listLength-1:
                insertsort = False
            
            
            if position > 0 and heightList[position-1]>current:
                heightList[position] = heightList[position-1]
                position = position-1
                winsound.Beep(heightList[trackInt] + 2000,10)
            else:
                
                heightList[position]=current
                index+=1
                current = heightList[index]
                position = index
                winsound.Beep(1000,5)
        

        if mergesort == True:
           
            mergeSort(heightList,xList,y,heightList,trackInt,index,listLength,tmpX,w)
            mergesort = False
        
        if quickSort == True:    
            def quicksort(arr, start, end,listLength,heightList,xList,tmpX,w,y,trackInt,index):
                if start< end:
                    displayupdate(xList,y,heightList,trackInt,index,listLength,tmpX,w)
                    split = partition(arr, start,end)
                    displayupdate(xList,y,heightList,trackInt,index,listLength,tmpX,w)
                    quicksort(arr, start, split-1,listLength,heightList,xList,tmpX,w,y,trackInt,index)
                    displayupdate(xList,y,heightList,trackInt,index,listLength,tmpX,w)
                    quicksort(arr, split+1, end,listLength,heightList,xList,tmpX,w,y,trackInt,index)
                    displayupdate(xList,y,heightList,trackInt,index,listLength,tmpX,w)
                return arr
            quicksort(heightList,0,len(heightList)-1,listLength,heightList,xList,tmpX,w,y,trackInt,index)
            quickSort= False
        
        if LinearSearch == True and searchready==True and len(intsearch)>0:
            a= ""
            for num in range (0,len(intsearch)):
                a = a+str(intsearch[num])
                item=int(a)
            if LI<len(heightList)-1 and found == False:
                if heightList[LI]==item:
                    Linearindex=LI
                    indexBS = Linearindex
                    found = True
                    Itemfound= True
                    LinearSearch = False
                    searchready = False
                    found = False
                    
                    
                else:
                    LI+=1
            else:
                
                LI=0
                LinearSearch = False
                searchready = False

        if BinarySearch == True and searchready == True and len(intsearch):
            a= ""
            for num in range (0,len(intsearch)):
                a = a+str(intsearch[num])
                item=int(a)
            if bsearchsort == False:
                Bsearch_sort(heightList)
                bsearchsort= True
            else:
                if first <= last and found==False:
                    midpoint=int((first+last)/2)
                    if heightList[midpoint]==item:
                        found = True
                        indexBS=midpoint
                        
                        BinarySearch = False
                        bsearchsort= False
                        found = False
                        Itemfound= True
                        first = 0
                        last = len(heightList)-1
                    if heightList[midpoint]<item:
                        first= midpoint-1
                    else:
                        last = midpoint-1
                    if first == last:
                        found = False
                        
                        BinarySearch = False
                        bsearchsort= False
                        found = False
                        indexBS = -1
                        first = 0
                        last = len(heightList)-1
                        
        
        
        draw_buttons(listLength,heightList,xList,tmpX,w)
        
        draw_inputbox()
        margins()
        array_text(heightList)
        draw(xList,y,heightList,trackInt,index)
        update()
visualisor()