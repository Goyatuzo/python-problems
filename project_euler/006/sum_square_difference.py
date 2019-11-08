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

    # sum of the squares
    sum_of_squares = (1 / 6) * n * (1 + n) * (1 + 2 * n)
    
    # square of the sums
    sum_base = (1 / 2) * n * (n + 1)
    square_of_sums = sum_base ** 2

    # Diff between sum of squares and square of the sum
    return abs(int(sum_of_squares - square_of_sums))

if __name__ == '__main__':
    print(difference(100))