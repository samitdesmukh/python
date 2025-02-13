class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, e):
        self.queue.append(e)
        print(f"Enqueued: {e}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! cannot dequeue.")
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue)==0
    def display(self):
        print("Queue:", self.queue)


q= Queue()
while True:
    print("\n choose an operation")
    print("1. Enqueue (ADD to queue)")
    print("2. Dequeue (Remove from queue)")
    print("3. check if queue is empty")
    print("4. Display queue")
    print("5. Exit")

    choice = input("Enter your choice(1-5)")
    if choice == '1':
        element= input("Enter the element to enqueue")
        q.enqueue(element)
    elif choice=='2':
        removed_element=q.dequeue()
        if removed_element is not None:
            print(f"Dequeue: {removed_element}")
    elif choice == '3':
        print(f"Is queue Empty?{q.is_empty()}")
    elif choice == '4':
        q.display()
    elif choice =='5':
        print("Exiting program")
        break
    else:
        print("Invalid choice!")


