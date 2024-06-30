def get_input(prompt,valid_options=None):
    while True:
        user_input=input(prompt).title()
        if valid_options and user_input not in valid_options:
            print(f"Invalid Input,Please choose from {','.join(valid_options)}")
        else:
            return user_input
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print ("Write Valid Number.Enter right integer")
        
def asc_order(loop_type,start,end,steps):
    attempt=1
    if loop_type in ["For","For Loop","Simple","A"]:
        if start<end:
            for step in range(start,end+1,steps):
                print(f"The {loop_type} Loop #{step} in Ascending Order and Attempt #{attempt} ")
            attempt+=1
        elif start >end:
            for step in range(end,start+1,steps):
                print(f"The {loop_type} Loop in ascending order and Attempt {attempt}")
                attempt+=1
    elif loop_type in ["While","While Loop","Pro","B"]:
        num=start
        if num>end:
            while num>=end:
             print(f"The {loop_type} Loop # {end} and attempt {attempt} in Ascending Order")
             attempt+=1
             end+=steps #num -= steps
        elif num<end:
            while num<=end:
                print(f"The {loop_type} Loop # {num} and attempt {attempt} in Ascending Order")
                num+=steps
                attempt+=1
def desc_order(loop_type,start,end,steps):
    attempt=1
    if loop_type in ["For","For Loop","Simple","A"]:
        if start>end:
         for step in range(start,end-1,-steps):#In des,bigger value comes first,and start is big
            print(f"The {loop_type} Loop #{step} in Descending Order and Attempt #{attempt} ")
            attempt+=1
        elif start<end:
            for step in range(end,start-1,-steps):#In des,bigger value comes first,and end is big
                print(f"The {loop_type} Loop #{step} in Descending Order and Attempt#{attempt}")
                attempt+=1
    elif loop_type in ["While","While Loop","Pro","B"]:
        num=end
        if num>start:#If end is greater then start
         while num>=start:#num(end) value changes and start is fixed.num=100,10,start=10
            print(f"The {loop_type} Loop # {num} and attempt {attempt} in Descending Order")
            attempt+=1
            num-=steps
        elif num<start:#start is big,so start changes and num(end) is fixed,because value decreases with steps 
            while start>=num:
                print(f"The {loop_type} Loop # {start} and attempt {attempt} in Descending Order")
                start-=steps
                attempt+=1
loop_type=get_input("Enter the Loop For/While",["For","For Loop","A","Simple","While","While Loop","B","Pro"])
loop_order=get_input(f"Enter the loop order for {loop_type} Loop Ascending/Descending Order",["Ascending","Asc","A","Positive","Descending","Des","B","Pro"])
initial_value=get_int_input("Enter the first value")
end_value=get_int_input("Enter the end value")
incrementation=get_int_input(f"Enter the value for change in {loop_order} Form for {loop_type} Loop")
# Determine order and call appropriate function
if loop_order in ["Ascending", "Simple", "Good", "Positive", "Pos","Asc","A"]:
    asc_order(loop_type, initial_value, end_value, incrementation)
elif loop_order in ["Descending", "Pro", "Bad", "Reverse", "Negative", "Neg","B","Des"]:
    desc_order(loop_type, initial_value, end_value, incrementation)
else:
    raise ValueError("Invalid loop order. Choose either ascending or descending.")
