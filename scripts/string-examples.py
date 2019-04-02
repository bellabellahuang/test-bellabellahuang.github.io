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


# -----------------------------
# converting http payload string to key-value dictionary
def convertParamsToDict(req_string):
    req_dict = {}
    for val in req_string.split('&'):
        k, v = val.split('=')
        req_dict[k] = v
    return req_dict
