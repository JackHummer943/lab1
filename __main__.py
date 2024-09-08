import json


class ModelDM:
    def __init__(self) -> None:
        self.EPSILON = 0.001

    @property
    def table(self):
        with open('table.json') as file:
            return json.load(file)

    @property
    def N(self):
        return len(self.table)

    def nonlinear_equation(self):
        for B in range(10000000):
            B = B + 1
            f_left = self.left_nonlinear_equation(B)
            f_right = self.right_nonlinear_equation(B)

            modules = abs(abs(f_left) - abs(f_right))

            if modules < 0.001:
                return B

    def left_nonlinear_equation(self, B):
        result = 0
        for i in range(self.N):
            try:
                equation = 1 / (B - (i + 1) + 1)
            except ZeroDivisionError:
                continue
            else:
                result += equation

        return result

    def right_nonlinear_equation(self, B):
        sum_xi = sum([data['xi'] for data in self.table])
        sum_ix = sum([(i + 1) * data['xi'] for i, data in enumerate(self.table)])

        numerator = self.N * sum_xi
        denominator = (B + 1) * sum_xi - sum_ix
        equation = numerator / denominator

        return equation

    def ratio_K(self, B):
        sum_ = sum([(B - (i + 1) + 1) * data['xi'] for i, data in enumerate(self.table)])

        equation = self.N / sum_

        return equation


model_dm = ModelDM()
B = model_dm.nonlinear_equation()
K = model_dm.ratio_K(B)
print(B,'\n', K)


# with open('table.json') as file:
#     table = json.load(file)

# N = len(table)
# EPSILON = 0.001

# def left(B):
#     result = 0
#     for i in range(N):
#         try:
#             foo = 1 / (B - (i + 1) + 1)
#         except ZeroDivisionError:
#             continue
#         else:
#             result += foo

#     return result


# def right(B):
#     sum_xi = sum([data['xi'] for data in table])
#     sum_ix = sum([(i + 1) * data['xi'] for i, data in enumerate(table)])

#     foo = N * sum_xi
#     bar = (B + 1) *sum_xi - sum_ix
#     baz = foo / bar

#     return baz


# for B in range(10000000):
#     B = B + 1
#     f_left = left(B)
#     f_right = right(B)

#     modules = abs(abs(f_left) - abs(f_right))

#     if modules < 0.001:
#         print(f'{B} - great!')
#         break

# try:
#     assert f_left == f_right
# except AssertionError:
#     continue
# else:
#     print(B)
