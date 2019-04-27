#import MySQLdb
import pyodbc
import urllib
import requests
import json
class DbRequests():


    def __init__(self):
            # Call the parent class constructor
            super().__init__()

    def Create_DB(self, cursor):
        
        query = "SELECT * FROM OCPIZZA.dbo.Aliment"
        cursor.execute(query)
        return query

    def Insert_stores(self,cursor):
        data = self.Request_stores()
        print(data)
        sql = '''INSERT INTO ocpizza.dbo.store (IdStore, Name)
                 VALUES(%s, %s)'''
        
        cursor.execute(sql,data)

#--Request api openfoodfacts stores
    def Request_stores(self):
        url_stores = "https://fr.openfoodfacts.org/stores.json"
        json_data = requests.get(url_stores).json()
        stores = []
        for each in json_data['tags']:
                #print(each['name'])
                name_store = each['name'] # collect item name
                stores.append(name_store) # Add to dictionary
                
                #print(stores)
        return(stores)

#--Request api openfoodfacts categories
    def Request_categories(self):    
        url_category = 'https://fr.openfoodfacts.org/categories.json'
        json_data = requests.get(url_category).json()
    
        for each in json_data['tags']:
                category = {}
                #print(each['name'])
                name_category = each['name'] # collect item name
                id_category = each['id'] # collect item id
                category.update({id_category:name_category}) # Add to dictionary

        return(category)

#--Request api openfoodfacts ingredients
    def Request_ingredients(self):  
        url_ingredients = "https://fr.openfoodfacts.org/ingredients.json"
        json_data = requests.get(url_ingredients).json()
    
        for each in json_data['tags']:
                ingredients = {}
                #print(each['name'])
                name_ingredients = each['name'] # collect item name
                id_ingredients = each['id'] # collect item id
                ingredients.update({id_ingredients:name_ingredients}) # Add to dictionary

        return(ingredients)

