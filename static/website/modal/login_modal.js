// close login modal
login_modal_close_btn.addEventListener('click', (e) => {
    e.preventDefault()

    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    login_modal.style.top = '-100vh'
})

// show login model
login_trigger.addEventListener('click', (e) => {
    e.preventDefault()
    // if logged in show logout modal
    if (localStorage.ecell_nitrr_user) {
        show_logout_modal()
        return
    }
    // hide other models
    modal_bg.forEach(m=> m.style.top="-100vh")
    // show the model

    body.style['overflow'] = 'hidden'
    body.style.height = '100vh'
    login_modal.style.top = 0
})

// do login req
login_btn.addEventListener('click', (e) => {
    e.preventDefault()
    commence_login()
})

commence_login = () => {
    console.log('login req sent')
    console.log(lemail.value, lpass.value)
    login_btn.innerHTML = '<i class="fa fa-2x fa-spinner fa-spin"></i>';
    login_btn.disabled = true

    fetch('login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        body: JSON.stringify({
            'email': lemail.value,
            'password': lpass.value,
            // 'email': 'mitsum@gmail.com',
            // 'password': 'ldappass',
        })
    })
        .then(response => response.json())
        .then(data => {
            login_btn.innerHTML = 'login'
            login_btn.disabled = false

            if (data.success) {
                login_success_handler()
            } else {
                login_failure_hander()
            }
        })
        .catch(error => console.error('fetch error', error))
}

login_success_handler = () => {
    body.style['overflow'] = 'none'
    body.style.height = 'auto'
    login_modal.style.top = '-100vh'
    // change btn text from login to logout
    login_trigger.innerText='logout'
    // store the cookie
    loggedin_user.innerText = lemail.value.split('@')[0]
    localStorage.ecell_nitrr_user = lemail.value
}

login_failure_hander = () => {
    modal_h2.innerText = 'incorrect email/password'
    modal_h2.style.color = 'red'
    lemail.value = ''
    lpass.value = ''
    lpass.removeAttribute.style
}
