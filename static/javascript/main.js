var ss = 1000000000000;
var sped = 1;
setInterval(function(){
    ss = ss + sped / 250;
    document.getElementById("time-label").textContent = ss;
}, 1);

