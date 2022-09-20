console.log('hi')

const data = fetch("https://rickandmortyapi.com/api/character")
.then(res => res.json())
.then(res => res.results.forEach(element => {
    document.write(`<p>${element.name}</p>`)
}))

console.log(data.results)