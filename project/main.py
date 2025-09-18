from functions_utils import is_number_bigger_than_given, add_salt_too_list
from service.logger import logger


def main():
    result = is_number_bigger_than_given(candidate_number=5)
    logger.info(f"is_number_bigger_than_given was called ", extra={
        "candidate_number": 5,
        "result": result
    })

    result = is_number_bigger_than_given(candidate_number=5)
    logger.debug(f"is_number_bigger_than_given was called ", extra={
        "candidate_number": 5,
        "result": result
    })

    result = is_number_bigger_than_given(candidate_number=5)
    logger.error(f"is_number_bigger_than_given was called ", extra={
        "candidate_number": 5,
        "result": result
    })

    result = is_number_bigger_than_given(candidate_number=5, threshold=10)

    given_list = []
    add_salt_too_list(given_list)
    add_salt_too_list(given_list)
    add_salt_too_list(given_list)
    add_salt_too_list(given_list)



if __name__ == "__main__":
    main()
