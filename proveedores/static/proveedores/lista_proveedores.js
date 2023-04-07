document.addEventListener("DOMContentLoaded", function() {
    // Agregar sombra a las cards
    var cards = document.querySelectorAll(".card");
    cards.forEach(function(card) {
        card.style.boxShadow = "0px 3px 3px rgba(0, 0, 0, 0.1)";

        card.addEventListener("mousemove", function(e) {
            // Obtener la posición del cursor relativa a la card
            var rect = card.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;

            // Mover la sombra de la card en la dirección opuesta al movimiento del cursor
            var shadowOffset = 10;
            var shadowX = (x - rect.width / 2) * 0.1;
            var shadowY = (y - rect.height / 2) * 0.1;
            card.style.boxShadow = "0px 3px 3px rgba(0, 0, 0, 0.1), " + -shadowX + "px " + -shadowY + "px " + shadowOffset + "px rgba(0, 0, 0, 0.2)";

            // Levantar la card
            card.style.transform = "translate3d(0, -1px, 0)";

            // Cambiar el cursor cuando pasa sobre la card
            card.style.cursor = "pointer";
        });

        card.addEventListener("mouseleave", function() {
            // Quitar la sombra adicional y volver a la posición original de la card
            card.style.boxShadow = "0px 3px 3px rgba(0, 0, 0, 0.1)";
            card.style.transform = "none";

            // Restablecer el cursor cuando sale de la card
            card.style.cursor = "default";
        });
    });
});
