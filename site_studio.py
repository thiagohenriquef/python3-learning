def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class')
    joining = ''.join(args)
    attrs = ' '.join(f'{key}="{value}"' for key, value in kwargs.items())
    return f'<{tag} {attrs}> {joining} </{tag}>'


if __name__ == '__main__':
    result = tag(
        'p',
        tag('span', 'Learning Python 3 with Cod3r Courses'),
        tag('strong', 'Thiago', id='Th'),
        tag('span', ' and '),
        tag('strong', 'Always foolish always hungry', id='ll'),
        tag('span', '.'),
        html_class='alert'
    )

    print(result)
