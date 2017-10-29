def get_change_as_string(change):
    if change > 0:
        return "+{}".format(change)
    else:
        return "{}".format(change)

def get_change_in_ranking(rank, previous_rank):
    return previous_rank - rank

def get_value2ranks(values):
    values = list(set(values))
    values.sort()
    value2ranks = {}
    for i, value in enumerate(values[::-1]):
        value2ranks[value] = i + 1    
    return value2ranks

def main():
    values          = [10,  8, 7, 4, 5, 6, 2]
    previous_values = [ 8, 10, 5, 6, 6, 4, 8]

    value2ranks           = get_value2ranks(values[:])
    previous_values2ranks = get_value2ranks(previous_values[:])

    print("=" * 41)
    print("| Value  | Rank | Chg. | P. Va. | Rank |")
    print("=" * 41)
    
    for value, previous_value in zip(values, previous_values):
        
        rank = value2ranks[value]
        
        previous_rank = previous_values2ranks[previous_value]
            
        change = get_change_in_ranking(rank, previous_rank) 
        print("| {:6d} | {:4d} | {:>4s} | {:6d} | {:5d} |".format(value,
                                                                  value2ranks[value],
                                                                  get_change_as_string(change),
                                                                  previous_value,
                                                                  previous_values2ranks[previous_value]))
    print("=" * 41)

if __name__ == "__main__":
    main()
