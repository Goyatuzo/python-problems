import operator

def difference(n):
    """This problem was optimized for the HackerRank interface. Since there will
    be multiple values being passed in, rather than computing the differences for
    each and every value, it would be more efficient to compute the difference for
    the largest value, then store all intermediate entries in an array and reference
    them when returning the final value. This takes up unnecessary space, but is easy
    to implement. The more space efficient version would only append to the output list
    when the i-th iteration is a value in the input n.
    :param n: The list of numbers to evaluate the sum square difference."""
    differences = []

    # Map all values of n to int.
    n = map(int, n)
    # First evaluate the sum square difference of the highest value in the list.
    highest = max(n)

    # Keep track of each point in the iteration to make computation simpler.
    sum_square = 0
    square_sum = 0

    for i in range(1, highest+1):
        sum_square += i ** 2
        square_sum += i

        differences.append(square_sum ** 2 - sum_square)

    return [differences[i-1] for i in n]