   // Load the CSV file
   d3.csv("../data_cleaning/nonvoters_data_clean.csv").then(function(data) {
      
   // Parse the income categories
    const incomeCategories = {
     1: "less than $40K",
     2: "$40-$75K",
     3: "$75-$125K",
     4: "$125K or more"
   };
    
  // Parse the education levels
   const educationLevels = {
     1: "College",
     2: "High school or less",
     3: "Some college"
   };

  // Parse the race categories
    const raceCategories = {
     1: "Black",
     2: "Hispanic",
     3: "Others",
     4: "White"
   };

  // Define the trace
   const trace = {
     type: "treemap",
     ids: data.map(d => [incomeCategories[d.income_cat], educationLevels[d.educ], raceCategories[d.race], d.gender === "1" ? "Female" : "Male"]),
     labels: data.map(d => d.RespId),
     parents: data.map(d => [educationLevels[d.educ], incomeCategories[d.income_cat], raceCategories[d.race], d.gender === "1" ? "Female" : "Male"]),
     values: data.map(d => 1),
     hovertemplate: "<b>%{id}</b><br>Count: %{value}<extra></extra>",
     textposition: "middle center",
     textfont: { color: "white" },
     marker: { colors: ["#003f5c", "#58508d", "#bc5090", "#ff6361", "#ffa600"] }
   };

  // Define the layout
   const layout = {
     title: "Treemap Plot with Plotly",
     font: { color: "black" },
     treemapcolorway: ["#003f5c", "#58508d", "#bc5090", "#ff6361", "#ffa600"],
     automargin: true,
     margin: { t: 60, l: 10, r: 10, b: 10 },
     hovermode: "closest"
   };

  // Create the plot
    Plotly.newPlot("treemap", [trace], layout);
  }).catch(function(error) {
    console.log(error);
  });



