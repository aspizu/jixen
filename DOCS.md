# Documentation for jixen

## Examples for inline-HTML to Javascript
```html
<div></div>
```
```js
(()=>{let e=document.createElement("div");return e;})()
```

```html
<div class="class1 class2" id="id1"></div>
```
```js
(()=>{let e=document.createElement("div");e.classList+=" "+'class1 class2';e.id='id1';return e;})()
```

```html
<div>
  <span>"Hello"</span>
  <p>{content}</p>
</div>
```
```js
(()=>{let e=document.createElement("div");e.append((()=>{let e=document.createElement("span");e.append('Hello');return e;})());e.append((()=>{let e=document.createElement("p");e.append(content);return e;})());return e;})()
```

```html
<button onclick={alert("hey")} oninput={alert("hey")}>"Hey"</button>
```
```js
(()=>{let e=document.createElement("button");e.append('Hey');e.addEventListener("click",()=>{alert("hey")});e.addEventListener("input",()=>{alert("hey")});return e;})()
```

```html
<{Foo("bar")} class="foo"></anythinggoeshere>
```
```js
(()=>{let e=Foo("bar");e.classList+=" "+'foo';return e;})()
```

## How to include inline-HTML in Javascript

```js
/* This example creates a button which when clicked will increment the number in itself */

function CounterButton() {
  return `<button onclick = { e.textContent += 1 }>"1"</button>`
}

document.body.append(`<CounterButton()></CounterButton>`)
```
