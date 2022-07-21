var ctx = document.getElementById("myChart").getContext('2d');
var graph
var graphData = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "PnL",
            data: [1,2,3,4,6,7],
            backgroundColor: [
                'rgba(73, 230, 18, .2)',
            ],
        },
        
    ]
},
options: {
    responsive: true
}
};






// var myChart = new Chart(ctx, graphData);
// var timeframe = document.querySelector('#app').innerText ;
// var timeframe = 1;
// var socket = new WebSocket('ws://localhost:8000/ws/graph/');






// socket.onmessage = function(e){
//     var newGraphData = graphData.data.datasets[0].data;
//     // newGraphData.shift();
//     var djangoData = JSON.parse(e.data);
//     newGraphData.push(djangoData.value);
//     var newGraphLabel = graphData.data.labels;
    
//     newGraphLabel.push(djangoData.label);
//     graphData.data.labels = newGraphLabel;
//     graphData.data.datasets[0].data = newGraphData;
//     myChart.update();
//     console.log(djangoData);
//     document.querySelector('#app').innerText = djangoData.value;


// }


console.log('5');