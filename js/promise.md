# Promise

```
const promise = new Promise((resolve, reject) => {

})

Promise.resolve()
Promise.reject()


const promise = new Promise((resolve, reject) => {
    resolve(3)
})

promise
.then((msg) => {
    console.log(msg, 'success')
    return msg
})
.then((msg) => console.log(msg, 'success2'))
.catch((err) => console.error(err, 'error'))
```
