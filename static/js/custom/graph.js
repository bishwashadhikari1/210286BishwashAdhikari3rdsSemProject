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
                'rgba(73, 230, 18, .1)',
            ],
        },

        ]
    }, options: {
        scales: {
            x: { 
                display: false
            }
        }
    }
};
const groupName = JSON.parse(document.getElementById('group-name').textContent);
console.log(groupName);
var woos = 'ws://' + window.location.host + '/ws/graph/' + groupName + '/';
console.log(woos)
var myChart = new Chart(ctx, graphData);
var socket = new WebSocket(woos);


socket.onmessage = function (e) {

    var newGraphData = graphData.data.datasets[0].data;
    // newGraphData.shift();
    var djangoData = JSON.parse(e.data);
    newGraphData.push(djangoData.pnl);
    var newGraphLabel = graphData.data.labels;
    var tablehtml = '<tr><th scope="col">Side</th><th scope="col">Symbol</th><th scope="col">Entry</th><th scope="col">Mark Price</th><th scope="col">Size</th><th scope="col">PnL</th></tr>'
    var historyhtml = '<tr><th scope="col">Symbol</th><th scope="col">PnL</th></tr>';
    newGraphLabel.push('.');
    graphData.data.labels = newGraphLabel;
    graphData.data.datasets[0].data = newGraphData;
    myChart.update();
    lofposition = djangoData.positions;
    historyy = djangoData.history;
    for (var i = 0; i < lofposition.length; i++) {
        tablehtml += "<tr>";
        var temphtml = '<th scope = "row">' + lofposition[i][0] + '</th>';
        tablehtml += temphtml;
        var sym = lofposition[i][1]
        var symnousd = sym.slice(0, (sym.length-4));
        iconurl = '<img src="https://www.cryptofonts.com/img/icons/'+ symnousd.toLowerCase() + '.svg" width="20px" height="20px">'
        var temphtml = '<th>' + lofposition[i][1]  + iconurl + '</th>';
        tablehtml += temphtml;
        let ep = +lofposition[i][2];

        var temphtml = '<th>' + ep.toFixed(2) + '</th>';
        tablehtml += temphtml;
        let mp = +lofposition[i][3];
        var temphtml = '<th>' + mp.toFixed(2) + '</th>';
        tablehtml += temphtml;
        var temphtml = '<th>' + lofposition[i][4] + '</th>';
        tablehtml += temphtml;
        if (lofposition[i][5] > 0) {
            var signal = 'green';
        } else {
            var signal = 'red';
        }
        let pnl = +(lofposition[i][5]);

        var temphtml = '<th style="color:' + signal + '">' + pnl.toFixed(2) + '</th>';
        tablehtml += temphtml;
        tablehtml += '</tr>';
    }
    for(var i = 0 ; i < historyy.length/2; i++){
        var sym = historyy[i*2]
        var symnousd = sym.slice(0, (sym.length-4));
        iconurl = '<img src="https://www.cryptofonts.com/img/icons/'+ symnousd.toLowerCase() + '.svg" width="20px" height="20px">'
        historyhtml += "<tr>";
        var temphtml = "<th scope = row>" + historyy[i*2] + iconurl + "</th>";

        historyhtml += temphtml;
        if (historyy[i*2+1] > 0) {
            var signal = 'green';
        } else {
            var signal = 'red';
        }
        let hpnl = +(historyy[i*2+1]);
        var temphtml ='<th style="color:' + signal + '">'  + hpnl.toFixed(2) + "</th>";
        historyhtml += temphtml;
        historyhtml += "</tr>";

    }
    document.getElementById('postable').innerHTML = tablehtml;
    document.getElementById('historytable').innerHTML = historyhtml;

    console.log(djangoData);
}


console.log('5');