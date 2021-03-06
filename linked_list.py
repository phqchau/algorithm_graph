class LinkedList(object):

  class Node(object):

    def __init__(self, data=None, next_node=None):
      self.data = data
      self.next_node = next_node

    def get_data(self):
      return self.data

    def set_data(self):
      self.data = None

    def get_next(self):
      return self.next_node

    def set_next(self, new_next):
      self.next_node = new_next

# ---------------- LinkedList Class methods ----------------
  def __init__(self, head=None):
    self.head = head

  def insert(self, data):    #Inserts the new node as the head
    new_node = self.Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    #return

  def get_head_value(self):
    return self.head.get_data() if self.head else None

  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.get_next()
    return count

  def search(self, data):
    current = self.head
    found = False
    while current and found is False:
      if current.get_data() == data:
        found = True
      else:
        current = current.get_next()
    if current is None:
      raise ValueError("Data not in list")
    return current

  def delete(self, data):
    current = self.head
    previous = None
    found = False
    while current and found is False:
      if current.get_data() == data:
        found = True
      else:
        previous = current
        current = current.get_next()
    if current is None:
      raise ValueError("Data not in list")
    if previous is None:
      self.head = current.get_next()
      current.data = None
      current.set_next(None)
      current = None
    else:
      previous.set_next(current.get_next())
      current.data = None
      current.set_next(None)
      current = None
