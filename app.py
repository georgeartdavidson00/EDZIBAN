from flask import Flask , render_template,url_for,request,redirect
from flask.scaffold import F
from recipes import *
import ast



app = Flask(__name__)

@app.route('/ingredient',methods=['GET','POST'])
def run_ingredients():
    if request.method == "POST":
        data = request.json
        MainData = check_for_recipes(data)
        #print(MainData)
        #newdata=str(MainData)
        # res = newdata.strip('][').split(', ')
        print(MainData)
        print("worked")
        return redirect(f'/showrecipe/{MainData}')
    return render_template('add_ingredients.html')
    
@app.route('/')
def main_run():
    return render_template('Project.html')

@app.route('/showrecipe/<data>')
def show_recipe(data):
    data=ast.literal_eval(data)

    print(data)
    #MainData = data.strip('[]').split(',')
    #print(MainData)
    return render_template('recipe.html', data=data)

    
if __name__ == '__main__':
    app.run(debug=True)