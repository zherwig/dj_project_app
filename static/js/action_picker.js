let element = document.getElementById('id_task');
    element.setAttribute("data-live-search", "true");
    element.classList.add("selectpicker");
    let options = element.getElementsByTagName("option")
    console.log(options)
    for (i = 0; i < options.length; i++) {
        let value = options[i].getAttribute("value")
        options[i].removeAttribute("value")
        if (value) {
            options[i].setAttribute("data-tokens", value)
        } else {
            options[i].setAttribute("data-tokens", "none")
        }
            
    }
