$(document).ready(function() {
    $("#id_scenario").change(function() {
        var scenario_id = $("#id_scenario").val();

        url = "/api/character?scenario_id=" + scenario_id;
        $.getJSON(url, function (json) {
            var options = "";
            for (var i = 0; i < json.length; i++) {
                options += '<option value="' + json[i].id + '">' + json[i].name + '</option>';
            }
            $('#id_character').html(options);

        });
    });
});