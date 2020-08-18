class BinaryHeap:
    def __init__(self):
        # Nb an empty heap list has a zero at the starting index that is never used
        # It is there so that integer division can work later on
        self.heap_list = [0]
        self.current_size = 0

    # swaps an item with its parent if the parent is smaller than the item
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i //
                                                  2] = self.heap_list[i // 2], self.heap_list[i]

                # unpythonic way
                # temp = self.heap_list[i]
                # self.heap_list[i] = self.heap_list[i // 2]
                # self.heap_list[i // 2] = temp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) < = self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]

            i = mc

    def min_child(self, i):
        #if there is no right child return the left child
        if (i*2 + 1) > self.current_size:
            return i * 2
        #check which is smaller between the left and right child and return that node
        else:
            if self.heap_list[i*2] > self.heap_list[i*2+1]:
                return self.heap_list[i*2+1]
            else:
                return self.heap_list[i*2]

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.perc_down(1)

        return ret_val

    #More analysis needed!!
    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
