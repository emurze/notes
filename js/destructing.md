# Destructuring

```
let {next: next_alias, value: value_alias} = get_info()

let [a, b, c] = get_info()

let [,,t] = get_info()

let { next: arg = 20 } = get_info()

let [,f1, f2, [f3, f4, f5]] = get_info()

function function get_info([a, b]) {}


function *foo() {
    yield 3
    yield 4
}
```
