import math
N = 9
M = 8

def show_all_combinations(cont):
    """
    for i in range(0, int(calc_combin()))
    """

def calc_combin():
    return (math.factorial(N + M - 1))/(math.factorial(N - 1) * math.factorial(M))

def main():
    print("mark")
    containers = [] * M
    """
    [][][][][][][][]

    """
    diff_combinations = calc_combin()
    print(show_all_combinations(containers))
    print(diff_combinations)

if __name__ == "__main__":
    main()