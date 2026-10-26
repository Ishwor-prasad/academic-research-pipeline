/**
 * Automated Google Forms Questionnaire Builder
 * Paste this script into Google Apps Script (script.google.com) to automatically
 * create a structured, validated research survey instrument.
 */

function createResearchSurvey() {
  var form = FormApp.create("Empirical Research Survey Instrument");
  form.setDescription("This questionnaire is part of an academic research investigation. All responses are confidential and used strictly for academic research analysis.");
  form.setConfirmationMessage("Thank you for your valuable participation in this academic research study.");
  form.setIsSpreadsheetLinked(true);

  // Section 1: Demographics & Context
  var itemRole = form.addMultipleChoiceItem();
  itemRole.setTitle("1. Primary Professional / Research Role")
          .setChoiceValues(["Retail Trader / Individual", "Institutional Investor / Fund Manager", "Financial / Research Analyst", "Academic / Other"])
          .setRequired(true);

  var itemExp = form.addMultipleChoiceItem();
  itemExp.setTitle("2. Years of Experience in Domain")
         .setChoiceValues(["0-2 years", "3-5 years", "6-10 years", "More than 10 years"])
         .setRequired(true);

  // Section 2: Core Constructs (Likert Scale)
  var itemScale = form.addScaleItem();
  itemScale.setTitle("3. Perceived Efficacy of Target Method / Model")
           .setBounds(1, 5)
           .setLabels("Extremely Ineffective", "Extremely Effective")
           .setRequired(true);

  Logger.log("Form created successfully: " + form.getEditUrl());
  Logger.log("Public URL: " + form.getPublishedUrl());
}
