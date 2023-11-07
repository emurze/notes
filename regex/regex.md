# Regex with Python


```
Meta characters

* ^ $ * + ? {} [] \ | ()

Any meta character in class is char except \ and ^ at start

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
