// while (true) {
//   var tds = $("#example").find("td");
//   for (let index = 0; index < tds.length; index++) {
//     var element = tds[index];
//     console.log(element.innerText);
//   }
//   $("#example_next").click();
// }

for (var i = 0; i < 473; i++) {
  var tds = $("#example").find("td");
  for (let index = 0; index < tds.length; index++) {
    var element = tds[index];
    console.log(element.innerText);
  }
  $("#example_next").click();
}
