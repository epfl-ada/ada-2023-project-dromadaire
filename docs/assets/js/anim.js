document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementsByClassName("w")[0]
    console.log(element);

    var oldScrollY = 0;

    if(element.style.opacity == "") {
        element.style.opacity = "0.0";
    }
    document.addEventListener("scroll", function(e) {
        
        if(window.scrollY < window.innerHeight*0.75) {
            const opacity = parseFloat(element.style.opacity);
            if(oldScrollY < window.scrollY) { // Scrolling down
                var newOpacity = 1/(window.innerHeight*0.75) * window.scrollY;
                console.log(newOpacity);
                element.style.opacity = newOpacity.toString();
            } else if (oldScrollY > window.scrollY) { // Scrolling up
                var newOpacity = 1 - 1/(window.innerHeight*0.75) * window.scrollY;
                console.log(newOpacity);
                element.style.opacity = newOpacity.toString();
            }
        }
    });
});