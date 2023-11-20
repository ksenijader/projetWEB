// script.js
// script.js

document.addEventListener("DOMContentLoaded", function() {
    var categoryButton = document.querySelector(".category-button");
    var categoryLinks = document.querySelectorAll(".category-link");

    // Récupérer la clé de la catégorie actuellement sélectionnée
    var currentCategoryKey = window.location.pathname.split("/activities/")[1].slice(0, -1);

    // Trouver le libellé correspondant à la clé de la catégorie actuelle
    var currentCategoryLabel = "";
    categoryLinks.forEach(function(link) {
        if (link.getAttribute("data-category") === currentCategoryKey) {
            currentCategoryLabel = link.textContent;
        }
    });

    // Mettre à jour le texte du bouton avec la catégorie actuelle
    categoryButton.textContent = currentCategoryLabel;

    categoryLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault();

            // Mettre à jour le texte du bouton
            categoryButton.textContent = event.target.textContent;

            // Récupérer l'URL de la page correspondante
            var pageUrl = event.target.getAttribute("data-url");

            // Rediriger vers la page correspondante
            window.location.href = pageUrl;
        });

        // Ajouter la classe "selected" au lien de la catégorie actuellement sélectionnée
        if (link.getAttribute("data-category") === currentCategoryKey) {
            link.classList.add("selected");
        } else {
            link.classList.remove("selected");
        }
    });
});
