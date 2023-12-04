$(document).ready(function() {
    function initializeAutocomplete(category) {
        $("#searchInput").autocomplete({
            source: "/autocompletecat/" + category + "/",
            minLength: 1,
            select: function(event, ui) {
                window.location.href = "/activity/" + ui.item.id + "/";
            }
        });
    }

    var currentURL = window.location.href;
    var categoryMatch = currentURL.match(/\/activities\/([^/]+)\//);
    var initialCategory = categoryMatch ? categoryMatch[1] : null;

    initializeAutocomplete(initialCategory || $(".category-link:first").data("category"));

    $(".category-button").on("change", function() {
        var selectedCategory = $(".category-button").val();

        $("#searchInput").autocomplete("destroy");

        initializeAutocomplete(selectedCategory);
    });
});
