from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load therapist data from Excel
def load_therapists():
    df = pd.read_excel('therapists.xlsx')
    return df

# Match therapists based on patient needs (simple rule-based)
def match_therapists(patient_need):
    df = load_therapists()
    matched_therapists = df[df['Expertise'].str.contains(patient_need, case=False)]
    return matched_therapists

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    patient_name = request.form.get('patient_name')
    patient_need = request.form.get('patient_need')

    # Match therapists based on expertise
    matched_therapists = match_therapists(patient_need)

    return render_template('match.html', therapists=matched_therapists, patient_name=patient_name)

@app.route('/assign', methods=['POST'])
def assign():
    patient_name = request.form.get('patient_name')
    therapist_name = request.form.get('therapist_name')
    
    # In a real app, you'd save the assignment to a database or file here
    # For now, we will just print to console and simulate the assignment
    print(f'Assigned {therapist_name} to {patient_name}')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
