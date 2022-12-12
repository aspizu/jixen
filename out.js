const v = (() => {
  let e = document.createElement('button')
  e.append('Hello')
  e.addEventListener('click', () => {
    console.log('Hello')
  })
  return e
})()
document.body.append(v)
