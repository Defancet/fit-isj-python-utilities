#!/usr/bin/env python3
def first_with_given_key(iterable, key=lambda x: x):
    result = []
    for iter_object in range(len(iterable)):
        if key(iterable[iter_object]) not in result:
            yield iterable[iter_object]
            result.append(key(iterable[iter_object]))
    del result

if __name__ == "__main__":
    print(tuple(first_with_given_key([[1], [2, 3], [4], [5, 6, 7], [8, 9]], key=len)))
