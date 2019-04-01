# -----------------------------
# separating a string with a delimeter
example = 'a/b/c/d'
print(example.split('/'))
# output: ['a', 'b', 'c', 'd']

print('/'.join(example.split('/')[2:]))
# output: c/d


# -----------------------------
# replacing the last character of a string
print(example[:-1] + 'e')


# -----------------------------
# formatting string with variable placer
example = """
    SELECT * FROM {table}
    WHERE id = '{id}';
"""

print(example.format(table="students", id="123"))
