import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact',response_class=HTMLResponse)
def get_list():
    #return{'name':'Platzi'}
    return """
    <h1> Hola FastAPI</h1>
    <p> parrafo ..... </p>
    """


def run():
    store.get_categories()

if __name__=='__main__':
    run()