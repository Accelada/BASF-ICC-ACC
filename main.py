# Interview coding challenge - BASF
# Date: 04/07/2024
# Author: Adrián Celada Celada

# Prerequisites
#-------------------------------------------------------------------------------------------------------
# The following challenges can be solved in any programming language which is popular today (e.g. COBOL
# is not recommended). You can send your source code via email to timo.himmelsbach@basf.com or provide
# a link to a public github repo. Your code may be incomplete or may not work - please hand it in anyway!
#-------------------------------------------------------------------------------------------------------

# Comments:
# Execute this code to see the solution of both exercises.
# Note: challenge 2 is not properly resolved.

#Challenge 1 - Algorithms
#-------------------------------------------------------------------------------------------------------
# Given three ordered arrays of arbitrary length containing random capital letters, write an algorithm which
# returns the longest ordered array which both arrays share!
import numpy as np

def longest_common_consecutive_substring(A, B, C):
    # Creation of a zeros 3D matrix
    la, lb, lc = len(A), len(B), len(C)
    dp = np.zeros((la + 1, lb + 1, lc + 1), dtype=int)
    max_len = 0
    end_pos = (0, 0, 0)

    # Iteration over the entire matrix
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            for k in range(1, lc + 1):
                if A[i-1] == B[j-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    if dp[i][j][k] > max_len:
                        max_len = dp[i][j][k]
                        end_pos = (i, j, k)

    # Rebuilding the string. Reverse iteration
    sequence = []
    i, j, k = end_pos
    while max_len > 0:
        sequence.append(A[i-1])
        i -= 1
        j -= 1
        k -= 1
        max_len -= 1

    sequence.reverse()
    return ''.join(sequence)

#Challenge 2 - Algorithms
#-------------------------------------------------------------------------------------------------------
# Assume an array of arbitrary length whose elements represent colors of the set blue (b), green (g) or red (r).
# Write an algorithm which returns the number of subsets in which the array can be split so that every subset
# contains equal color representations! Remark: The colors do not have to appear in equal order within the
# subsets.

def count_equal_color_subsets(arr):
    n = len(arr)
    
    count_b = count_g = count_r = 0
    prefix_count = {(0, 0, 0): 1}  
    
    total_valid_splits = 0
    
    for i in range(n):
        if arr[i] == 'b':
            count_b += 1
        elif arr[i] == 'g':
            count_g += 1
        elif arr[i] == 'r':
            count_r += 1
        
        current_prefix = (count_b, count_g, count_r)
        
        if current_prefix in prefix_count:
            total_valid_splits += prefix_count[current_prefix]
            prefix_count[current_prefix] += 1
        else:
            prefix_count[current_prefix] = 1
    
    return total_valid_splits

if __name__ == "__main__":
    # Challenge 1
    A = "UIBAZDBSIAHFB"
    B = "PQACIZDBIBDLAG"
    C = "QIDBCZDBKSHDVF"
    sequence = longest_common_consecutive_substring(A,B,C)
    print(f"Output challenge 1: {sequence}")
    
    # Chanllenge 2
    colors = ['r', 'b', 'g', 'g', 'b', 'r']
    print(f"Output challenge 2: {count_equal_color_subsets(colors)}")