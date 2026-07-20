#!/usr/bin/env python3
import sys

def solve() -> None:
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.readline

    t_line = input()
    if not t_line:
        return
    t = int(t_line)
    out_lines = []
    for _ in range(t):
        line = input()
        while line.strip() == '':
            line = input()
        n = int(line)
        a = list(map(int, input().split()))
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for i in range(n - 1):
            u = i
            v = i + 1
            w = a[i] ^ a[i + 1]
            adj[u].append((v, w))
            adj[v].append((u, w))
        # Compute XOR from root (0) to all nodes
        xor_to = [0] * n
        visited = [False] * n
        stack = [0]
        visited[0] = True
        while stack:
            u = stack.pop()
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    xor_to[v] = xor_to[u] ^ w
                    stack.append(v)
        # Count frequencies
        freq = {}
        for val in xor_to:
            freq[val] = freq.get(val, 0) + 1
        # Find max frequency
        max_freq = 0
        for cnt in freq.values():
            if cnt > max_freq:
                max_freq = cnt
        # Answer
        out_lines.append(str(n - max_freq))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
