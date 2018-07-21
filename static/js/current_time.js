function timeNow() {
  var d = new Date(),
  h = (d.getHours()<10?'0':'') + d.getHours(),
  m = (d.getMinutes()<10?'0':'') + d.getMinutes();
  document.getElementById("output").innerHTML = h + ':' + m;
}