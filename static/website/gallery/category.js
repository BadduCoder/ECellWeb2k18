const spinner = document.querySelector('#spinner')
const cat_heading = document.querySelector('.cat-heading')
var gallery = document.querySelector(('#lightgallery'))

fetch('/gallery_api/').then(d => d.json())
    .then(d => {
        console.log(d)
        spinner.parentNode.removeChild(spinner)

        data = d[cid]
        cat_heading.innerHTML = data.name

        for (var i = 1; i <= data.count; i++) {
            // <a href="/${data.url+i+'a.jpg'}">
            // <img src="/${data.url+i+'ab.jpg'}">
            // </a>
            gallery.innerHTML += `
          
            <li class="col-xs-6 col-sm-4 col-md-3"
                data-src="/${data.url+i+'a.JPG'}"
                data-sub-html="<h4>${data.name}</h4>"
                data-pinterest-text="Pin it1" data-tweet-text="share on twitter 1">
                <a href="">
                    <img class="img-responsive" src="/${data.url+i+'ab.JPG'}" alt="Thumb-1">
                </a>
            </li>
`
        }

        lightGallery(document.getElementById('lightgallery'));
    })