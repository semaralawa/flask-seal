from main import mysql

from flask import (
    Blueprint, redirect, render_template, request, url_for
)

# create blueprint
bp = Blueprint('home', __name__, url_prefix='/')


# homepage router
@bp.route('/home', methods=('GET', 'POST'))
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM blogs")
    data = cursor.fetchall()
    return render_template('home.html', datas=data)


# add data router
@bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO blogs (user_id, title, description, image) 
                            VALUES (%s, %s, %s, %s)''',
                       (user_id, title, description, image))
        mysql.connection.commit()
        print('add data success')
        return redirect(url_for('home.home'))


# edit data router
@bp.route('/edit/<id>', methods=('GET', 'POST'))
def edit(id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        title = request.form['title']
        description = request.form['description']
        image = request.form['image']

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE `blogs` SET `user_id` = %s, `title` = %s, `description` = %s, 
                            `image` = %s WHERE `blogs`.`id` = %s''',
                       (user_id, title, description, image, id))
        mysql.connection.commit()
        print('edit data success')
        return redirect(url_for('home.home'))

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM blogs WHERE id=%s", (id))
    data = cursor.fetchall()
    return render_template('edit.html', datas=data)


# delete data router
@bp.route('/delete/<id>', methods=('GET', 'POST'))
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM blogs WHERE id=%s", (id))
    mysql.connection.commit()
    print('delete data success')
    return redirect(url_for('home.home'))
