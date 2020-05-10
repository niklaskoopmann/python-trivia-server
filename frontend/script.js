function populateDropdowns() {
  var categories;
  $.get("http://192.168.179.69:42069/about/categories", function(data, status) {
    console.log(data);
    data["categories"].forEach((item, i) => {
      $(".categories").append("<option value=" + item["internal"] + ">" + item["display"] + "</option>");
    });
  });
}

function drawChart(){
  var ctxP = document.getElementById("chart-area").getContext('2d');
  var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
      labels: ["Brown", "Blue", "Orange", "Yellow", "Pink", "Green"],
      datasets: [{
        data: [1, 1, 1, 1, 1, 1],
        backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360", "#000000"],
        //onClick: [function(){console.log("a")}, function(){console.log("b")}, function(){console.log("c")}, function(){console.log("d")}, function(){console.log("e")}, function(){console.log("f")}]
        //hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774", "#000000"]
      }]
    },
    options: {
      responsive: true,
      tooltips: {
        mode: ''
      },
      legend: {
        position: 'bottom',
        onClick: null
      }
    }
  });
}
