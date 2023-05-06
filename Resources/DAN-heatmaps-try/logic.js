// // D3 V4
// // To set the dimensions and margins of the graph:
// var margin = {top:80, right:25, bottom:30, left:40},
//     width = 450 - margin.left - margin.right,
//     height = 450 - margin.top - margin.bottom;


// // To append the SVG object to the body of the page:
// var svg = d3.select('#heatmap')
//     .append("svg")
//         .attr('width', width + margin.left + margin.right)
//         .attr('height', height + margin.top + margin.bottom)
//     .append('g')
//         .attr('transform',
//             'translate(' + margin.left + ',' + margin.top + ')');

// // To read the data:
// d3.csv('../nonvoters_data_clean_2TQ3.csv', function(data) {

//     // The labels of row and columns, which are the unique identifier of the columns 'group' and 'variable':
//     var myGroups = d3.map(data, function(d){return d.RespId;}).keys()
//     // console.log(myGroups);
//     var myVars = d3.map(data, function(d){return d.variable_q3;}).keys()
//     // console.log(myVars);

//     // To build x scales and axis:
//     var x = d3.scaleBand()
//             .range([ 0, width ])
//             .domain(myGroups)
//             .padding(0.05);
//     svg.append('g')
//         .style('font-size', 15)
//         .attr('transform', 'translate(0,' + height + ')')
//         .call(d3.axisBottom(x).tickSize(0))
//         .select('.domain').remove()

//     // To build Y scales and axis:
//     var y = d3.scaleBand()
//             .range([ height, 0 ])
//             .domain(myVars)
//             .padding(0.05);
//     svg.append('g')
//         .style('font-size', 15)
//         .call(d3.axisLeft(y).tickSize(0))
//         .select('.domain').remove()

//     // To build the color scale:
//     var myColour = d3.scaleSequential()
//         .interpolator(d3.interpolateInferno)
//         .domain([1,4])

//     // To create a tooltip
//     var tooltip = d3.select('#heatmap')
//         .append('div')
//         .style('opacity', 0)
//         .attr('class', 'tooltip')
//         .style('background-color', 'white')
//         .style('border', 'solid')
//         .style('border-width', '2px')
//         .style('border-radius', '5px')
//         .style('padding', '5px')

//     // Three functions that change the tooltip when the user hovers/moves/leaves a cell
//     var mouseover = function(d) {
//         tooltip
//             .style('opacity', 1)
//         d3.select(this)
//             .style('stroke', 'black')
//             .style('opacity', 1)
//     }

//     var mousemove = function(d) {
//         tooltip
//         .html('The exact value of<br>this cell is: ' + d.value_q3)
//         .style('left', (d3.mouse(this)[0]+70) + 'px')
//         .style('top', (d3.mouse(this)[1]) + 'px')
//     }

//     var mouseleave = function(d) {
//         tooltip
//             .style('opacity', 0)
//         d3.select(this)
//             .style('stroke', 'none')
//             .style('opacity', 0.8)
//     }

//     // To add the squares:
//     svg.selectAll()
//         .data(data, function(d) {return d.RespId+':'+d.variable_q3;})
//         .enter()
//         .append('rect')
//             .attr('x', function(d) { return x(d.RespId) })
//             .attr('y', function(d) { return y(d.variable_q3) })
//             .attr('rx', 4)
//             .attr('ry', 4)
//             .attr('width', x.bandwidth() )
//             .attr('height', y.bandwidth() )
//             .attr('fill', function(d) { return myColour(d.value_q3)} )
//             .style('stroke-width', 4)
//             .style('stroke', 'none')
//             .style('opacity', 0.8)
//         .on('mouseover', mouseover)
//         .on('mousemove', mousemove)
//         .on('mouseleave', mouseleave)
// });





// D3 V6
// set the dimensions and margins of the graph
const margin = {top: 80, right: 25, bottom: 30, left: 40},
  width = 450 - margin.left - margin.right,
  height = 450 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#heatmap")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

//Read the data
d3.csv('../q3_coded_nonvoters_data_clean.csv').then(function(data) {

  // Labels of row and columns -> unique identifier of the column called 'group' and 'variable'
  const myGroups = Array.from(new Set(data.map(d => d.Q3_group)))
  const myVars = Array.from(new Set(data.map(d => d.variable)))

  // Build X scales and axis:
  const x = d3.scaleBand()
    .range([ 0, width ])
    .domain(myVars)
    .padding(0.05);
  svg.append("g")
    .style("font-size", 15)
    .attr("transform", `translate(0, ${height})`)
    .call(d3.axisBottom(x).tickSize(0))
    .select(".domain").remove()

  // Build Y scales and axis:
  const y = d3.scaleBand()
    .range([ height, 0 ])
    .domain(myGroups)
    .padding(0.05);
  svg.append("g")
    .style("font-size", 15)
    .call(d3.axisLeft(y).tickSize(0))
    .select(".domain").remove()

  // Build color scale
  const myColour = d3.scaleSequential()
    .interpolator(d3.interpolateGnBu)
    .domain([1,50])

  // create a tooltip
  const tooltip = d3.select("#heatmap")
    .append("div")
    .style("opacity", 0)
    .attr("class", "tooltip")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "2px")
    .style("border-radius", "5px")
    .style("padding", "5px")

  // Three function that change the tooltip when user hover / move / leave a cell
  const mouseover = function(event,d) {
    tooltip
      .style("opacity", 1)
    d3.select(this)
      .style("stroke", "black")
      .style("opacity", 1)
  }
  const mousemove = function(event,d) {
    tooltip
      .html("The exact value of<br>this cell is: " + d.value)
      .style("left", (event.x)/2 + "px")
      .style("top", (event.y)/2 + "px")
  }
  const mouseleave = function(event,d) {
    tooltip
      .style("opacity", 0)
    d3.select(this)
      .style("stroke", "none")
      .style("opacity", 0.8)
  }

  // add the squares
  svg.selectAll()
    .data(data, function(d) {return d.Q3_group+':'+d.variable;})
    .join("rect")
      .attr("x", function(d) { return x(d.variable) })
      .attr("y", function(d) { return y(d.Q3_group) })
      .attr("rx", 4)
      .attr("ry", 4)
      .attr("width", x.bandwidth() )
      .attr("height", y.bandwidth() )
      .style("fill", function(d) { return myColour(d.value)} )
      .style("stroke-width", 4)
      .style("stroke", "none")
      .style("opacity", 0.8)
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
})

// Add title to graph
svg.append("text")
        .attr("x", 0)
        .attr("y", -50)
        .attr("text-anchor", "center")
        .style("font-size", "22px")
        .text("How much do you agree or disagree with the following statements?")

// // Add subtitle to graph
// svg.append("text")
//         .attr("x", 0)
//         .attr("y", -20)
//         .attr("text-anchor", "left")
//         .style("font-size", "14px")
//         .style("fill", "grey")
//         .style("max-width", 400)
//         .text("A short description of the take-away message of this chart.");
