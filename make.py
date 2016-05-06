import os

from shutil import copytree
from os.path import join
from string import Template



from model import Field, config_dict as model


if __name__=='__main__':
    # Model, model, models
    project_dir = r'' or '.'
    model_name=model['name'].capitalize()
    form_name=model_name
    model_name_lower=model['name'].lower()
    app_name=model_name_lower+'s'
    verbose_name=model['verbose_name']

    # models.py
    for f in model['fields']:
        Field(f)
    INDENT='\n'+chr(32)*4
    dd=Field.instance_dict
    model_fields=INDENT.join(str(ins) for name, ins in dd.items())
    
    # forms.py
    INDENT='\n'+chr(32)*12
    form_fields=repr(list(dd))
    form_labels=INDENT.join('%s:%s,'%(repr(k),repr(v.label)) for k, v in dd.items())
    form_error_messages=INDENT.join('# %s:{"":""},'%repr(k) for k, v in dd.items())
    form_widgets=''
    for name, e in dd.items():
        if 'help_text' in e.kwargs:
            hint=repr(e.kwargs['help_text'])
            if e.type=='TextField':
                form_widgets+=INDENT+"'%(name)s':forms.Textarea(attrs={'placeholder':%(hint)s,'title':%(hint)s,'rows':5}),"%locals()
            else:
                form_widgets+=INDENT+"'%(name)s':forms.TextInput(attrs={'placeholder':%(hint)s,'title':%(hint)s}),"%locals()
    form_widgets=form_widgets.strip()

    # start to generate rendered files
    dst=join(project_dir, app_name)
    copytree('app',dst)
    for rename_dir in ['static','templates']:
        old = join(dst, join(rename_dir, 'app'))
        new = join(dst, join(rename_dir, app_name))
        os.rename(old, new)
    for root, dirs, files in os.walk(dst):
        for name in files:
            p=join(root, name)
            tp=Template(open(p,encoding='u8').read())
            with open(p,'w',encoding='u8') as f:
                f.write(tp.safe_substitute(**locals()))