function populateDropdowns() {
  var categories;
  $.get("http://192.168.179.69:42069/about/categories", function(data, status) {
    console.log(data);
    data["categories"].forEach((item, i) => {
      $(".categories").append("<option value=" + item["internal"] + ">" + item["display"] + "</option>");
    });
  });
}

var ctxP = document.getElementById("pieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
  type: 'pie',
  data: {
    labels: ["Red", "Green", "Yellow", "Grey", "Dark Grey"],
    datasets: [{
      data: [300, 50, 100, 40, 120],
      backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C", "#949FB1", "#4D5360"],
      hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774"]
    }]
  },
  options: {
    responsive: true
  }
});