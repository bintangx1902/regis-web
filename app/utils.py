def get_template(name: str) -> str:
    """
    :param name: string like the name only of your html file. ex:this
    :return: full html file name with path, ex: app/this.html
    """
    return f'app/{name}.html'


def is_pass_check(cleaned_data) -> bool:
    """
    :param cleaned_data: a django form.cleaned_data
    :return: True or False, true when the average score is over 70
    """
    average_score = (
            (cleaned_data.get('ipa_score', 0) +
             cleaned_data.get('mtk_score', 0) +
             cleaned_data.get('bind_score', 0) +
             cleaned_data.get('bing_score', 0)) / 4
    )
    return average_score >= 70
