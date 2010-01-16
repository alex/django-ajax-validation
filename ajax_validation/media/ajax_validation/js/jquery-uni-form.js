function uniform_callback(data, form) {
    var field_divs = $(form).find(".ctrlHolder").filter(".error");
    field_divs.removeClass("error");
    field_divs.find(".errorField").remove();

    $.each(data.errors, function(key, val) {
        var field_div = $(form).find(".ctrlHolder").filter("#div_" + key);
        field_div.addClass("error");
        field_div.prepend('<p id="error_1_' + key + '" class="errorField">'
            + val + '</p>');
    });
}

