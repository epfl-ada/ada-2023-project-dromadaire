document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementsByClassName("w")[0]

    var oldScrollY = window.scrollY;

    // Make sure that if we have above 75% of the screen, the opacity is 1
    if(window.scrollY > window.innerHeight*0.75) {
       element.style.opacity = "1.0";
    }

    //if(element.style.opacity == "") {
    //    element.style.opacity = "0.0";
    //}


    
    document.addEventListener("scroll", function(e) {
        if(window.scrollY < window.innerHeight*0.75) {
            const opacity = parseFloat(element.style.opacity);
            var newOpacity = 1/(window.innerHeight*0.75) * window.scrollY;
            element.style.opacity = newOpacity.toString();
        } else {
            // Make sure the opacity is 1
            element.style.opacity = "1.0";
        }

        oldScrollY = window.scrollY;
    });
});

viridis.forEach((rgb, index) => {
    const cssVariableName = `--viridis-${index}`;
    const cssVariableValue = `rgb(${rgb.join(', ')})`;
    styleTag.innerHTML += ` ${cssVariableName}: ${cssVariableValue};`;
});