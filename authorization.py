import pytest
import os
import sys

TEST_RESULT_PATH = os.getenv('TEST_RESULT_PATH')

print(f'{TEST_RESULT_PATH}')

if __name__ == '__main__':
    path = f'{TEST_RESULT_PATH}/log.txt'
    sys.stdout = open(path, 'a')
    pytest.main(args=[
        '-rA',
        '-v',
        f'--report-log={TEST_RESULT_PATH}/authorization.jsonl',
        f'--html={TEST_RESULT_PATH}/authorization.html',
        '--self-contained-html'
    ])
    #close log file
    sys.stdout.close()