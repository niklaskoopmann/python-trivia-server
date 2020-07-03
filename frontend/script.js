function populateDropdowns() {
  var categories;
  $.get("http://192.168.179.69:42069/about/categories", function(data, status) {
    console.log(data);
    data["categories"].forEach((item, i) => {
      $(".categories").append("<option value=" + item["internal"] + ">" + item["display"] + "</option>");
    });
  });
}

function drawChart() {
  var ctxP = document.getElementById("chart-area").getContext('2d');
  var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
      labels: ["Brown", "Blue", "Orange", "Yellow", "Pink", "Green"],
      datasets: [{
        data: [1, 1, 1, 1, 1, 1],
        backgroundColor: ["#896752", "#45a8db", "#df733f", "#ffd147", "#df77ba", "#30846a"],
        //onClick: [function(){console.log("a")}, function(){console.log("b")}, function(){console.log("c")}, function(){console.log("d")}, function(){console.log("e")}, function(){console.log("f")}]
        hoverBackgroundColor: ["#5e3c2a", "#2f5fa7", "#b14d28", "#daa233", "#ae4b7c", "#21695f"]
      }]
    },
    options: {
      responsive: true,
      tooltips: {
        mode: ''
      },
      legend: {
        position: 'bottom',
        onClick: null,
        boxWidth: 10,
        fontSize: 40
      }
    }
  });
}