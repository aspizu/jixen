# jixen
jixen is a pre-processor for JavaScript which converts inline HTML expressions into 
actual JavaScript code which when executed will return the HTML element using the DOM 
API.

[![State-of-the-art Shitcode](https://img.shields.io/static/v1?label=State-of-the-art&message=Shitcode&color=7B5804)](https://github.com/trekhleb/state-of-the-art-shitcode)

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
