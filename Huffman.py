import heapq

# Function to print Huffman Codes recursively
def print_codes(tree, code=""):
    if len(tree) == 2:
        # It's a leaf node (character, frequency)
        print(tree[0], ":", code)
        return
    # Internal node: left and right branches
    print_codes(tree[1], code + "0")
    print_codes(tree[2], code + "1")


def huffman_coding(chars, freq):
    # Step 1: Create a min-heap (priority queue)
    heap = [[freq[i], chars[i]] for i in range(len(chars))]
    heapq.heapify(heap)

    # Step 2: Build the Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        # Combine two smallest nodes into one new node
        new_node = [left[0] + right[0], left, right]
        heapq.heappush(heap, new_node)

    # Step 3: Print Huffman Codes
    print("Character : Huffman Code")
    print_codes(heap[0])


# Example input
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

huffman_coding(chars, freq)
