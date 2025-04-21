list_items = []

try:
    num_items = int(input())
    for i in range(num_items):
        curr_item = int(input())
        list_items.append(curr_item)

    max_item = list_items[0]
    for item in list_items:
        if item > max_item:
            max_item = item

    print(max_item)
except EOFError:
    # Handle the case when no input is provided
    print("No input provided.")


