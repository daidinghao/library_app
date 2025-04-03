{
    "name": "Library",                                                              
    'version': '1.0',
    "summary": "Manage books and library members.",                                 
    'description': 'A simple module to manage books',                               
    "author": "Dai",                                                             
    "depends": ["base"],                                                            
    'category': 'Library',                                                                              
    "application": True,                                                            
    "data": [
        "security/ir.model.access.csv", 
        "views/library_book_views.xml",
        "views/library_loan_views.xml",
        "views/library_member_views.xml",
        "views/library_publisher_views.xml",
        "views/partner_views.xml",
        'views/library_loan_report.xml'
        ],                                       
    "installable": True,                                                            
    "auto_install": False,                                                          
}


