
document.addEventListener('DOMContentLoaded', function() {
    // Assuming you have an anchor element with id "drawerLink"
    // const drawerLink = document.getElementById('_drawer--opened');
  
    // // Trigger the click event programmatically
    // drawerLink.click();

    document.addEventListener("wheel", function(e) {
        const drawer = document.getElementById('_drawer');
        if (window.scrollY == 0 && !drawer.hasAttribute('opened') && e.deltaY < 0) {
            const drawerLink = document.getElementById('_menu');
            
            // Trigger the click event programmatically
            drawerLink.click();
        }
    })
  });