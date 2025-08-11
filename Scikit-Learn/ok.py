from fpdf import FPDF

# Create PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'Heart Disease Prediction Report', ln=True, align='C')

# Introduction
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '1. Introduction', ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, "This report provides an analysis of heart disease prediction using Logistic Regression and Random Forest models.")

# Data Preprocessing
pdf.ln(5)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '2. Data Preprocessing', ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, "The dataset was preprocessed by imputing missing values and scaling the numerical features.")

# Model Results
pdf.ln(10)
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, '3. Model Results', ln=True)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, f"Logistic Regression Accuracy: {accuracy_score(y_test, y_pred_log)}\n"
                      f"Random Forest Accuracy: {accuracy_score(y_test, y_pred_rf)}")

# Save PDF
pdf_output_path = "heart_disease_prediction_report.pdf"
pdf.output(pdf_output_path)
print(f"PDF report saved as {pdf_output_path}")
