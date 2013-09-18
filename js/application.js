

$(document).ready(function() {
    $("#image").on("click", "img", function() {
        $(this).next("p.description").slideToggle();
    });
});