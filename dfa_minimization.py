import time


def read_input():
    cases = []
    c = int(input().strip())  #numero de casos
    if c <= 0:
        print("El número de casos debe ser mayor que 0.")
    for _ in range(c):
        n = int(input().strip())  #numero de estados
        if n <= 0:
            print("El número de estados debe ser mayor que 0.")
            break
        alphabet = input().strip().split()  #alfabeto
        final_states = set(
            map(int, input().strip().split()))  #estados finales
        transition_table = [] #tabla de transiciones
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            transition_table.append(row[1:])  #ignora el primer numero de cada fila
        cases.append((n, alphabet, final_states, transition_table))
    return cases

def minimize_dfa(n, alphabet, final_states, transition_table):
    distinguishable = [[False] * n for _ in range(n)]
    for p in range(n):
        for q in range(p + 1, n):
            if (p in final_states) != (q in final_states):
                distinguishable[p][q] = True
    changed = True
    while changed:
        changed = False
        for p in range(n):
            for q in range(p + 1, n):
                if not distinguishable[p][q]:
                    for idx in range(len(alphabet)):
                        p_next = transition_table[p][idx]
                        q_next = transition_table[q][idx]
                        x, y = min(p_next, q_next), max(p_next, q_next)
                        if distinguishable[x][y]:  #marca las transiciones distinguibles
                            distinguishable[p][q] = True
                            changed = True
                            break
    equivalent_states = [(p, q) for p in range(n) for q in range(p + 1, n) if not distinguishable[p][q]]
    return equivalent_states


def main():
    cases = read_input()
    for i, (n, alphabet, final_states, transition_table) in enumerate(cases, start=1):
        print(f"\nCaso #{i}:")
        time.sleep(1)
        equivalent_states = minimize_dfa(n, alphabet, final_states, transition_table)
        if equivalent_states:
            print("Estados equivalentes:", " ".join(f"({p},{q})" for p, q in sorted(equivalent_states)))
            time.sleep(1.5)
        else:
            print("Estados equivalentes: Ninguno")
            time.sleep(1.5)
if __name__ == "__main__":
    main()
