def tower_of_hanoi(numbers, b, m, e):  
    if(numbers == 1):  
        print('Move disk 1 from pole {} to pole {}'.format(b, e))  
        return
    tower_of_hanoi(numbers - 1, b, e, m)  
    print('Move disk {} from Pole {} to Pole {}'.format(numbers, b, e))  
    tower_of_hanoi(numbers - 1, m, b, e)  
   
numbers = 3
tower_of_hanoi(numbers, 'A', 'B', 'C')