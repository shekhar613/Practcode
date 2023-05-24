// // on logindata submite
console.log("login js linked...")
$(document).on('submit', '#post-form', function (e) {
    e.preventDefault();
    
    // Downloader_section.innerHTML=containt_text;

    $.ajax({
        type: 'POST',
        url:'/login',
        data: {
            email: $('#email').val(),
            password: $('#password').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            data = $.parseJSON(data);
            window.location.replace("/dashboard");

            console.log("aasdfasdfasdf@@@SADSDfg!@XCSDFG")
            


        }
    })
})

