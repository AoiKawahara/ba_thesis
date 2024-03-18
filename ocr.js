const FOLDER_ID = "";
const SPREAD_SHEET_OUTPUT_ID = ""
const SPREAD_SHEET_INPUT_ID = ""
const SHEET_NAME = "シート1"
const folder = DriveApp.getFolderById(FOLDER_ID);

function downloadImage() {
  let inputsheet = SpreadsheetApp.openById(SPREAD_SHEET_INPUT_ID).getSheetByName(SHEET_NAME);
  let lastRow = inputsheet.getLastRow();

  for(let i=0; i<lastRow-1; i++){
    let url = inputsheet.getRange(2+i,1).getValue();
    let blob = UrlFetchApp.fetch(url).getBlob();
    folder.createFile(blob);
  }
}

const outputsheet = SpreadsheetApp.openById(SPREAD_SHEET_OUTPUT_ID).getSheetByName(SHEET_NAME);

function inserttexts(){
  const files = Drive.Children.list(FOLDER_ID).items;
  for (const file of files){
    const image = Drive.Files.copy({title: "tekito"}, file.id, {"ocr":true, "ocrLanguage":"en"});
    const text = DocumentApp.openById(image.id).getBody().getText();
    outputsheet.appendRow([text]);
    Drive.Files.remove(image.id);
  }
}
