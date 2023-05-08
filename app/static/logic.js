// Created a const for each graph to their respective API route:
const treemapURL = '/api/treemap/';
const Q3URL = '/api/q3/';
const Q4URL = '/api/q4/';
const Q5URL = '/api/q5/';
const Q30URL = '/api/q30/';

// Read the JSON of one of the questions with D3 to get the voter categories and once read, appended each category to the dropdown menu
// of the dashboard:
d3.json(Q3URL).then(({categories}) => {
  
  categories.forEach(id => {
    d3.select('select').append('option').text(id)
  });
  
  optionChanged();

});

// Used the function expression 'optionChanged' to limit where the function is available and keep the global scope light whenever the
// voter category is changed:
const optionChanged = () => {
  // Took the first voter category:
  let selectedCategory = d3.select('select').node().value;

  // Changed HTML text to reflect the currently selected voter category:
  d3.select("#treemapCategory").text(selectedCategory);

  // Created a function to load and update the treemap with the data from the demographic questions:
  const treemapOptionChanged = () => {
    d3.json(treemapURL).then(({treemapData}) => {

      // Filtered the voter categories within the demographic questions' JSON and compared it to the selected one from the dropdown menu to
      // see what voter category data to call:
      let treemapsData = treemapData.filter(obj => obj.voter_category == selectedCategory)[0];

      // Defined the treemap data:
      let {labels, parents, values} = treemapsData;

      // Turned the JSON objects into arrays:
      var arrLabels = Object.values(labels);
      var arrParents = Object.values(parents);
      var arrValues = Object.values(values);

      // Created a variable for the trace of the treemap:
      var traceTreemap = [{
        type: 'treemap',
        values: arrValues,
        labels: arrLabels,
        parents: arrParents,
        branchvalues: 'total',
        hoverlabel: {
          font: {
            size: 28
          }
        },
        textposition: 'middle center',
        textfont: {
          size: 20
        }
      }];

      // Created a variable for the layout of the treemap:
      var layoutTreemap = {
        colorway: ['#F6BDC0', '#F1959B', '#F07470', '#EA4C46']
      };

      // Graphed the treemap with the trace data and the layout:
      Plotly.newPlot('treemap', traceTreemap, layoutTreemap);
    })
  };

  // Created a function to load and update the doughnut chart with the data from question 5:
  const Q5OptionChanged = () => {
    d3.json(Q5URL).then(({q5}) => {

       // Changed HTML text to reflect the currently selected voter category:
      d3.select("#q5DoughnutCategory").text(selectedCategory);

      // Filtered the voter categories within the question 5 JSON and compared it to the selected one from the dropdown menu to see what
      // voter category data to call:
      let q5Data = q5.filter(obj => obj.voter_category == selectedCategory)[0];

      // Defined the data of question 5:
      let {q5_options, values} = q5Data;

      // Turned the JSON objects into arrays:
      var arrQ5Options = Object.values(q5_options);
      var arrQ5Values = Object.values(values);

      // Created a loop to fill the data needed (with the specific format requested) for the Google Chart:
      var forQ5DoughnutData = [['Response', '% of respondents']];
      for (let i = 0; i < arrQ5Options.length; i++) {
        forQ5DoughnutData.push([`${arrQ5Options[i]}`, arrQ5Values[i]]);
      };

      // Loaded the Google Chart with the correct package and called the function 'drawChart':
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      
      // Created the function 'drawChart':
      function drawChart() {
        // Defined the data for the chart:
        var q5DoughnutData = google.visualization.arrayToDataTable(forQ5DoughnutData);

        // Defined the layout (i.e. the size of the doughnut hole and the colours).
        var Q5Options = {
          pieHole: 0.4,
          slices: {
            0: {color: d3.interpolateGnBu(0.7)},
            1: {color: '#EA4C46'}
          },
        };

        // Selected the HTML id where the chart should go:
        var chart = new google.visualization.PieChart(document.getElementById('q5Doughnut'));
        
        // Drew the chart with the coded data and the coded layout:
        chart.draw(q5DoughnutData, Q5Options);
      };
    })
  };

  // Created a function to load and update the doughnut chart with the data from question 30:
  const Q30OptionChanged = () => {
    d3.json(Q30URL).then(({q30}) => {

      // Changed HTML text to reflect the currently selected voter category:
      d3.select("#q30DoughnutCategory").text(selectedCategory);

      // Filtered the voter categories within the question 30 JSON and compared it to the selected one from the dropdown menu to see what
      // voter category data to call:
      let q30Data = q30.filter(obj => obj.voter_category == selectedCategory)[0];

      // Defined the data of question 30:
      let {q30_options, values} = q30Data;

      // Turned the JSON objects into arrays:
      var arrQ30Options = Object.values(q30_options);
      var arrQ30Values = Object.values(values);

      // Created a loop to fill the data needed (with the specific format requested) for the Google Chart:
      var forQ30DoughnutData = [['Response', '% of respondents']];
      for (let i = 0; i < arrQ30Options.length; i++) {
        forQ30DoughnutData.push([`${arrQ30Options[i]}`, arrQ30Values[i]]);
      }

      // Loaded the Google Chart with the correct package and called the function 'drawChart':
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);

      // Created the function 'drawChart':
      function drawChart() {
        // Defined the data for the chart:
        var q30DoughnutData = google.visualization.arrayToDataTable(forQ30DoughnutData);

        // Defined the layout (i.e. the size of the doughnut hole and the colours).
        var Q30Options = {
          pieHole: 0.4,
          slices: {
            0: {color: '#EA4C46'},
            1: {color: d3.interpolateGnBu(0.8)},
            2: {color: d3.interpolateGnBu(0.5)},
            3: {color: '#F1959B'},
            4: {color: 'purple'}
          }
        };

        // Selected the HTML id where the chart should go:
        var chart = new google.visualization.PieChart(document.getElementById('q30Doughnut'));
        
        // Drew the chart with the coded data and the coded layout:
        chart.draw(q30DoughnutData, Q30Options);
      };
    })
  };

  // Created a function to load and update the first heatmap with the data from question 3:
  const Q3OptionChanged = () => {
    d3.json(Q3URL).then(({q3}) => {

      // Changed HTML text to reflect the currently selected voter category:
      d3.select("#q3HeatmapCategory").text(selectedCategory);

      // Filtered the voter categories with the JSON of question 3 and compared it to the selected one from the dropdown menu to see what 
      // voter category data to call:
      let q3Data = q3.filter(obj => obj.voter_category == selectedCategory)[0];
    
      // Defined the heatmap data:
      let {q3_group, value, variable} = q3Data;

      // Created consts to label the 'x' and 'y' axes:
      const xLabels = ['Strongly agree', 'Somewhat agree', 'Somewhat disagree', 'Strongly disagree'];
      const yLabels = ['F', 'E', 'D', 'C', 'B', 'A'];

      // Arranged the Z values based on the documentation of the heatmap:
      let zValues = [[value[0], value[1], value[2], value[3]],
                      [value[4], value[5], value[6], value[7]],
                      [value[8], value[9], value[10], value[11]],
                      [value[12], value[13], value[14], value[15]],
                      [value[16], value[17], value[18], value[19]],
                      [value[20], value[21], value[22], value[23]]
                    ];
  
      // Created a variable to define the end colours of the scale of the heatmap:
      var myColour = [
        [0, d3.interpolateGnBu(0.3)],
        [1, d3.interpolateGnBu(0.7)]
      ];

      // Created a variable for the trace of the heatmap:
      var Q3TraceHeatmap = [
        {
          z: zValues,
          x: xLabels,
          y: yLabels,
          type: 'heatmap',
          colorscale: myColour,
          hoverongaps: false        }
      ];
  
      // Created a variable for the layout of the treemap:
      var Q3Layout = {
        annotations: [],
        xaxis: {
          autotick: false,
          tick0: 'Strongly agree',
          ticks: '',
          title: 'Agree or Disagree',
        },
        yaxis: {
          ticks: '',
          ticksuffix: ' ',
          width: 700,
          height: 700,
          autosize: false,
          title: 'Statements'
        }
      };

      // Looped to get the percentages of each heatmap cell to show:
      for ( var i = 0; i < yLabels.length; i++ ) {
        for ( var j = 0; j < xLabels.length; j++ ) {
          var currentValue = zValues[i][j];
          var textColor = 'black';
          var result = {
            xref: 'x1',
            yref: 'y1',
            x: xLabels[j],
            y: yLabels[i],
            text: zValues[i][j]+'%',
            font: {
              family: 'Arial',
              size: 12,
              color: 'rgb(50, 171, 96)'
            },
            showarrow: false,
            font: {
              color: textColor
            }
          };
          Q3Layout.annotations.push(result);
        }
      }
      
      // Graphed the treemap with the trace data and the layout:
      Plotly.newPlot('q3Heatmap', Q3TraceHeatmap, Q3Layout);
    })
  };

  // Created a function to load and update the second heatmap with the data from question 4:
  const Q4OptionChanged = () => {
    d3.json(Q4URL).then(({q4}) => {

      // Changed HTML text to reflect the currently selected voter category:
      d3.select("#q4HeatmapCategory").text(selectedCategory);

      // Filtered the voter categories with the JSON of question 4 and compared it to the selected one from the dropdown menu to see what
      // voter category data to call:
      let q4Data = q4.filter(obj => obj.voter_category == selectedCategory)[0];

      // Defined the heatmap data:
      let {q4_group, value, variable} = q4Data;

      // Created consts to label the 'x' and 'y' axes:
      const xLabels = ['A significant impact', 'Somewhat of an impact', 'Just a slight impact', 'No impact at all'];
      const yLabels = ['F', 'E', 'D', 'C', 'B', 'A'];

      // Arranged the Z values based on the documentation of the heatmap:
      let zValues = [[value[0], value[1], value[2], value[3]],
                      [value[4], value[5], value[6], value[7]],
                      [value[8], value[9], value[10], value[11]],
                      [value[12], value[13], value[14], value[15]],
                      [value[16], value[17], value[18], value[19]],
                      [value[20], value[21], value[22], value[23]]
                    ];

      // Created a variable to define the end colours of the scale of the heatmap:
      var myColour = [
        [0, d3.interpolateGnBu(0.3)],
        [1, d3.interpolateGnBu(0.7)]
      ];

      // Created a variable for the trace of the heatmap:
      var Q4TraceHeatmap = [
        {
          z: zValues,
          x: xLabels,
          y: yLabels,
          type: 'heatmap',
          colorscale: myColour,
          hoverongaps: false,
        }
      ];
      
      // Created a variable for the layout of the treemap:
      var Q4Layout = {
        annotations: [],
        xaxis: {
          autotick: false,
          tick0: 'Strongly agree',
          ticks: '',
          title: 'Impact',
        },
        yaxis: {
          ticks: '',
          ticksuffix: ' ',
          width: 700,
          height: 700,
          autosize: false,
          title: 'Bodies'
        }
      };

      // Looped to get the percentages of each heatmap cell to show:
      for ( var i = 0; i < yLabels.length; i++ ) {
        for ( var j = 0; j < xLabels.length; j++ ) {
          var currentValue = zValues[i][j];
          var textColor = 'black';
          var result = {
            xref: 'x1',
            yref: 'y1',
            x: xLabels[j],
            y: yLabels[i],
            text: zValues[i][j]+'%',
            font: {
              family: 'Arial',
              size: 12,
              color: 'rgb(50, 171, 96)'
            },
            showarrow: false,
            font: {
              color: textColor
            }
          };
          Q4Layout.annotations.push(result);
        }
      }
      
      // Graphed the treemap with the trace data and the layout:
      Plotly.newPlot('q4Heatmap', Q4TraceHeatmap, Q4Layout);
    
    })
  };

  // Called all the chart functions created to graph the selected questions:
  treemapOptionChanged();
  Q5OptionChanged();
  Q30OptionChanged();
  Q3OptionChanged();
  Q4OptionChanged();
  Q5OptionChanged();
};