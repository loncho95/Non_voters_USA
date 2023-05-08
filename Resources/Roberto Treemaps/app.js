   // Load the CSV file
   d3.csv("../data_cleaning/nonvoters_data_clean.csv").then(function(data) {

    var incomeValues = [75, 50, 40, 35]; 
    var incomeLabels = ["< $40K", "$40-$75K", "$75-$125K", "> $125K"]; 
    var incomeParents = ["Income", "Income", "Income", "Income"]; 
    
    var educationValues = [60, 40, 50]; 
    var educationLabels = ["College", "High school or less", "Some college"]; 
    var educationParents = ["Education Level", "Education Level", "Education Level"]; 
    
    var raceValues = [40, 30, 20, 60]; 
    var raceLabels = ["Black", "Hispanic", "Others", "White"]; 
    var raceParents = ["Race", "Race", "Race", "Race"]; 
    
    var genderValues = [70, 30]; 
    var genderLabels = ["Female", "Male"]; 
    var genderParents = ["Gender", "Gender"]; 
    
    var values = [100, 0, 25, 60, 55, 10, 0, 50, 60, 40, 0, 40, 30, 20, 60, 0, 85, 65]; 
    var labels = ["VOTER", "Income", "< $40K", "$40-$75K", "$75-$125K", "> $125K", "Education Level", "College", "High school or less", "Some college", "Race", "Black", "Hispanic", "Others", "White", "Gender", "Female", "Male"]; // all labels
    var parents = ["", "VOTER", "Income", "Income", "Income", "Income", "VOTER", "Education Level", "Education Level", "Education Level", "VOTER", "Race", "Race", "Race", "Race", "VOTER", "Gender", "Gender"]; // all parents
    
    var data = [{
      type: 'treemap',
      values: values,
      labels: labels,
      parents: parents,
      marker: {
        color: ['red', '#ffcccc', '#ff9999', '#ff6666', '#ff4d4d', '#ff1a1a', '#e60000', '#ff1a1a', '#b30000'],
        colorscale: [[0, 'red'], [0.25, '#ffcccc'], [0.4, '#ff9999'], [0.5, '#ff6666'], [0.6, '#ff4d4d'], [0.75, '#ff1a1a'], [0.8, '#e60000'], [0.9, '#ff1a1a'], [1, '#b30000']],
      }
    }];    

    var layout = {
      width: 600,
      height: 500,
      margin: {
        l: 20,
        r: 20,
        b: 20,
        t: 20,
        pad: 4
      },
      // Center the chart horizontally and vertically
      style: {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)'
      }
    };

Plotly.newPlot('treemap', data)
});
