from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
      #attemp1
      # if self.current:
      #   self.storage.move_to_end(item)
      #   return 
      # if self.capacity == self.storage.__len__(): 
      # #len(self.storage):
      #   self.storage.remove_from_head()
      #   self.capacity -= 1
        
      # self.storage.add_to_tail(item)
      # self.current = self.storage.tail
      
      # self.capacity += 1
      if self.storage.length < self.capacity:
        self.storage.add_to_tail(item)
        self.current = self.storage.tail 
      if self.storage.length == self.capacity:  
        if self.current is self.storage.tail: 
          self.storage.tail.next = self.storage.head 
      self.current.value = item
      self.current = self.current.next       
        
        

    def get(self):
        # Note:  This is the only [] allowed
      list_buffer_contents = []

        # TODO: Your code here
      # if self.current: 
          # list_buffer_contents[self.current.value:] + list_buffer_contents[:self.current.value]
      current = self.storage.head
      while current:
        list_buffer_contents.append(current)
        current = current.next
        if current is self.storage.head:
          break
      return [ item.value for item in list_buffer_contents] 
      
     
# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
