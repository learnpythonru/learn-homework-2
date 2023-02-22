import datetime
import os
import random
import re
import telebot
import config
import ephem


def main():
    bot = telebot.TeleBot(config.BOT_TOKEN)

    def read_cities(user_id):

        def read_file(file_name) -> list:
            cities_list = []
            try:
                with open(file_name, 'r', newline='\r\n', encoding='utf-8') as f:
                    while True:
                        line = f.readline().strip()
                        if not line:
                            break
                        cities_list.append(line)
                    return cities_list
            except (FileNotFoundError, IOError) as e:
                print(e)
                bot.send_message(user_id, 'Something goes wrong, try later '
                                          'or contact support, please')

        user_list = []
        files = ['cities.csv']
        if str(user_id) in os.listdir('./users'):
            files.append(f'./users/{user_id}')
            user_list = read_file(files[1])
        common_cities_list = read_file(files[0])
        return common_cities_list, user_list

    @bot.message_handler(commands=['cities', 'города'])
    def game_of_cities(msg):  # Orchestrator of Cities game
        if bot.get_state(msg.chat.id):  # Check, whether we are playing already
            if available_letter(
                    bot.get_state(msg.chat.id)) == msg.text.lower()[0]:
                response = play_cities(msg.chat.id, msg.text)
            else:  # If user's first letter of a city is wrong
                response = bot.get_state(msg.chat.id)  # keep state with current city
        else:  # The beginning of a game
            response = play_cities(msg.chat.id, city='')
        if response == '1':
            stop_game_of_cities(msg)
            user_message = 'Congratulations! You won the game!'
        elif response == bot.get_state(msg.chat.id):
            named_cities(msg)
            user_message = 'Wrong city. The last was: ' + response
        else:
            bot.set_state(msg.chat.id, response)  # Setting user state, based on a name of a city
            next_letter = available_letter(response)  # Choosing available letter for the next turn
            user_message = response + f' your move is on {next_letter}'
        bot.send_message(msg.chat.id, user_message)

    def available_letter(word: str) -> str:
        for i in word[::-1].lower():
            if i not in ('ь', 'ы', 'ъ', 'ё'):
                return i

    def compare_cities(all_cities, user_named, city, user_id) -> str:  # Compare user's city with
        # available and replying with a city, if possible
        if city == '':  # The only way of a blank city - is the beginning of a game
            bot_city = random.choice(all_cities)
            save_already_named(user_id, bot_city)
            return bot_city
        else:
            if city.capitalize() in all_cities and city not in user_named:
                result_set = set(all_cities)
                result_set.symmetric_difference_update(set(user_named))
                result_set.symmetric_difference_update(([city]))
                for each in result_set:
                    if each[0].lower() == available_letter(city):
                        bot_city = each
                        save_already_named(user_id, bot_city)
                        save_already_named(user_id, city)  # add to user's named
                        return bot_city  # If we found corresponding city
                return '1'  # If not - user wins
            return bot.get_state(user_id)

    def save_already_named(user_id, bot_city):  # saving city that is already used for this user
        try:
            with open(f'./users/{user_id}', 'a', newline='', encoding='utf-8') as f:
                f.writelines(f'{bot_city}\r\n')
        except (FileNotFoundError, IOError) as e:
            print(e)
            bot.send_message(user_id, 'Critical error. '
                                      'Please, start the game again')

    def play_cities(user_id, city) -> str:  # Choosing available cities
        all_cities, user_named = read_cities(user_id)
        bot_city = compare_cities(all_cities, user_named, city, user_id)
        return bot_city

    @bot.message_handler(commands=['cities_stop', 'города_стоп'])
    def stop_game_of_cities(msg):
        try:
            bot.delete_state(msg.chat.id)
            os.remove(f'./users/{msg.chat.id}')
            bot.send_message(msg.chat.id, 'If you stop the game - I won)')
        except (FileNotFoundError, FileExistsError, OSError) as e:
            print(e)
            bot.send_message(msg.chat.id, 'Something goes wrong, try later'
                                              ' or contact support, please')

    @bot.message_handler(commands=['wordcount', 'wc'])
    def word_count(msg):
        args = telebot.util.extract_arguments(msg.text)
        if args:
            res = args.strip().split()
            for each in res:
                if not each.isalpha():
                    bot.send_message(msg.chat.id,
                                     f'Input some WORDS, not numbers')
                    break
                else:
                    bot.send_message(msg.chat.id, f'{len(res)} words')
        else:
            bot.send_message(msg.chat.id, 'Input some words after command')

    @bot.message_handler(commands=['full_moon', 'next_full_moon', 'moon'])
    def next_full_moon(msg):
        args = telebot.util.extract_arguments(msg.text)
        next_moon = f'Next full moon based on today will be on '+\
                    str(
                        ephem.next_full_moon(
                            datetime.datetime.today()
                        )
                    )
        if args:
            res = args.strip().split()[0]
            if re.match(r'(0?[1-9]|[12][0-9]|3[01])[\-]'
                        r'(0?[1-9]|1[012])[\-]([12][0-9]+)', res):
                try:
                    res = datetime.datetime.strptime(res, '%d-%m-%Y')
                    next_moon = f'Next full moon based on {res} will be on ' +\
                                str(
                                    ephem.next_full_moon(
                                        res
                                    )
                                )
                except (ValueError, KeyError) as e:
                    print(e)
                    next_moon += "\nPlease input ONLY " \
                                 "date using format dd-mm-yyyy"
            else:
                next_moon += "\nPlease input date using format dd-mm-yyyy"
        bot.send_message(msg.chat.id, next_moon)

    @bot.message_handler(commands=['/named_cities'])
    def named_cities(msg):
        _, my_list = read_cities(msg.chat.id)
        bot.send_message(msg.chat.id, ', '.join(my_list))

    @bot.message_handler(content_types=['text'])
    def main_reply(msg):
        if os.path.isfile(f'./users/{msg.chat.id}'):
            game_of_cities(msg)
        else:
            bot.send_message(msg.chat.id,
                             f'Available commands are: '
                             f'\n/wordcount /wc counting words put '
                             f'after the command'
                             f'\n/next_full_moon /next_moon /moon'
                             f' - put a date dd-mm-yyyy after the comand to'
                             f' see the next full moon date'
                             f'\n/cities /города - the cities game'
                             f'\n/named_cities - the list of cities which have'
                             f' been already named'
                             f'\n/cities_stop /города_стоп - stop playing')
    try:
        bot.infinity_polling(allowed_updates=['chat_member',
                                              'my_chat_member',
                                              'message'])
    except KeyboardInterrupt:
        bot.stop_polling()


if __name__ == '__main__':
    main()