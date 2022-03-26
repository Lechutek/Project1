users = [{"name": "Kamil", "country":"Poland"}, {"name":"John", "country": "USA"}, {"name":"Yeti"}]
users_pl=[x for x in users if x.get('country') and x['country']=='Poland']
print (users_pl)