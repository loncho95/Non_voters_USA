d3.csv('../data_cleaning/nonvoters_data_clean.csv').then(function(rows) {

  // Roll up the data by income_cat and count the number of occurrences
  var incomeCounts = d3.rollup(rows, 
    v => v.length,  // count the number of occurrences
    d => d.income_cat  // group by income_cat
  );

  console.log(incomeCounts);

  function unpack(rows, keys) {
    return rows.map(function(row) { 
      return keys.map(function(key) {
        return row[key]
      })
    });
  }

  function getIncomeLevel(income_cat) {
    var count = incomeCounts.get(income_cat);
    if (income_cat == 1) {
      return { level: 'Less than $40K', count: count };
    } else if (income_cat == 2) {
      return { level: '$40- $75K', count: count };
    } else if (income_cat == 3) {
      return { level: '$75 - $125K', count: count };
    } else {
      return { level: '$125K or more', count: count };
    }
  }
  
  var data = [{
    type: "treemap",
    ids: unpack(rows, ['educ', 'race', 'gender', 'income_cat']),
    labels: ['Education Level', 'Race', 'Gender', 'Income Category'],
    parents: ['', '', '', ''],
    level: getIncomeLevel(rows.income_cat)
  }];
  
  Plotly.newPlot('treemap', data);
});


