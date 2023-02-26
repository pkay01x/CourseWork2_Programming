function scanPorts() {
    var ip_address = document.getElementById("ip_address").value;
    var port_range = document.getElementById("port_range").value;
    var loadingMessage = document.getElementById("loading");
    loadingMessage.style.display = "flex";
    eel.scan_ports(ip_address, port_range)(displayResults);
    
}

function displayResults(results) {
    var resultArea = document.getElementById("results");
    var loadingMessage = document.getElementById("loading");
    loadingMessage.style.display = "none";
    var i = 0;
    function displayNextResult() {
        if (i < results.length) {
            resultArea.innerHTML += results[i] + "<br>";
            i++;
            setTimeout(displayNextResult, 100); // Delay before displaying next result
        }
    }
    displayNextResult();
}

document.getElementById("reset").addEventListener("click", function() {
    document.getElementById("ip_address").value = "";
    document.getElementById("port_range").value = "";
    document.getElementById("results").innerHTML = "";
  });