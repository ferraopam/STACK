class Stack:
    def __init__(self):
        self.st=[]
    def push(self):
        num=int(input("Enter the element to push"))
        self.st.append(num)
        print("Element Pushed")
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty:")
        else:
            ele=self.st.pop()
            print(f"Element poped is {ele}")

    def search(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            num=int(input("Enter the elment to search"))
            if num in self.st:
                print(f"Element found at position {self.st.index(num)+1}")
            else:
                print("Element not found")
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Elements in the stack are:")
            for i in range(len(self.st)-1,-1,-1):
                print(self.st[i])
    def is_empty(self):
        if(len(self.st)==0):
            return True 
        else:
            return False
        
        
if __name__=="__main__":
        st=Stack()
        opt_dict={1:st.push,2:st.pop,3:st.display,4:st.search,5:exit}
        while True:
            print("1.push, 2.pop, 3.search.4.display,5.exit")
            try:
                ch=int(input("Enter your choice:"))
                ref=opt_dict[ch] 
                ref()
            except (ValueError,KeyError):
                print("Enter only numbers 1 to 5")
            
    