//Code was used on Google Sheets using extension AppScript


function findMatch() {
  // Get the spreadsheet
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // Get the range of column A
  var rangeA = sheet.getRange("A1:A" + sheet.getLastRow()).getValues();

  // Get the range of column B
  var rangeB = sheet.getRange("B1:B" + sheet.getLastRow()).getValues();

  // Initiate column D counter
  var d = 0;

  // Iterate through column A 
  for (var a = 0; a < rangeA.length; a++) { 
    var valueA = rangeA[a][0]; 
    d++; 
    var matchCount = 0; // Reset matchCount with each new row in column A 

    // Iterate through column B 
    for (var b = 0; b < rangeB.length; b++) { 
      var valueB = rangeB[b][0]; 
      // Check if the number in column A matches any of the numbers in column B 
      if (valueA === valueB) { 
        matchCount++; // Increment matchCount for each match found 
      }
    }

    // Add the results to column D
    var columnD = sheet.getRange("D" + d); // Get the correct row number based on column A current row
    var score = valueA * matchCount; // Multiply the number in column A by the # of matching instances from column B
    columnD.setValue(score); // Set the result to column D 
  }
}