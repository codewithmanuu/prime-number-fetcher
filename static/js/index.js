$(document).ready(function() {
    $('#prime-form').on('submit', function(event) {
        event.preventDefault(); 

        var formData = {
            'input_number': $('#input_number').val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        };

        $.ajax({
            type: 'POST',
            url: '',  
            data: formData,
            dataType: 'json',
            success: function(response) {
                $('#response').removeClass('alert-danger').addClass('alert alert-success').html('<strong>Success:</strong><br> ' + response.success).fadeIn();
                $('#input_number').val('');
            },
            error: function(xhr) {
                var errors = xhr.responseJSON;
                var errorHtml = '<ul>';
                $.each(errors, function(key, value) {
                    errorHtml += '<li>' + value + '</li>';
                });
                errorHtml += '</ul>';
                $('#response').removeClass('alert-success').addClass('alert alert-danger').html(errorHtml).fadeIn();
                $('#input_number').val('');
            }
        });
    });
});