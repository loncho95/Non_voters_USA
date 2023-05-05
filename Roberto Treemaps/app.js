// // Set the dimensions of the treemap
// var width = 960;
// var height = 500;

// // Create a color scale for the treemap
// var color = d3.scaleOrdinal(d3.schemeCategory10);

// // Create a treemap layout
// var treemap = d3.treemap()
//     .size([width, height])
//     .padding(1)
//     .round(true);

// // Load the CSV file
// d3.csv("../database/nonvoters_data_clean.csv").then(function(data) {

//   // Nest the data by the specified columns
//   var nestedData = d3.nest()
//     .key(function(d) { return d.educ; })
//     .key(function(d) { return d.race; })
//     .key(function(d) { return d.gender; })
//     .key(function(d) { return d.income_cat; })
//     .rollup(function(v) { return v.length; })
//     .entries(data);

//   // Convert the nested data to a hierarchical structure
//   var root = d3.hierarchy({ values: nestedData }, function(d) { return d.values; })
//     .sum(function(d) { return d.value; });

//   // Compute the treemap layout
//   treemap(root);

//   // Append the treemap to the HTML div
//   var svg = d3.select("#treemap")
//     .append("svg")
//     .attr("width", width)
//     .attr("height", height)
//     .append("g")
//     .attr("transform", "translate(0,0)");

//   // Create a cell for each data element in the treemap
//   var cell = svg.selectAll("g")
//     .data(root.leaves())
//     .enter().append("g")
//     .attr("transform", function(d) { return "translate(" + d.x0 + "," + d.y0 + ")"; });

//   // Create a rectangle for each cell
//   cell.append("rect")
//     .attr("width", function(d) { return d.x1 - d.x0; })
//     .attr("height", function(d) { return d.y1 - d.y0; })
//     .attr("fill", function(d) { return color(d.parent.data.key); });

//   // Add text labels for each cell
//   cell.append("text")
//     .attr("x", function(d) { return (d.x1 - d.x0) / 2; })
//     .attr("y", function(d) { return (d.y1 - d.y0) / 2; })
//     .attr("text-anchor", "middle")
//     .text(function(d) { return d.parent.data.key + ": " + d.data.value; })
//   }).catch(function(error) {
//     console.log(error);
//   });

// Load the CSV file
d3.csv("../database/nonvoters_data_clean.csv").then(function(data) {

  // Data transformation
  var nested_data = d3.nest()
    .key(function(d) { return d.educ; })
    .key(function(d) { return d.race; })
    .key(function(d) { return d.gender; })
    .key(function(d) { return d.income_cat; })
    .rollup(function(v) { return v.length; })
    .entries(data);

  // Create treemap layout
  var treemap = d3.treemap()
    .size([800, 600])
    .paddingInner(5)
    .paddingOuter(10);

  // Apply layout to data
  var root = d3.hierarchy({values: nested_data}, function(d) { return d.values; })
    .sum(function(d) { return d.value; });

  treemap(root);

  // Create SVG element
  var svg = d3.select("#treemap")
    .append("svg")
    .attr("width", 800)
    .attr("height", 600);

  // Draw rectangles
  svg.selectAll("rect")
    .data(root.leaves())
    .enter()
    .append("rect")
    .attr("x", function(d) { return d.x0; })
    .attr("y", function(d) { return d.y0; })
    .attr("width", function(d) { return d.x1 - d.x0; })
    .attr("height", function(d) { return d.y1 - d.y0; })
    .attr("fill", "steelblue");

  // Add text labels
  svg.selectAll("text")
    .data(root.leaves())
    .enter()
    .append("text")
    .attr("x", function(d) { return d.x0 + 5; })
    .attr("y", function(d) { return d.y0 + 15; })
    .text(function(d) { return d.data.key; });

});
