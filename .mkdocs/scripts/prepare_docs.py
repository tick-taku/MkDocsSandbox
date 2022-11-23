import yaml
import shutil
import os

print('INFO - mkdir docs')
os.makedirs('docs/', exist_ok=True)

with open('.mkdocs/conf.yml') as file:
  conf = yaml.safe_load(file)

  print('INFO - Moving config file: mkdocs.yml')
  shutil.copy('.mkdocs/mkdocs.yml', './')

  if 'top' in conf:
    top_md = conf['top']
    print(f'INFO - Moving top md file: {top_md}')
    shutil.copy(top_md, f'docs/{os.path.basename(top_md)}')

  if 'logo' in conf:
    logo = conf['logo']
    print(f'INFO - Moving logo image file: {logo}')
    shutil.copy(logo, f'docs/{os.path.basename(logo)}')

  if 'favicon' in conf:
    favicon = conf['favicon']
    print(f'INFO - Moving favicon image file: {favicon}')
    shutil.copy(favicon, f'docs/{os.path.basename(favicon)}')

  for doc in conf['docs']:
    print(f'INFO - Moving document: {doc}')
    shutil.copytree(doc, f'docs/{doc}', dirs_exist_ok=True)
