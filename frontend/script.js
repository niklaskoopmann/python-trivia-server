

function populateDropdowns () {
  var categories;
  $.get("http://192.168.179.69:42069/about/categories", function(data, status) {
    categories = data
  });

  $.(".categories").each(function(i, object) {
    categories.forEach((item, j) => {
      object.appendChild("<option value="" ")
    });
  });
}
