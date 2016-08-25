from django.shortcuts import render_to_response

def index(resquest):
    return render_to_response('login.html',{})