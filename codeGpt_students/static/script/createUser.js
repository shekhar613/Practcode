// on create user data submite
console.log("create users js linked...")
$(document).on('submit', '#post-createuser_form', function (e) {
    e.preventDefault();
 
    $.ajax({
        type: 'POST',
        url:'/auth2',
        data: {
            
            name:$('#username').val(),
            email: $('#email').val(),
            contact:$('#contact').val(),
            collegeName:$('#college').val(),
            year:$('#year').val(),
            courseName:$('#course').val(),
            password: $('#password').val(),


            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            // data = $.parseJSON(data);
            console.log(data)


        }
    })
})

