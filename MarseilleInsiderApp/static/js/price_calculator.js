document.addEventListener("DOMContentLoaded", function () {
            var participantsValue = document.getElementById("participantsValue");
            var decreaseButton = document.getElementById("decreaseParticipants");
            var increaseButton = document.getElementById("increaseParticipants");
            var prixTotalElement = document.querySelector(".prix-total");
            var prixUnitaire = parseFloat(document.getElementById('loisir-data').getAttribute('data-prix-fournisseur'));
            function updatePrixTotal() {
                let currentValue = parseInt(participantsValue.textContent);
                prixTotalElement.textContent = "Prix total pour " + currentValue + " participants : " + (currentValue * prixUnitaire) + "€";
            }

        decreaseButton.addEventListener("click", function () {
            var currentValue = parseInt(participantsValue.textContent);
            if (currentValue > 1) {
                participantsValue.textContent = currentValue - 1;
                updatePrixTotal();
            }
        });

        increaseButton.addEventListener("click", function () {
            var currentValue = parseInt(participantsValue.textContent);
            participantsValue.textContent = currentValue + 1;
            updatePrixTotal();
        });
    });