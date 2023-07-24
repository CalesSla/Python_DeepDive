# Remove prefix/suffix 
data = [
    "(log) [2022-03-01T13:30:01] Log record 1",
    "(log) [2022-03-01T13:30:02] Log record 2",
    "(log) [2022-03-01T13:30:03] Log record 3",
    "(log) [2022-03-01T13:30:04] Log record 4",
    ]

print([s.removeprefix("(log) ") for s in data])
