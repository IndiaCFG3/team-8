function plotGraph1(){
        var x = document.getElementById("input");
		var Info = x.elements[0].value
        var country = x.elements[1].value
        var requestURL = "http://localhost:5000/"+Info+"/bycountry/"+country
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
        new Chartist.Line('.ct-chart1', data);
		/*if(x.elements[2].value!="") var k=plotGraph2();
        return xmlHttp.responseText;*/

}
function plotGraph2(){
        var x = document.getElementById("input");
		var Info = x.elements[0].value
        var country = x.elements[2].value
        var requestURL = "http://localhost:5000/"+Info+"/bycountry/"+country
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
        new Chartist.Line('.ct-chart2', data);
        return xmlHttp.responseText;

}

document.getElementById("done").addEventListener("click", plotGraph1);
document.getElementById("done").addEventListener("click", plotGraph2);