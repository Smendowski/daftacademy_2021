Sample Triangle:
```
     7
    2 5
   4 8 2
```

We treat it as:

```
  START
   2 5
  4 8 2
    7 
  (END)
```

Expected Result after algorithm:
```
graph = {
    'START': {'2_1': 2, '2_2': 5}, 
    '2_1': {'2_2': 5, '3_1': 4, '3_2': 8}, 
    '2_2': {'2_1': 2, '3_2': 8, '3_3': 2}, 
    '3_1': {'3_2': 8, 'END': 7}, 
    '3_2': {'3_1': 4, '3_3': 2, 'END': 7},
    '3_3': {'3_2': 8, 'END': 7},
    'END': {}
    }

cost = {'START': 0, '2_1': inf, '2_2': inf, '3_1': inf, '3_2': inf, '3_3': inf, 'END': inf}
```