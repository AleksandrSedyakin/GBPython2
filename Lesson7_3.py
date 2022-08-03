class Cell:
    def __init__(self, num_of_slots):
        """num_of_slots = int"""
        self.num_of_slots = num_of_slots

    def __add__(self, other):
        return Cell(self.num_of_slots + other.num_of_slots)

    def __sub__(self, other):
        if self.num_of_slots - other.num_of_slots > 0:
            return Cell(self.num_of_slots - other.num_of_slots)
        elif other.num_of_slots - self.num_of_slots > 0:
            return Cell(other.num_of_slots - self.num_of_slots)
        else:
            print('Разность количества ячеек двух клеток менее 1')

    def __mul__(self, other):
        return Cell(self.num_of_slots * other.num_of_slots)

    def __truediv__(self, other):
        return Cell(self.num_of_slots // other.num_of_slots)

    def make_order(self, Cell_obj, num_of_slots_in_line):

        if Cell_obj.num_of_slots // num_of_slots_in_line > 0:
            str1 = f"{'*' * num_of_slots_in_line}\n"
            str2 = f"{str1 * (Cell_obj.num_of_slots // num_of_slots_in_line)}"
            return f"{str2}{'*' * (Cell_obj.num_of_slots % num_of_slots_in_line)}"
        else:
            return f"{'*' * Cell_obj.num_of_slots}"

cell = Cell(12)
print(cell.make_order(cell, 5))
