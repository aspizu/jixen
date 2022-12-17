# jixen
jixen is a pre-processor for JavaScript which converts inline HTML expressions into 
actual JavaScript code which when executed will return the HTML element using the DOM 
API.

## Usage
**Install dependencies using pip**

`pip install -r requirements.txt`

**Run jixen on your code**

`python jixen in.js out.js`

## Examples

**Input:**
```js
const v = `<button onclick={console.log('Hello')}>"Hello"</button>`
document.body.append(v)
```

**Output:**
```js
const v = (() => {
  let e = document.createElement('button')
  e.append('Hello')
  e.addEventListener('click', () => {
    console.log('Hello')
  })
  return e
})()
document.body.append(v)
```

## Documentation
see [~/DOCS.md](DOCS.md)
