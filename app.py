# import flask into project
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a flask object of the JobApp from the Flask module
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# Creating the database Model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(20), nullable=False)
    jobtitle = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    url = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    # apply = db.Column(db.String(20))
    
    # Function to return a string after a Job has been created
    def __repr__(self):
        return '<Job %r>' % self.id


# Create the default page
# Route to Add entry
@app.route('/', methods=['POST', 'GET'])
# Define a function to load the default page
def index():
    if request.method == 'POST':
        # company
        comp = request.form['company']
        # job title
        job_title = request.form['jobTitle']
        # location
        loc = request.form['location']
        # url
        url = request.form['jobUrl']
        # posted
        posted = request.form['datePosted']
        
        
        new_job = Job(company=comp, jobtitle=job_title, location=loc, url=url, date_posted=posted)
          
        try:
            db.session.add(new_job)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your job to the database'
        
    else:
        jobs = Job.query.order_by(Job.date_added).all()
        return render_template('index.html', jobs=jobs)



# Route to Delete entry
@app.route('/delete/<int:id>')
def delete(id):
    # store job to delete in variable
    job_to_delete = Job.query.get_or_404(id)
    
    try:
        db.session.delete(job_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return 'There was a problem deleting this job'
    
    
# Route to Add entry
@app.route('/update/<int:id>', methods=['GET', 'POST'])
# Define a function to load the default page
def update(id):
    
    if request.method == 'POST':
        
        job = Job.query.get(request.form.get(id))
        
        # company
        job.company = request.form['company']
        # job title
        job.jobTitle = request.form['jobTitle']
        # location
        job.location = request.form['location']
        # url
        job.jobUrl = request.form['jobUrl']
        # posted
        job.datePosted = request.form['datePosted']
        
          
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue editing your job'
        
    else:
        return render_template('/')
        
    
    

if __name__ == "__main__":
    app.run(debug=True)