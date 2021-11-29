function newData() {
var ss = SpreadsheetApp.getActive();
var sourceSheet = ss.getSheetByName('DATA'); // set source
var reportSheet = ss.getSheetByName('REPORT'); // set report sheet

sourceSheet.getRange('Q:Q').copyTo(sourceSheet.getRange('H2'), {contentsOnly:true}); // copies col Q to col H and removes formula
sourceSheet.getRange('R:R').copyTo(sourceSheet.getRange('I2'), {contentsOnly:true}); // copies col R to col I and removes formula
sourceSheet.getRange('O:O').copyTo(sourceSheet.getRange('C1')); // copies col O to col C
var date = Utilities.formatDate(new Date(), "GMT+1", "dd MMM yyyy")
var cDate = sourceSheet.getRange('C1'); // select date cell
var rDate = reportSheet.getRange('Q2'); // select date cell
cDate.setValue(date);
rDate.clearContent();
rDate.setValue(date);

}

function archive() {

var ss = SpreadsheetApp.getActive();
var sourceSheet = ss.getSheetByName('DATA'); // set source
var destSheet = ss.getSheetByName('ARCHIVE'); // set destination

// archives old data, moves new data to old slot and formats it
destSheet.insertColumnBefore(1); // insert column on destination sheet so new data does not overwrite
sourceSheet.getRange('B:B').copyTo(destSheet.getRange('A1')); // copy col b to archive
sourceSheet.getRange('B:B').clearContent(); // clear col b
sourceSheet.getRange('C:C').copyTo(sourceSheet.getRange('B1'), {contentsOnly:true}); // copies col c to col b (AKA last reports data) and removes formula
sourceSheet.getRange('C:C').clearContent(); // clears old col c
sourceSheet.getRange('B1').setNumberFormat('dd MMM yyyy'); // sets moved date to readable number format

newData();

}
