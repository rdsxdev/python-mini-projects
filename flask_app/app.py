from flask import Flask
app = Flask(__name__) #Flask constructor

#Using a decorator to tell the application about URL association with functions
@app.route('/hello/<name>') #Defines home route
def hello_name(name): #Creating a function that is bound to home route when route page is accessed
    return 'Hello %s!'% name

if __name__=='__main__':
    app.run(debug=True) #Runs app in debug mode (makes sure the app is not needed to restart manually)
                                                #if any changes whatsoever

