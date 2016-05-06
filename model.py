from collections import OrderedDict
from pypinyin import lazy_pinyin as lp

from_module=object()

class _(str):
    def __repr__(self):
        return self.__str__()

fmd={
    'help_text':'help_texts',
    'choices':'choices',
}


config_dict = {
    'name':'Question', 
    "verbose_name":"问题", 
    'fields':[
        {
            'label':'标题', 
            'max_length':50, 
            'blank':False,
            'help_text':from_module,
        }, 

        {
            'type':'text', 
            'label':'正文', 
            'max_length':5000, 
            'blank':False,
            'help_text':'详细描述你的问题',
        }, 

        {
            'label':'概要', 
            'max_length':50, 
            'blank':False,
            'help_text':from_module,
            'choices':from_module,
        }, 

    ],  
}

class Field(object):
    """docstring for Field"""

    default_dict = {
        'type':'char', 
        'max_length':100, 
        'default':{"char":"", "text":"", "integer":0,} ,
        'blank':True,
        'null':True,  
    }
    name_set=set()
    instance_dict=OrderedDict()

    def __init__(self, fd):
        self.fd = fd.copy()
        self.kwargs={}
        self._setup()

    def __str__(self):
        return '%s=models.%s(%s, %s)'%(
            self.name,
            self.type,
            repr(self.label),
            ', '.join('%s=%s'%(k,repr(v)) for k, v in self.kwargs.items()),
        )

    def try_get(self, arg_name):
        return self.fd.pop(arg_name,None) or self.default_dict.get(arg_name)

    def _setup(self):
        kw=self.kwargs
        f=self.fd
        # label
        label=f.pop('label', None)
        if not label:
            raise Exception('必须指定label的值')
        self.label=label

        # name
        name=f.pop('name', None) or ''.join(e[0] for e in lp(label))
        if name in self.name_set:
            raise Exception('字段名重复:',name)
        self.name_set.add(name)
        self.name=name

        # field_type
        self.raw_type = self.try_get('type')
        self.type = self.raw_type.capitalize()+'Field'
        if self.type in ('CharField', 'TextField'):
            kw['max_length']=self.try_get('max_length')

        # help_text and choices
        for key in ['help_text','choices']:
            val=f.pop(key, None)
            if val is from_module:
                kw[key] = _(fmd[key]+'.'+name) # string that use str as repr
            elif type(val) is str:
                kw[name]=val
            elif val is None:
                pass
            else:
                Exception('%s:%s value type error'%(key, val))

        # rest defaults
        kw['blank']=self.try_get('blank')
        kw['default']=self.try_get('default').get(self.raw_type,"")

        # generic fields
        kw.update(f)

        # from_module the instance to class
        self.instance_dict[name]=self