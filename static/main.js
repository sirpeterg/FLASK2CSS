let root = document.documentElement;
let color = document.getElementById("body").getAttribute("data-value");
root.style.setProperty('--color', color);
