var signup_btn = document.querySelector('#submit')
// var verify_btn = document.querySelector('#verify_btn')

// signup form data
var s_n1 = document.querySelector('#name')
var s_n2 = document.querySelector('#company')
var s_email = document.querySelector('#email')
var s_cno = document.querySelector('#contact_no')
var s_p1 = document.querySelector('#designation')
var s_p2 = document.querySelector('#remarks')

signup_btn.addEventListener('click', (e) => {
    e.preventDefault()
    signup_btn.disabled = true

    fetch("/speakers/new_speaker/add", {
        method: 'POST',
        body: JSON.stringify({
            name: s_n1.value,
            company: s_n2.value,
            email: s_email.value,
            designation: s_p1.value,
            contact_no: s_cno.value,
            remarks : s_p2.value
        })
    })
        .then(d => {
            signup_btn.innerHTML = 'Submit'
            signup_btn.disabled = false

            console.log(d)
            return d.json()
        })
        .then(d => {
            console.log('hereeee')
            console.log(d)
            if (d.success) {
                // close_modals()
                alert('Congratulations!!! You have successfully added speaker details.')
                // l_cont.classList.add('show')
            } else {
                console.log('here')
                console.log(d)
                alert(d.message)
            }
        })
})
