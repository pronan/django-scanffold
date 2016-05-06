# django-scanffold
A straightforward tool for creating an app folder with CRUD views from a model configuration file.
##为什么要做这个项目
django已经有了admin, 要这个干嘛? 

1. 在实际开发中, 有一层用户的权限仅次于开发者, 但是他们不懂程序, 因此不能直接让其接触admin界面.
2. 需要更多的控制权, views, urls, templates等等.

##要求
1. Python3, django 1.8, jinja2, pypinyin

## 用法
目前主要是为中文设计考虑的. 比如要设计一个学生成绩系统,假设字段为:`姓名, 性别, 班级, 成绩`, 那么在model.py里面这样配置:
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
            'choices':[('男','男'), ('女', '女')],
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
就会得到students文件夹. 这是一个完备的app文件夹, 在settings.py文件添加该app后, 直接就可以访问各种资源了.
##计划
目前的设计是为我个人的项目考虑的, 因此耦合度较高, 很多地方还待完善.即便如此, 你也可以用它搭个框架, 之后再小修小改, 总好过最原始的`python manage.py startapp `吧? 想想那枯燥无味的一遍又一遍的填充views.py, forms.py, models.py和templates的过程吧.
