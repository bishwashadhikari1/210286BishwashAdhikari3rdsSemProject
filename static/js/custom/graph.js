var ctx = document.getElementById("lineChart").getContext('2d');
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: "PnL",
      data: 
      [],
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
});