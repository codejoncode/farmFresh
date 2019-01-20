# Outside of the normal web2py information that goes into the db.py 
#This file features the tables manually created. 

db.define_table('products',
               Field('product_name', requires=IS_NOT_EMPTY()),
               Field('product_price', requires=IS_NOT_EMPTY()),
               Field('product_image', requires=IS_URL()),
               Field('product_status', requires=IS_IN_SET(['active', 'inactive'])),
               Field('farm_name', requires=IS_NOT_EMPTY()),
               Field('farm_address', requires=IS_NOT_EMPTY()),
               Field('farm_website', requires=IS_URL()),
               auth.signature
               )
db.define_table('profile',
                Field('farm_name'),
                Field('farm_address'),
                Field('farm_website'),
                auth.signature
                )
db.define_table('internet_orders',
               Field('productId', type= 'integer'),
               Field('qty', type = 'integer'),
               Field('userId', type = 'integer'),
               Field('status'),
               Field('date_ordered')
               )