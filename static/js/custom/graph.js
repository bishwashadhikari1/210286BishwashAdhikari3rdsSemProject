var ctx = document.getElementById("myChart").getContext('2d');
var graph
var graphData = {
    type: 'line',
    data: {
        labels: ['jan','feb', 'mar', 'apr', 'may', 'june'],
        datasets: [{
            label: "PnL",
            data: [1,2,3,4,6,7],
            backgroundColor: [
                'rgba(73, 230, 198, .2)',
            ],
            borderWidth: 1
        },
        
    ]
},
options: {
    responsive: true
}
};
var myChart = new Chart(ctx, graphData);
var timeframe = document.querySelector('#app').innerText ;
var wws = new WebSocket('wss://stream.binance.com:9443/ws/BTCUSDT@kline_'+timeframe+'m')
var socket = new WebSocket('ws://localhost:8000/ws/graph/');
wws.onmessage(

)

wws.onmessage = function(e){
    
}
socket.onmessage = function(e){
    var newGraphData = graphData.data.datasets[0].data;
    newGraphData.shift();
    var djangoData = JSON.parse(e.data);
    newGraphData.push(djangoData.value);
    graphData.data.datasets[0].data = newGraphData;
    myChart.update();
    console.log(djangoData);
    document.querySelector('#app').innerText = djangoData.value;
    

}


console.log('5');