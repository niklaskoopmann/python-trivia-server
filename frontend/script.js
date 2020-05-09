function populateDropdowns() {
  var categories;
  $.get("http://192.168.179.69:42069/about/categories", function(data, status) {
    categories = data
  });
}