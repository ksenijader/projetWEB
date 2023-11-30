$(function() {
    $("#searchInput").autocomplete({
        source: "/autocompletebis/",
        minLength: 1,
        select: function(event, ui) {
            // Redirect to the selected pack's page

            window.location.href = "/activity/" + ui.item.id + "/";}
    });
});