import numpy as np
# # Absolute imports:
# from Python_Scrips_Modules_CH01.Parte01.matrix_operations import matrix_sum
# # Relative imports
from .matrix_operations import matrix_sum



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