from flask import Flask, render_template, request, url_for, redirect

from unit import EnemyUnit, PlayerUnit, BaseUnit
from classes import unit_classes
from equipment import Equipment
from arena import Arena

app = Flask(__name__)

heroes = {
    "player": BaseUnit,
    "enemy": None
}

arena = Arena()


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/choose-hero/', methods=['get', 'post'])
def choose_hero():
    if request.method == 'GET':
        header = 'Выберите героя'
        equipment = Equipment()
        weapons = equipment.get_weapon_names()
        armors = equipment.get_armor_names()
        result = {
            'header': header,
            'weapons': weapons,
            'armors': armors,
            'classes': unit_classes
        }
        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        name = request.form['name']
        weapon_name = request.form['weapon']
        armor_name = request.form['armor']
        unit_class_name = request.form['unit_class']

        if unit_class_name not in unit_classes:
            return "Такого класса не существует"

        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class_name))

        if weapon_name not in Equipment().get_weapon_names() or armor_name not in Equipment().get_armor_names():
            return "Такого оружия или брони не существует"

        player.create_armor(Equipment().get_armor(armor_name))
        player.create_weapon(Equipment().get_weapon(weapon_name))

    heroes['player'] = player
    return redirect(url_for('choose_enemy'))


@app.route('/choose-enemy/', methods=['get', 'post'])
def choose_enemy():
    if request.method == 'GET':
        header = 'Выберите противника'
        equipment = Equipment()
        weapons = equipment.get_weapon_names()
        armors = equipment.get_armor_names()
        result = {
            'header': header,
            'weapons': weapons,
            'armors': armors,
            'classes': unit_classes
        }
        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        name = request.form['name']
        weapon_name = request.form['weapon']
        armor_name = request.form['armor']
        unit_class_name = request.form['unit_class']

        if unit_class_name not in unit_classes:
            return "Такого класса не существует"

        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class_name))

        if weapon_name not in Equipment().get_weapon_names() or armor_name not in Equipment().get_armor_names():
            return "Такого оружия или брони не существует"

        enemy.create_armor(Equipment().get_armor(armor_name))
        enemy.create_weapon(Equipment().get_weapon(weapon_name))

    heroes['enemy'] = enemy
    return redirect(url_for('start_fight'))


@app.route('/fight/')
def start_fight():
    arena.start_game(player=heroes['player'], enemy=heroes['enemy'])
    return render_template('fight.html', heroes=heroes)


@app.route('/fight/hit/')
def hit():
    if arena.game_is_running:
        result = arena.player_hit()
    else:
        result = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route('/fight/use-skill/')
def use_skill():
    if arena.game_is_running:
        result = arena.player_use_skill()
    else:
        result = arena.battle_result
    return render_template('fight.html', heroes=heroes, result=result)


@app.route('/fight/pass-turn')
def pass_turn():
    if arena.game_is_running:
        result = arena.next_turn()
    else:
        result = arena.battle_result

    return render_template('fight.html', heroes=heroes, result=result)


@app.route('/fight/end-fight/')
def end_fight():
    return render_template('index.html', heroes=heroes)


if __name__ == '__main__':
    app.run()
