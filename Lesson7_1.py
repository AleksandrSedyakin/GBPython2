data_list = [[1, 2, 3], [7, 4, 3], [2, 9, 6]]

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        matrix_str = ''
        for el in self.list:
            m_str = ''
            for str in el:
                m_str += f"{str} "
            matrix_str += f"{m_str}\n"
        return matrix_str

    def __add__(self, other):
        num_el = 0
        for el in self.list:
            num_num = 0
            while num_num < len(el):
                el[num_num] += other.list[num_el][num_num]
                num_num += 1
            num_el += 1
        return Matrix(self.list)



my_m = Matrix(data_list)
print(my_m)

my_m2 = Matrix(data_list)
print(my_m + my_m2)

