import numpy as np
# # Absolute imports:
# from Python_Scrips_Modules_CH01.matrix_pack import matrix_sum
# from Python_Scrips_Modules_CH01.matrix_pack import main as ml
# Relative imports:
# from .matrix_pack import matrix_sum
# # from .matrix_pack import main as ml
# from .matrix_pack.matrix_operations import matrix_sum
# from .matrix_pack.matrix_pack import main as ml
from .matrix_pack.matrix_operations import matrix_sum
print('hola')



def main():
    a1 = np.array([[1.2, 1.3, 1.4],
                   [2.1, 2.2, 2.3],
                   [3.1, 3.2, 3.3]])
    a2 = np.array([[1.2, 1.3, 1.4],
                   [2.1, 2.2, 2.3],
                   [2.1, 2.2, 2.3]])
    ans = matrix_sum(a1, a2)

    print(ans)

    # ml()
    return 0


if __name__ == '__main__':
    print('run as python -m directory.script_name.py')
    main()