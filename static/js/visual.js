

function noVote() {

	var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var parseTime = d3.timeParse("%d-%b-%y");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[1]); });



    d3.tsv(url, function (d) {

        return d;
    }, function (error, data) {

    	function glow(i){
var gl = [];
    	var keys = d3.keys(data[0]);
	data.forEach(function(d) {
		if (i>0){gl.push(parseFloat(d[keys[i]]))}
		else {gl.push( parseTime(d[keys[i]])   )
		;}

    });
return gl;
    	}

		var cf = [];
    	var result = [];
		for (i = 0; i < 2; i++) {
    		cf.push(glow(i));
}


for ( var i = 0; i < cf[0].length; i++ ) {
  result.push( [ cf[0][i], cf[1][i] ] );

}
console.log(cf);
        if (error) throw error;

        x.domain(d3.extent(cf[0], function (d) {
            return d;
        }));
        y.domain(d3.extent(cf[1], function (d) {
            return d;
        }));
data = result;

        g.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))
            .select(".domain")
			.attr("x", 1)
			.attr("dx", "0.1em")
			.attr("text-anchor", "end");


        g.append("g")
            .call(d3.axisLeft(y))
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", "0.71em")
            .attr("text-anchor", "end")
            .text("Price ($)");



        g.append("path")
            .datum(data)
            .attr("fill", "none")
            .attr("stroke", "steelblue")
            .attr("stroke-linejoin", "round")
            .attr("stroke-linecap", "round")
            .attr("stroke-width", 1.5)
            .attr("d", line);
    });


}
