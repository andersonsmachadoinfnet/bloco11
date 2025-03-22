class MinHeap:
    def __init__(self):
        self.a = []

    def insert(self, val):
        self.a.append(val)
        i = len(self.a) - 1
        while i > 0 and self.a[(i - 1) // 2] > self.a[i]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def delete(self, value):
        i = -1
        for j in range(len(self.a)):
            if self.a[j] == value:
                i = j
                break
        if i == -1:
            return
        self.a[i] = self.a[-1]
        self.a.pop()
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.a) and self.a[left] < self.a[smallest]:
                smallest = left
            if right < len(self.a) and self.a[right] < self.a[smallest]:
                smallest = right
            if smallest != i:
                self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
                i = smallest
            else:
                break

    def minHeapify(self, i, n):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.minHeapify(smallest, n)

    def printHeap(self):
        print("Min Heap:", self.a)

    def createHeap(self, values):
        for value in values:
            self.insert(value)

    def search(self, element):
        for j in self.a:
            if j == element:
                return True
        return False

if __name__ == "__main__":
    h = MinHeap()
    h.createHeap([5, 2, 3, 7, 1])
    h.printHeap()
    h.insert(0)
    h.printHeap()
    print("Procurando pelo 7 na heap:", "Encontrado" if h.search(7) else "Não encontrado")
    h.delete(0)
    h.printHeap()
