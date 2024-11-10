from flask import Flask, render_template, request, session, redirect
import os
import chatgpt, image_analyzer
import random
import string
from zipfile import ZipFile


def generate_random_string(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

app = Flask(__name__)
app.secret_key = "SECURITY 1000"

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allow only specific file extensions
ALLOWED_EXTENSIONS = {'zip'}

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/timeline")
def timeline():
    if not 'data' in session:
        return redirect("/")

    data = session["data"]
    for i in range(len(data)):
        if data[i]['img']:
            data[i]['img'] = os.path.join(app.config['UPLOAD_FOLDER'], session['cookie'], data[i]['img'])


    print(data)

    return render_template("/timeline.html", data=data)


@app.route('/logout')
def logout():
    print(f"logout()")

    folder_path = os.path.join(UPLOAD_FOLDER, session['cookie'])
    print(f"cookies = {session['cookie']}; folder_path = {folder_path}")
    for i in os.listdir(folder_path):
        os.remove(os.path.join(folder_path, i))
    os.rmdir(folder_path)
    print(f"os.rmdir({folder_path})")
    session.clear()
    return redirect('/')

@app.route('/upload', methods=['POST'])
def upload():
    session['cookie'] = generate_random_string(40)
    file = request.files['file']
    filename = 'chat.zip'
    path1 = os.path.join(app.config['UPLOAD_FOLDER'], session['cookie'])
    os.makedirs(path1)
    path = os.path.join(path1, filename)
    file.save(path)
    with ZipFile(path, 'r') as zObject: 
       zObject.extractall(path=path1) 
       print('extracted')
    return render_template('/selection.html')

@app.route('/upload-timeline')
def upload_file():
    if not 'cookie' in session:
        return redirect('/')

    path = os.path.join(UPLOAD_FOLDER, session['cookie'])
    res = chatgpt.extractData_timeline(path=path).split("\n")

    content = []

    for line in res:
        start = line.find("[") + 1
        end = line.find("]")
        date = line[start:end].split(',')[0]
        start = line.find('"') + 1
        end = line.rfind('"')
        title = line[start:end]
        img = None
        for i in line.split():
            if '.jpg' in i:
                img = i
                break
        
        color = 'white'

        if img:
            color = image_analyzer.extractData_image(UPLOAD_FOLDER+'/'+session['cookie']+'/'+img)

            for mood in image_analyzer.colours.keys():
                if mood in color.lower():
                    color = image_analyzer.colours[mood]
                    break

        print(color)
        
        content.append({
            'date': date,
            'title': title,
            'img': img,
            'color': color
        })

    print(content)
    session["data"] = content
    #TODO: Remove
    print(f"\n\n\n\nFinish upload")

    return redirect('/timeline')

@app.route('/quiz')
def quiz():
    return render_template('/quiz.html')#, data=session['data'])

@app.route('/upload-quiz')
def upload_quiz():
    if not 'cookie' in session:
        return redirect('/')
    path = os.path.join(UPLOAD_FOLDER, session['cookie'])

    res = chatgpt.get_questions(path=path)

    print(res)

    return redirect('/quiz')


if __name__ == "__main__":
    app.run(debug=True)

