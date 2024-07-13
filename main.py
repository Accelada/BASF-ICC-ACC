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
    
    array_length = len(arr)
    
    # ODD LENGTH
    if array_length % 2 != 0:
        if len(set(arr)) == 1:
            return array_length + 1
        
        else:
            return 0
    
    # EVEN LENGTH
    else:
        unique_elements = list(set(arr))
        num_unique_elements = len(unique_elements)
        elements = elements_counter(arr, unique_elements)
        
        num_of_common_subsets = 0
        
        for i in range(array_length):
            ii = i + 1
            if array_length % ii == 0:
                divider = int(array_length / ii)
                list_of_sub_sets = []
                
                for j in range(ii):
                    list_of_sub_sets.append(arr[divider*j:divider*(j+1)])
                
                if ii == 1:
                    if check_same_elements(elements):
                        num_of_common_subsets += ii
                    
                else:
                    same_elements_in_each_sub_set = True
                    for k, sub_set in enumerate(list_of_sub_sets):
                        if k != 0:
                            if elements_counter(sub_set, elements) != elements_counter(list_of_sub_sets[k-1], elements):
                                same_elements_in_each_sub_set = False
                                break
                    
                    if same_elements_in_each_sub_set:        
                        num_of_common_subsets += ii
                            
            else:
                continue
                    
        return num_of_common_subsets
    
def check_same_elements(elements):
    keys = list(elements.keys())
    first_val = elements[keys[0]]
    
    return all(elements[key] == first_val for key in keys)
    
def elements_counter(string, items):
    # Dict initialization
    elements = dict()
    
    for item in items:
        elements[item] = 0
    
    for s in string:
        elements[s] += 1
        
    return elements


if __name__ == "__main__":
    # Challenge 1
    # Example 1
    A = "ADDB"
    B = "CDDE"
    C = "EDDF"
    sequence = longest_common_consecutive_substring(A,B,C)
    print(f"Output challenge 1 - example 1: {sequence}")
    
    # Example 2
    A = "UIBAZDBSIAHFB"
    B = "PQACIZDBIBDLAG"
    C = "QIDBCZDBKSHDVF"
    sequence = longest_common_consecutive_substring(A,B,C)
    print(f"Output challenge 1 - example 2: {sequence}")
    
    # Chanllenge 2
    # Example 1
    colors = ['r', 'r', 'b', 'b', 'g', 'g']
    print(f"Output challenge 2 - example 3: {count_equal_color_subsets(colors)}")
    
    # Example 2
    colors = ['r', 'r', 'b', 'b', 'g']
    print(f"Output challenge 2 - example 3: {count_equal_color_subsets(colors)}")
    
    # Example 3
    colors = ['r', 'b', 'g', 'g', 'b', 'r']
    print(f"Output challenge 2 - example 3: {count_equal_color_subsets(colors)}")