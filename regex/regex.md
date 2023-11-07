# Regex with Python


```
Meta characters

* ^ $ * + ? {} [] \ | ()

Any meta character in class is char except \ and ^ at start


\ - escape symbol and \n - meta char
r'' - escape total string

print('\User\nwefwefwef\rwefwefwef') We should escape them all

r'\User\nwefwefwef\rwefwefwef' == '\\User\\nwefwefwef\\rwefwefwef'

If we use re.compile() and we want to escape then
we should escape literal twice or ones + r''
```


```
[] - class

[abc] - any abc

[^abc] - any except abc

\d - any digit = [0-9]  &  \D = [^0-9]

\s - any space = [ \t\n\r\f\v]  &  \S = [^ \t\n\r\f\v]

\w - any word = [a-zA-Z0-9_]  &  \W = [^a-zA-Z0-9_]


{m, n} - repeating

<symbol>* == <symbol>{0,}

<symbol>+ == <symbol>{1,}

<symbol>? == <symbol>{0, 1}
```

```
regex = re.compile(pattern)

regex.match(string) -> lazy object or None from the beginning of a string

regex.search(string) -> lazy object or None from any place

regex.findall(string) -> list of characters or []

regex.finditer(string) -> iterator of objects or empty iterator

```
