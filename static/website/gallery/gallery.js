var gallery = document.querySelector('#gallery')
var spinnner = document.querySelector('#spinner')

fetch('/gallery_api/').then(d => d.json())
    .then(d => {
        console.log(d)
        spinnner.parentNode.removeChild(spinnner)
        d.forEach((ele,i) => {
            gallery.innerHTML += `
<h5 class="category_title">
   <a href="/gallery/${i}/">${ele.name}</a>                 
</h5>
            `
        })
    })


