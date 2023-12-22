document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementsByClassName("w")[0]
    const title = document.getElementById("logo-div")
    const maxOpacity = 0.95;
    var oldScrollY = window.scrollY;

    // Make sure that if we have above 75% of the screen, the opacity is 1
    if(window.scrollY > window.innerHeight*0.75) {
       element.style.opacity = maxOpacity.toString();
    }

    //if(element.style.opacity == "") {
    //    element.style.opacity = "0.0";
    //}


    
    document.addEventListener("scroll", function(e) {
        if(window.scrollY < window.innerHeight*0.75) {
            const opacity = parseFloat(element.style.opacity);
            var newOpacity = 1/(window.innerHeight*0.75) * window.scrollY;
            if(newOpacity <= maxOpacity) {
                element.style.opacity = newOpacity.toString();
            }
            title.style.opacity = (1-newOpacity).toString();
        } else {
            // Make sure the opacity is 1
            element.style.opacity = maxOpacity.toString();
        }

        oldScrollY = window.scrollY;
    });

    window.addEventListener("popstate", function(e) {
        console.log(e);   
    });
});