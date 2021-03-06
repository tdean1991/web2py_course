# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from contacts.py")

def data():
    rows = db(db.contact).select()
    return locals()

def filter():
    #get count
    rows1_count = db(db.contact.state_name=='CA').count()
    # get all records, sorted by name
    #rows2_all_sorted_by_name = db(db.contact).select(orderby=~db.contact.last_name | db.contact.first_name)
    # filter, show only those whose last_name starts with M
    #rows3_startswith = db(db.contact.last_name.startswith('M')).select(orderby=db.contact.first_name | db.contact.last_name)
    rows4_by_state = db(~(db.contact.state_name=='CA')).select(orderby=db.contact.last_name 
        | db.contact.first_name)
    rows5_combo = db(~(db.contact.state_name=='CA') &
        (db.contact.last_name.startswith('A'))).select(orderby=db.contact.last_name)
    return locals()

def add():
    form = SQLFORM(db.contact).process()
    return locals()

def view():
    if request.args(0) is None:
        rows = db(db.contact).select(orderby=db.contact.last_name | db.contact.first_name)
    else:
        letter = request.args(0)
        rows = db(db.contact.last_name.startswith(letter)).select(
            orderby=db.contact.last_name | db.contact.first_name)
    return locals()

def update():
    record = db.contact(request.args(0)) or redirect(URL('view'))
    form = SQLFORM(db.contact, record)
    if form.process().accepted:
        response.flash = T('Record Updated')
    else:
        response.flash = T('Please complete the form.')
    return locals()
