var ctx = document.getElementById("myChart").getContext('2d');
var graph
var graphData = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "PnL",
            data: [],
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
const groupName = JSON.parse(document.getElementById('group-name').textContent);
console.log(groupName);
var woos = 'ws://' + window.location.host + '/ws/graph/'+ groupName + '/';
console.log(woos)

var myChart = new Chart(ctx, graphData);
var timeframe = document.querySelector('#app').innerText ;

var socket = new WebSocket(woos);






socket.onmessage = function(e){
    var newGraphData = graphData.data.datasets[0].data;
    // newGraphData.shift();
    var djangoData = JSON.parse(e.data);
    newGraphData.push(djangoData.pnl);
    var newGraphLabel = graphData.data.labels;
    
    newGraphLabel.push(djangoData.time);
    graphData.data.labels = newGraphLabel;
    graphData.data.datasets[0].data = newGraphData;
    myChart.update();
    console.log(djangoData);
    document.querySelector('#app').innerText = djangoData.pnl;


}


console.log('5');