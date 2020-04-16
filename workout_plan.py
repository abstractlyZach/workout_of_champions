import random


MIN_MULTIPLIER = 1
MAX_MULTIPLIER = 3


def main():
    exercises = get_exercises()
    for exercise in exercises:
        do_exercise(exercise)
        input('Press <enter> to continue')
    print('*' * 60)
    print('nice.')


def get_exercises():
    exercises = list()
    with open('exercises.csv', 'r') as infile:
        for line in infile.readlines():
            exercise, min_reps, max_reps = line.split(',')
            exercises.append((exercise, int(min_reps), int(max_reps)))
    return exercises


def do_exercise(exercise_data):
    exercise_name, min_reps, max_reps = exercise_data
    num_reps, coinflip, multiplier = do_rng(min_reps, max_reps)
    print_exercise(exercise_name, num_reps, coinflip, multiplier)


def do_rng(min_reps, max_reps):
    num_reps = random.randrange(min_reps, max_reps + 1)
    coinflip = random.choice(['heads', 'tails'])
    multiplier = random.randrange(MIN_MULTIPLIER, MAX_MULTIPLIER + 1)
    return (num_reps, coinflip, multiplier)


def print_exercise(exercise_name, num_reps, coinflip, multiplier):
    print('=' * 20)
    print(exercise_name)
    print(f'base reps: {num_reps}')
    print(f'coin flip: {coinflip}')
    print(f'multiplier: {multiplier}x')
    print(f'total reps: {num_reps * multiplier}')
    

if __name__ == '__main__':
    main()
