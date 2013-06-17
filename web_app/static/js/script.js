$(function(event){

	// Bit.ly Link of the Moment

	$.get("https://api-ssl.bitly.com/v3/highvalue?access_token=7b17a350da22325411fa948240023c020d35fdaa&limit=1", function(response) {
		var query = "default";
		query = response["data"]["values"][0];
		console.log(query);
		$("h2").html("<a href='" + query + "' target='_blank'>" + query + "</a>");
		console.log("Success");
	}).fail(function() {
		console.log("Failure");
	}).always(function() {
		console.log("Complete");
	});

	// D3 Graph Creation

				    var width = 960,
			    height = 2200;

				var cluster = d3.layout.cluster()
				    .size([height, width - 160]);

				var diagonal = d3.svg.diagonal()
				    .projection(function(d) { return [d.y, d.x]; });

				var svg = d3.select("body").append("svg")
				    .attr("width", width)
				    .attr("height", height)
				  .append("g")
				    .attr("transform", "translate(40,0)");

				d3.json("/flare", function(error, root) {
				  var nodes = cluster.nodes(root),
				      links = cluster.links(nodes);

				  var link = svg.selectAll(".link")
				      .data(links)
				    .enter().append("path")
				      .attr("class", "link")
				      .attr("d", diagonal);

				  var node = svg.selectAll(".node")
				      .data(nodes)
				    .enter().append("g")
				      .attr("class", "node")
				      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })

				  node.append("circle")
				      .attr("r", 4.5);

				  node.append("text")
				      .attr("dx", function(d) { return d.children ? -8 : 8; })
				      .attr("dy", 3)
				      .style("text-anchor", function(d) { return d.children ? "end" : "start"; })
				      .text(function(d) { return d.name; });
				});

				d3.select(self.frameElement).style("height", height + "px");

	// Submissions

	$('#submit-button').click(function(event) {

		console.log("Now sending: " + $('#topic').val());

		dispatch($('#topic').val());
	});

	$('.link').click(function(event){
	//	
		event.preventDefault();
		console.log("Now sending: " + $(this).html());

		dispatch($(this).html());
	});

//	http://metricle.com:9000/

	function dispatch(data) {

		$.ajax({
  			type: 'post',
    		url: '/jack?start=' + data,
    		success: function(x) {
    			console.log(data);
    		}
		});

	}

});