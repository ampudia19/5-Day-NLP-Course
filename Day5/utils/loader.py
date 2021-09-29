import pandas as pd

def dataLoad(file, cols, types):
    '''
    Loads data chunks, 100,000 observations at a time. 
    Works for a subset of variables.
    
    '''
    # Empty list to grow
    tmp_lst = []
    
    try:
        for chunk in pd.read_csv(
            file,                      # Argument: File passed to function
            error_bad_lines=False,     # Argument: Prevent breaking on wrongly encoded lines
            low_memory=False,          # Argument: CPU-exhaustive
            usecols=cols,              # Argument: Columns to use
            dtype=types,               # Argument: Types for columns
            parse_dates=['date'],      # Argument: Pass column as datetime
            chunksize=100000           # Argument: Chunksize
        ):
            tmp_lst.append(chunk)      # Argument: Append each chunk to the empty list 
            
    except MemoryError as e:           # Failsafe: If local machine runs out of memory, give error
        print(e)
    except ValueError as e:            # Failsafe: If local machine reads something not in correct format, return Value error
        print('Load Error: ', e)
        
    news_df = (
        pd.concat(tmp_lst, axis=0)     # Argument: Concatenate all the chunkjs in list
    )

    return news_df