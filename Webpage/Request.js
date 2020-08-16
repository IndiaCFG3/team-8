function plotGraph1() {
    var x = document.getElementById("input");
    var Info = x.elements[0].value
    var urlstub = "supply"
    if(Info == "Supply"){urlstub = "supply"}
    if(Info == "Demand"){urlstub = "perperson"}
    if(Info == "Production Cost"){urlstub = "price"}
    var country = x.elements[1].value
    var requestURL = "http://localhost:5000/" + urlstub +"/bycountry/" + country
    console.log(requestURL)
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", requestURL, false); // false for synchronous request
    xmlHttp.send(null);
    var obj = JSON.parse(xmlHttp.responseText)
    var i = 0
    var yrs = []
    var vals = []
    while (i < obj.years.length) {
        yrs.push(obj.years[i])
        vals.push(obj.values[i])
        i = i + 5
    }
    var data = {
        labels: yrs,
        series: [
            vals
        ]
    };
    new Chartist.Line('.ct-chart1', data);
    if(x.elements[2].value!="") var k=plotGraph2();
    return xmlHttp.responseText;

}

function plotGraph2() {
    console.log("START REQUEST SECOND")
    var x = document.getElementById("input");
    var Info = x.elements[0].value
    console.log(Info)
    var urlstub = "supply"
    if(Info == "Supply"){urlstub = "supply"}
    if(Info == "Demand"){urlstub = "perperson"}
    if(Info == "Production Cost"){urlstub = "price"}
    var country = x.elements[2].value
    console.log(urlstub)
    var requestURL = "http://localhost:5000/" + urlstub +"/bycountry/" + country
    console.log(requestURL)
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", requestURL, false); // false for synchronous request
    xmlHttp.send(null);
    var obj = JSON.parse(xmlHttp.responseText)
    var i = 0
    var yrs = []
    var vals = []
    while (i < obj.years.length) {
        yrs.push(obj.years[i])
        vals.push(obj.values[i])
        i = i + 5
    }
    var data = {
        labels: yrs,
        series: [
            vals
        ]
    };
    new Chartist.Line('.ct-chart2', data);
    return xmlHttp.responseText;
}

document.getElementById("done").addEventListener("click", plotGraph1);
document.getElementById("done").addEventListener("click", plotGraph2);