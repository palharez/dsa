"""
Time Complexity: O(log(high-low))
"""

# Comparing double values directly is bad practice
# Using a small epsilon value is the preferred approach
EPS = 0.00000001


def binary_search(low, high, target, double):
    if high <= low:
        raise "high should be greate than low"

    mid = 0

    while (high - low) > EPS:
        # Find the middle point
        mid = (high + low) / 2

        # Compute the value of our function for the middle point
        # Note that f can be any function not just the square root function
        value = double(mid)

        if value > target:
            high = mid

        else:
            low = mid

    return mid


if __name__ == "__main__":
    """
    EXAMPLE #1
    Suppose we want to know what the square root of 875 is and
    we have no knowledge of the wonderful Math.sqrt() function.
    One approach is to use a binary search because we know that
    the square root of 875 is bounded in the region: [0, 875].

    We can define our function to be f(x) = x*x and our target
    value to be 875. As we binary search on f(x) approaching
    successively closer values of 875 we get better and better
    values of x (the square root of 875)
    """
    low = 0.0
    high = 875
    target = 875
    def double(x): return x*x

    sqrtVal = binary_search(low, high, target, double)
    print(sqrtVal)
