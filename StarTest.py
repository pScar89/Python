def get_argument_lines():
    lines = []
    more = True

    while more:

        prem = input('\nEnter a premise?\n')

        if prem == 'n':
            more = False
        else:
            lines.append(prem)

    need_conc = input('\nWould you like to test a conclusion?\n')

    if need_conc == 'y':
        conclusion = input('\nWhat is the conclusion?\n')
    else:
        conclusion = 'null is null'

    lines.append(conclusion)

    return lines


def split_lines(lines):
    word_list = []

    for line in lines:
        word_list.append(line.split())

    return word_list

# The next few functions handle the different ways an argument line can be given
# It is kind of difficult to read due to the nature of syntax.
# They underline and add a '*' to the correct terms.
# The 'tracker' is used to determine which line is the conclusion


def d_and_s_not_clause(line, tracker):

    # There is something about this '\u0332' which is used to underline the
    # characters. I had to add a space to the end with the below line, and
    # then apply the .join(). It also wouldn't work when I tried adding the
    # space in a different method

    line[len(line) - 1] = line[len(line) - 1] + ' '
    line[len(line) - 1] = '\u0332'.join(line[len(line) - 1])

    if tracker != 1:
        line[len(line) - 1] = line[len(line) - 1] + '*'
    else:
        if line[0] == 'some':
            line[1] = line[1] + '*'
        else:
            line[0] = line[0] + '*'


def d_and_s_all_line(line, tracker):
    line[1] = line[1] + ' '
    line[1] = '\u0332'.join(line[1])

    if tracker != 1:
        line[1] = line[1] + '*'
    else:
        line[len(line) - 1] = line[len(line) - 1] + '*'


def d_and_s_no_line(line, tracker):
    line[1] = line[1] + ' '
    line[1] = '\u0332'.join(line[1])
    line[len(line) - 1] = line[len(line) - 1] + ' '
    line[len(line) - 1] = '\u0332'.join(line[len(line) - 1])

    if tracker != 1:
        line[1] = line[1] + '*'
        line[len(line) - 1] = line[len(line) - 1] + '*'


def d_and_s_other_line(line, tracker):
    if line[len(line) - 2] == 'not':
        d_and_s_not_clause(line, tracker)
    else:
        if tracker == 1:
            if line[0] == 'some':
                line[1] = line[1] + '*'
            else:
                line[0] = line[0] + '*'

            line[len(line) - 1] = line[len(line) - 1] + '*'


def distribute_and_star(word_lines):
    tracker = len(word_lines)

    for line in word_lines:

        if line[0] == 'all':
            d_and_s_all_line(line, tracker)

        elif line[0] == 'no':
            d_and_s_no_line(line, tracker)

        else:
            d_and_s_other_line(line, tracker)

        tracker -= 1

    return word_lines


def footer(d_lines):
    print('\nFinal:\n')

    for line in d_lines:

        joined_lines = ''

        for word in line:
            joined_lines = joined_lines + ' ' + word

        print(joined_lines)

        # doc.write(joined_lines)

    print('\n')


def header():
    print('\nIn this program you input arguments one line at a time.')
    print('For now, it will output a distributed, starred version of the argument.')
    print('Type "n" for no, and "y" for yes. Do not capitalize words, only letters.\n')
    print('Here is what a sample run looks like:\n')
    print('Enter a premise?\n'
          'all L is M\n'
          '\n'
          'Enter a premise?\n'
          'g is not L\n'
          '\n'
          'Enter a premise?\n'
          'n\n'
          '\n'
          'What is the conclusion?\n'
          'g is not M\n'
          '\n'
          'Final:\n'
          '\n'
          'all L̲ * is M\n'
          'g is not L̲ *\n'
          'g* is not M̲\n'
          '------------\n')


def run():
    lines = split_lines(get_argument_lines())

    return distribute_and_star(lines)


def main():
    ready = True
    #doc = open('output.txt', 'a')

    header()

    while ready:
        footer(run())

        again = input('Another argument?\n')

        if again == 'n':
            ready = False

    # doc.close()


main()
