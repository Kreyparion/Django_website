window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("logo").style.width = "50px";
        document.getElementById("navbar").style.paddingTop = "1rem";
    } else {
        document.getElementById("logo").style.width = "100px";
        document.getElementById("navbar").style.paddingTop = "3rem";
    }
}