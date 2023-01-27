questions = {
    'Question 1': {
        'question': 'how much is 2+2?',
        'answers': {
            'a': '2',
            'b': '4',
            'c': '8',
            'd': '-3'
        },
        'right_answer': 'b'
    },
    'Question 2': {
        'question': 'how much is 4x2?',
        'answers': {
            'a': '2',
            'b': '12',
            'c': '8',
            'd': '20'
        },
        'right_answer': 'c'
    },
}
correct_answers = 0
for qkey, qvalue in questions.items():
    print(f'{qkey}:')
    print(f'{qvalue["question"]}')
    for akey, avalue in qvalue['answers'].items():
        print(f'[{akey}]: {avalue}')

    user_answer = input('type your answer: ')
    if user_answer == qvalue['right_answer']:
        print('correct')
        correct_answers += 1
    else:
        print('wrong')
percentage = correct_answers / len(questions) * 100
print(f'you got {correct_answers} answers right')
print(f'your percentage: {percentage:.0f}%')
