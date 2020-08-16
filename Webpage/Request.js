function plotGraph(){
        var x = document.getElementById("input");
		var Info = x.elements[0].value
        var country = x.elements[1].value
        var requestURL = Info+"/bycountry/"+country
        console.log(requestURL)
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", requestURL, false); // false for synchronous request
        xmlHttp.send( null );
        var obj = JSON.parse(xmlHttp.responseText)
        var data = {
            labels: obj.years,
            series: [
                obj.values
            ]
        };
        new Chartist.Line('.ct-chart', data);
        return xmlHttp.responseText;

}
document.getElementById("done").addEventListener("click", plotGraph);