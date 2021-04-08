import click
import sys

from eth2deposit.cli.existing_mnemonic import existing_mnemonic
from eth2deposit.cli.new_mnemonic import new_mnemonic
from eth2deposit.utils.click import (
    captive_prompt_callback,
    choice_prompt_func,
)
from eth2deposit.utils import config
from eth2deposit.utils.constants import INTL_LANG_OPTIONS
from eth2deposit.utils.intl import (
    get_first_options,
    fuzzy_reverse_dict_lookup,
    load_text,
)


def check_python_version() -> None:
    '''
    Checks that the python version running is sufficient and exits if not.
    '''
    if sys.version_info < (3, 7):
        click.pause(load_text(['err_python_version']))
        sys.exit()


@click.group()
@click.pass_context
@click.option(
    '--language',
    callback=captive_prompt_callback(
        lambda language: fuzzy_reverse_dict_lookup(language, INTL_LANG_OPTIONS),
        choice_prompt_func(lambda: 'Please choose your language', get_first_options(INTL_LANG_OPTIONS))(),
    ),
    default='English',
    prompt=choice_prompt_func(lambda: 'Please choose your language', get_first_options(INTL_LANG_OPTIONS))(),
    required=True,
    type=str,
)
def cli(ctx: click.Context, language: str) -> None:
    config.language = language


cli.add_command(existing_mnemonic)
cli.add_command(new_mnemonic)


if __name__ == '__main__':
    check_python_version()
    cli()
