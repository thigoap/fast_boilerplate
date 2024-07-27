from http import HTTPStatus

from fastapi import HTTPException


def sanitize(string: str) -> str:
    alpha = ''.join(
        char for char in string if char.isalnum() or char.isspace()
    )
    # print(" ".join(alpha.split()).lower())
    sanitized = ' '.join(alpha.split()).lower()
    print('sanitized', sanitized)
    if not sanitized:
        # print('')
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Empty string',
        )
    return ' '.join(alpha.split()).lower()
