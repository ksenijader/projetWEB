$(function() {
    $("#searchInput").autocomplete({
        source: "/autocomplete/",
        minLength: 1,
        select: function(event, ui) {
            // Redirect to the selected pack's page

            window.location.href = "/pack/" + ui.item.id + "/";}
    });
});