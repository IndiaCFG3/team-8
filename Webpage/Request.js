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
function draw_on_map(){
    google.charts.load('current', {
    'packages': ['geochart'],
    // Note: you will need to get a mapsApiKey for your project.
    // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
    var x = document.getElementById("input");
    var stub = x.elements[3].value
    var requestURL = 'http://localhost:5000/'+stub+'/all'
    console.log(requestURL)
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", requestURL, false); // false for synchronous request
    xmlHttp.send(null);
    var obj = JSON.parse(xmlHttp.responseText)
    var dat = []
    dat.push(["Country", "Popularity"])
    for (let property in obj) {
        dat.push([property, obj[property]])
    }
    var data = google.visualization.arrayToDataTable(dat);

    var options = {};

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
}
}
document.getElementById("done").addEventListener("click", plotGraph1);
document.getElementById("done").addEventListener("click", plotGraph2);
document.getElementById("done").addEventListener("click", draw_on_map)