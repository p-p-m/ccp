$(document).ready(function() { 
    // bind 'myForm' and provide a simple callback function
    var form = $("#contactform");
    form.ajaxForm({
            beforeSubmit: function() { 
                $("#sendbutton").attr('disabled', true);
                form.find('input').attr('readonly', true);
                form.find('textarea').attr('readonly', true);
                $("#sendwrapper").prepend('<span>Sending message, please wait... </span>')
            },
            success: function(data) {
                $("#sendbutton").attr('disabled', false);
                form.find('input').attr('readonly', false);
                form.find('textarea').attr('readonly', false);
                $("#sendwrapper").find('span').remove();
                form.html(data);
            }
        }
    ); 
}); 