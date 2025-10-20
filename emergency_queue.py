from dataclasses import dataclass

@dataclass(order=True)
class Patient:
    urgency: int  # order=True uses first field for comparisons; 1 = most urgent
    name: str

    def __post_init__(self):
        if not isinstance(self.urgency, int):
            raise TypeError("urgency must be an int from 1 to 10")
        if not (1 <= self.urgency <= 10):
            raise ValueError("urgency must be between 1 (most urgent) and 10 (least urgent)")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")


class MinHeap:
    def __init__(self):
        self.data: list[Patient] = []

    # ---- Index helpers ----
    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    # ---- Heapify helpers ----
    def heapify_up(self, index: int) -> None:
        while index > 0:
            p = self._parent(index)
            if self.data[index] < self.data[p]:
                self.data[index], self.data[p] = self.data[p], self.data[index]
                index = p
            else:
                break

    def heapify_down(self, index: int) -> None:
        n = len(self.data)
        while True:
            left = self._left(index)
            right = self._right(index)
            smallest = index

            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right

            if smallest != index:
                self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
                index = smallest
            else:
                break

    # ---- Public API ----
    def insert(self, patient: Patient) -> None:
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self) -> Patient:
        if not self.data:
            raise IndexError("peek from empty heap")
        return self.data[0]

    def remove_min(self) -> Patient:
        if not self.data:
            raise IndexError("remove_min from empty heap")
        minimum = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return minimum

    def print_heap(self) -> None:
        print("Current Queue:")
        for p in self.data:
            print(f"- {p.name} ({p.urgency})")

    def __len__(self) -> int:
        return len(self.data)


if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient(name="Jordan", urgency=3))
    heap.insert(Patient(name="Taylor", urgency=1))
    heap.insert(Patient(name="Avery", urgency=5))
    heap.print_heap()

    next_up = heap.peek()
    print("Next up:", next_up.name, next_up.urgency)

    served = heap.remove_min()
    print("Served:", served.name)
    heap.print_heap()
