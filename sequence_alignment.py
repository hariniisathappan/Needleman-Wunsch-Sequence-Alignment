"""
===========================================================
Sequence Alignment using Needleman-Wunsch Algorithm
===========================================================

Author: Harinii Sathappan

Description:
This project implements global sequence alignment, a fundamental
bioinformatics algorithm used to compare DNA/protein sequences.

This concept is analogous to spectral matching in hyperspectral
image analysis.

===========================================================
"""

import numpy as np

def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n = len(seq1)
    m = len(seq2)

    # Initialize matrix
    score = np.zeros((n+1, m+1))

    for i in range(n+1):
        score[i][0] = i * gap
    for j in range(m+1):
        score[0][j] = j * gap

    # Fill matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            match_score = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete = score[i-1][j] + gap
            insert = score[i][j-1] + gap

            score[i][j] = max(match_score, delete, insert)

    return score


def main():
    print("=== Sequence Alignment (Needleman-Wunsch) ===\n")

    seq1 = "ATGCT"
    seq2 = "AGCT"

    matrix = needleman_wunsch(seq1, seq2)

    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)

    print("\nAlignment Score Matrix:\n")
    print(matrix)

    print("\nFinal Alignment Score:", matrix[-1][-1])


if __name__ == "__main__":
    main()