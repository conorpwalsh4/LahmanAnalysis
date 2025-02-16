def avoid_overlap(df, threshold=3):
    to_keep = []
    prev_index = -threshold - 1  # Initial value to ensure first row is kept
    
    for index in df.index:
        if index >= prev_index + threshold:
            to_keep.append(index)
            prev_index = index
            
    return df.loc[to_keep]