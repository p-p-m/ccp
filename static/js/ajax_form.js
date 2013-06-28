jQuery(function() {
    var form = jQuery("#contactform");
    form.submit(function(e) {
        jQuery("#sendbutton").attr('disabled', true)
        form.find('input').attr('disabled', true);
        form.find('textarea').attr('disabled', true);

        jQuery("#sendwrapper").prepend('<span>Sending message, please wait... </span>')
        jQuery("#ajaxwrapper").load(
            form.attr('action') + ' #ajaxwrapper',
            form.serializeArray(),
            function(responseText, responseStatus) {
                jQuery("#sendbutton").attr('disabled', false);
                form.find('input').attr('disabled', false);
                form.find('textarea').attr('disabled', false);
                jQuery("#sendwrapper").find('span').remove();
            }
        );
        e.preventDefault(); 
    });
});
