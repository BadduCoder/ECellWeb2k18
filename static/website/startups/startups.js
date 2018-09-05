var startups_div = document.querySelector('#startups')
var spinner = document.querySelector('#spinner')

var startups = []
var regsitered_startups = []

fetch('/startups/userstartups')
    .then(d => d.json())
    .then(d => {
        regsitered_startups = d.id
        update_color()
    })
    .catch(err => console.error(err))

fetch('/startups/list/')
    .then(d => d.json())
    .then(d => {
        spinner.remove()
        startups = d.startups
        create_startups(startups)
    })
    .catch(err => console.error(err))

create_startups = (items) => {
    items.forEach((i) => {
        startups_div.innerHTML += `
        <div class=startup>
            <div class='iholder'>
                <img src=${i.pic}>
            </div>
            <button class='more' data-id=${i.id}>read more</button>
        </div>
        `
    })

    // this adds the event listeners for more btn
    startup_modal()
}