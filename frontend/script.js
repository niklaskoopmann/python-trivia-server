function populateDropdowns () {
  var categories;
  $.get("http://192.168.179.69:42069/about/categories", function(data, status) {
    console.log(data);
    data["categories"].forEach((item, i) => {
      $(".categories").append("<option value=" + item["internal"] + ">" + item["display"] + "</option>");
    });
  });
}
