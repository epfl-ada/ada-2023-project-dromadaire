
function opacityCmp(scrollY, cutOff, maxOpacity=0.95){
    let clip = scrollY < cutOff ? scrollY : cutOff;
    let opacity = (1.0/cutOff) * clip;
    if (opacity > maxOpacity) {
        return maxOpacity;
    } else {
        return opacity;
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementsByClassName("w")[0]
    const title = document.getElementById("logo-div")
    const maxOpacity = 0.95;
    const cutOff = window.innerHeight*0.75;
    var oldScrollY = window.scrollY;

    // Make sure that if we have above 75% of the screen, the opacity is 1
    if(window.scrollY > window.innerHeight*0.75) {
       element.style.opacity = maxOpacity.toString();
    }

    //if(element.style.opacity == "") {
    //    element.style.opacity = "0.0";
    //}
    
    document.addEventListener("scroll", function(e) {
        if(window.scrollY < cutOff) {
            let opacity = opacityCmp(window.scrollY, cutOff);
            element.style.opacity = opacity.toString();
            title.style.opacity = (1-opacity).toString();
        } else {
            // Make sure the opacity is max
            element.style.opacity = maxOpacity.toString();
        }

        oldScrollY = window.scrollY;
    });

    window.addEventListener("popstate", function(e) {
        console.log(e);   
    });
});