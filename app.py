from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/collection-center')
def collection_center():
    return render_template('collection-center.html')

@app.route('/upcoming-events')
def upcoming_events():
    return render_template('upcoming-events.html')

@app.route('/raffle', methods=['GET', 'POST'])
def raffle():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Handle file upload
        donation_photo = request.files.get('donation-photo')
        
        if donation_photo:
            # Save the file to the uploads folder
            filename = donation_photo.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            donation_photo.save(filepath)

        # Redirect to a success page or handle submission success
        return redirect(url_for('raffle_success'))
    
    return render_template('raffle.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/raffle-success')
def raffle_success():
    return 'Raffle entry submitted successfully!'

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        
    app.run(debug=True)
