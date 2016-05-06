# django-scanffold
A straightforward tool for creating an app folder with CRUD views from a model configuration file.
## 用法
目前主要是为中文设计考虑的. 比如要设计一个学生成绩系统,假设字段为:姓名,性别,班级,成绩, 那么在model.py里面这样配置:
```
config_dict = {
    'name':'Student', 
    "verbose_name":"学生", 
    'fields':[
        {
            'label':'姓名', 
            'max_length':5, 
            'blank':False,
            'help_text':'请填写你的姓名',
        }, 

        {
            'label':'性别', 
            'max_length':1, 
            'blank':False,
            'choices':['男','女'],
        }, 

        {
            'label':'班级', 
            'max_length':10, 
            'blank':False,
            'help_text':from_module, # will be render as 'help_texts.bj',
            'choices':from_module, # will be render as 'choices.bj',
        }, 

        {
            'label':'成绩',
            'type':'integer',
            'blank':False,
            'help_text':_('help_texts.cj'), # will be render as 'help_texts.cj',
        }, 
        
    ],  
}
```
