# UP GOING

```

Equality, Compound asignment, Logical

== - checks value && type
=== - checks value

+= *= -= /=
-- ++

|| &&

.toString()
.valueOf()
.length
typeof ''
instanceof


Primitive values

string
number
boolean
null | undefined
object - array, function(subtype), instance
symbol


Coersion

Implicit
var + ""  +var

Explicit
String() Number()


false - 1. ""
        2. 0, -0, NaN
        3. null, undefined, falses


> or <

['a', 'b'] -> "a,b"
"32" > 43 -> 32 > 43
"32" > "43" -> 32 > 43  - first number
32 > "rferg" -> 32 > NaN


switch (2){
  case ..:
    ...
    break
  case ...:
    break
  default:
    break
}

"use strict"


LIFE functin
(function() {
    // each function creates own scope
})()


func.call(this, a, b, c)
func.apply(this, [args])
func.bind(this, a, b, c) - 1 bind to this, defer-args


new foo() - new empty this


Inheritance via prototype


setTimeout(() => {}, 1000)
setInterval() clearInterval()


build-in objects

String
Number
Boolean
Object
Array
Date
RegExp
Error

() => {} - outer

this - first parent

dublicate - Object.assign( {}, obj )
Object.is(obj1, obj2)

Object.defineProperty(obj, "a", {
    value: 333,
    writable: false, // changeable
    enumerable: false,
    configurable: false, // no-delete
})
Object.preventExtensions(obj) - Immutable


get b() {
    return this._b_
},
set b(value) {
    this._b_ = value
}



let promise = new Promise(() => {})            explicit
let array = []   // new Array() & .valueOf()   implicit
let object = {}  // new Object() & .valueOf()  implicit
let number = 18  // new Number() & .valueOf()  implicit


all(objects & primitives) 1. has __proto__ -> prototype - is object
                          2. created via build-in functions &
                             class & not arrow functions

class | not arrow function  1. has prototype - independent object
                              (String.prototype !== Object.prototype)

Why __proto__ exists? To provide primitive methods. (18).toFixed()


Object.setPrototypeOf(obj2, obj1)
obj2.__proto__ === obj1  // true

function foo() {} function bar() {}
foo.prototype.a = 4
bar.prototype.b = 5
Object.setPrototypeOf(bar.prototype, foo.prototype)
console.log((new bar()).__proto__.__proto__)


String('an apple') -> primitives

console.log((new Number(5)).valueOf() === 5)


new Number(43) -> instance (object) (need for extensive logic)

let number = new Number(333)
number.double_valueOf = function() {return this.valueOf() * 2}



FEATURES


if (typeof DEBUG !== "undefined") {}

(cond) ? res : else_res

?? when null / undefined
|| when falsy


let obj = {
    name,
    func()
}
```
