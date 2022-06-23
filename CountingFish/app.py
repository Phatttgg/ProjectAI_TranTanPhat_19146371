from flask import Flask,render_template,url_for,request,redirect
from detecto import core, utils, visualize
import os
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'png', 'jfif', 'mov', 'jpg', 'jpeg', 'gif'}
app=Flask(__name__)


@app.route('/')
def game1():
  return render_template('home.html') 

  
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file'] 
        basepath=os.path.dirname(__file__)
        file_path=os.path.join(basepath,secure_filename(f.filename))
        
       
      
        f.save(file_path)
        model = core.Model.load('fish_model.pth', ['fish'])
        image = utils.read_image(file_path)
        predictions = model.predict(image)
        
        labels, boxes, scores = predictions
        
        scores=scores
        
        alt_score=[]
        for i in scores:
            alt_score.append(float(i))
        
        fish=[0]
        count=0
        j=0
        for i in labels:
            if i=="fish":
                fish.append(alt_score[j])
                if alt_score[j]> 0.8:
                  count=count+1
            j=j+1
        final=[]    
        fish_score=max(fish)
        
        fish_score=round(fish_score*100,2)
        if (fish_score>75):
            final.append("fish")
     
        
        return render_template("home.html",fish_score=fish_score,final=final,len=len(final),count=count)
        final=[]



if __name__=='__main__':
     app.run(debug=True)