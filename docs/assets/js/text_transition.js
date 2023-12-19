// Parse the value of the translateX property
// strin should look like "translateX(123px)"
function parseTranslateX(str){
    const match = str.match(/translateX\(([\d.]+)px\)/);
    const integerValue = parseInt(match[1], 10);
    return integerValue;
}

var maxPx = 0;

function getFirstMaxPx(parsed) {
    if(parsed > maxPx){
        maxPx = parsed;
        console.log("New maxpPx: " + maxPx.toString());
    } else {
        console.log("Max is not bigger");
    }
}

// Map a value in a given interval to another interval
function mapValue(value) {
    const [fromMin, fromMax] = [0, maxPx]; // TODO: make sure this doesn't change from device to device
    const [toMin, toMax] = [1,2];
  
    // Ensure the value is within the source interval
    const clampedValue = Math.min(Math.max(value, fromMin), fromMax);
  
    // Calculate the mapped value in the target interval
    const mappedValue = (clampedValue - fromMin) * (toMax - toMin) / (fromMax - fromMin) + toMin;
  
    return mappedValue;
}


// Wait for the DOM to be loaded
document.addEventListener("DOMContentLoaded", function() {
    
    console.log("Window width" + window.innerWidth.toString())

    // Observe mutations on the sidebar to sync our animation to it
    const target = document.getElementById('_sidebar');
    
    // Create a new MutationObserver with the callback function
    const observer = new MutationObserver(function(mutations){
        for (const mutation of mutations) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
                // Get the current translateX value, map it to the interval [1,2] and invert it (bigger the translation, smaller the scale)
                const int = parseTranslateX(mutation.target.style.transform);
                getFirstMaxPx(int);
                const mapped = 3 - mapValue(int);

                // Set the scaling of the div containing the icon, title and subtitle to the mapped value
                const about = document.getElementsByClassName("sidebar-sticky")[0]
                about.style.transform = `scale(${mapped})`;
            }
          }
    });
    
    // Configure the observer to watch for attribute changes
    const observerConfig = { attributes: true, attributeFilter: ['style'] };
    
    // Start observing the target element
    observer.observe(target, observerConfig);
});