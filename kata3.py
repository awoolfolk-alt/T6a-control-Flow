for aisle in range(1, 4):
    for shelves in range(1, 5):
        #adding the "end="" clause caused the formula to stake horizontally instead of vertically.
        print(f"[A{aisle}-S{shelves}]", end=" ")
    print()