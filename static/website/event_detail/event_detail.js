var event_detail = document.querySelector('#event_detail')
console.log(event_detail)

put_event_in_place = (event) => {
    event_detail.innerHTML += (`
            <article class="container">
                <h2 class="">${event.name}</h2>
                <hr>
                <div class="img ">
                    <img src='${event.cover_pic}' alt=""> </div>
                </div>
                <div class=text>
                    <p><strong>Date: </strong>${event.date}</p>
                    <p><strong>Time: </strong>${event.time}</p>
                    <p><strong>Email: </strong>${event.email}</p>
                    <p><strong>Venue: </strong>${event.venue} on ${event.date} at ${event.time}</p>
                    <p class="text-justify">${event.details}</p>
                    <div class='text-center mt-5'>
                        <button class="register_btn" data-eid=${event.id}>Register</button>
                    </div>
                </div>
            </article>
        `)
}

fetch('/event/list')
    .then(data => data.json())
    .then((data) => {
        // close the spinner
        document.querySelector('#spinner').remove()

        // put the data into place
        var page_eid = window.location.href.split('/').pop()
        var event = data.Events.filter((event) => event.id == page_eid)[0]
        put_event_in_place(event)
        console.log(JSON.stringify(event, null, 2))

    })
    .catch(err => console.error(err))

