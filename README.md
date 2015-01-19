-  Creates a class FrozenDict that behaves like a dictionary, except all the mutable methods are removed.
-  Compatible with both Python2 and Python3.
-  A temp dict is created, the "read-only" bound methods are saved, then the temp dict is deleted.
-  Like a tuple, FrozenDict is hashable if and only if all its items are hashable
-  All the equality and comparison operators behave just like a normal dictionary.
-  FrozenDict is bidirectional, dict(FrozenDict(*args, **kw)) == dict(*args, **kw)
-  Methods such as copy() and fromkeys() return an instance of FrozenDict
-  FrozenDict is NOT a subclass of dict, so users cannot do a workaround such as dict.__delitem__(obj, key)