var ctx = document.getElementById("lineChart").getContext('2d');

var graphData = {
    type: 'line',
    data: {
        labels: pnldata.label,
        datasets: [{
            label: "PnL",
            data: pnldata.pnl,
            backgroundColor: [
                'rgba(105, 0, 132, .2)',
            ],
            borderColor: [
                'rgba(200, 99, 132, .7)',
            ],
            borderWidth: 2
        },
        
    ]
},
options: {
    responsive: true
}
};
var myLineChart = new Chart(ctx, graphData);