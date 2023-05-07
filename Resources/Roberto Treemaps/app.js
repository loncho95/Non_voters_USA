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
    
    var values = [225, 150, 150, 100, 75, 50, 40, 35, 60, 40, 50, 40, 30, 20, 60, 70, 30]; 
    var labels = ["VOTER", "Income", "< $40K", "$40-$75K", "$75-$125K", "> $125K", "Education Level", "College", "High school or less", "Some college", "Race", "Black", "Hispanic", "Others", "White", "Gender", "Female", "Male"]; // all labels
    var parents = ["", "VOTER", "Income", "Income", "Income", "Income", "VOTER", "Education Level", "Education Level", "Education Level", "VOTER", "Race", "Race", "Race", "Race", "VOTER", "Gender", "Gender"]; // all parents
    
    var data = [{
      type: 'treemap',
      values: values,
      labels: labels,
      parents: parents,
      marker: {colorscale: 'Greens'}
    }];    
  
Plotly.newPlot('treemap', data)

});
