// google.charts.load('current', {
//     'packages': ['geomap'],
//     // Note: you will need to get a mapsApiKey for your project.
//     // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
//     // 'mapsApiKey': 'AIzaSyCuOdzw2EabitjjEqoAzAwuXUfUvmDqruc'
// });
// google.charts.setOnLoadCallback(drawMap);
//
// function drawMap() {
//     console.log("START DRAW")
//     var x = document.getElementById("input");
//     var requestURL = "http://localhost:5000/population/all"
//     console.log(requestURL)
//     var xmlHttp = new XMLHttpRequest();
//     xmlHttp.open("GET", requestURL, false); // false for synchronous request
//     xmlHttp.send(null);
//     var obj = JSON.parse(xmlHttp.responseText)
//     var dat= []
//     dat.push(["Country", "Popularity"])
//     for (let property in obj) {
//         dat.push([property, obj[property]])
//     }
//     var data = google.visualization.arrayToDataTable(dat);
//     var options = {};
//     options['dataMode'] = 'regions';
//     var container = document.getElementById('regions_div');
//     console.log(container)
//     console.log(dat)
//     var geomap = new google.visualization.GeoMap(container);
//     geomap.draw(data, options);
// }

google.charts.load('current', {
    'packages': ['geochart'],
    // Note: you will need to get a mapsApiKey for your project.
    // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
    var requestURL = "http://localhost:5000/production/all"
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