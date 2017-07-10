/**
 * Created by c on 11.05.17.
 */

var datasets = d3.range(3).map(function(d) { return {"y": d3.randomUniform(1)() } });
console.log(dataset);

        var svg = d3.select('.col-xs-11').append('svg');
    svg.attr('width', 500)
        .attr('height', 500)
        .append('circle')
        .attr("cy", 20)
        .attr("cx", 20)
        .attr("r", 20)
        .attr("fill", "red")

        var gh = d3.selectAll('p');
    gh.attr('width', 20)
        .attr('height', 20)
        .data(datasets)
        .text(datasets[0]);






    var data = d3.csv('messdaten', function(d) {
          d.forEach(function(d) {

    d.date = +d.date;
    d.close = +d.close;


  }

  );









          var svg = d3.select('.main').html('');

d3.csv(url, function(d) {
  return {
    Name: d.Name, Surname: d.Surname, Age: d.Age
 };
}, function(error, rows) {
		d3.select(".col-xs-11")
			.selectAll("circle")
			.data(rows)
			.enter()
			.append("circle");
	console.log(rows[0]);




xaxis_extent = d3.extent(2, function (d) {
	return d['Name']
});
xaxis_extent = d3.extent(2, function (d) {
	return d['Surname']

});

var x_scale = d3.scaleLinear();
var y_scale = d3.scaleLinear();
var x_axis  = d3.axis()
	.scale(x_scale)
	.ticks();
var y_axis  = d3.axis()
	.scale(y_scale)
	.orientation("left");
var height = 20;
	d3.select("svg")
		.append('g')
		.attr("class", "x axsis")
		.attr("trasform", "translate(0," + height + ")")
		.call(x_scale);
var margin = 20;
	d3.select("svg")
		.append('g')
		.attr("class", "y axsis")
		.attr("trasform", "translate(0," + margin + ")")
		.call(y_scale);
});

d3.csv(url, function(data) {
	console.log(data);

var keys = d3.keys(data[0]);
console.log(keys);

	var gl = [];
	console.log(gl);
data.forEach(function(d) {
		console.log("gl");
        gl.push(d[keys[2]]);
        console.log(gl);

    });
	console.log(gl);

return keys
})

if (i === 0){gl.push(parseTime(d[keys[i]]))} else {gl.push(d[keys[i]]);}
  });