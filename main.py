from flask import Flask, render_template, request, redirect, url_for, session
from utils import query
# 创建flask对象
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gsolvit'


@app.route('/', methods=['GET', 'POST'])
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method=='GET':
        return render_template('admin_login.html')
    else:
        adminID = request.form.get('adminID')
        password = request.form.get('password')

        sql = "select * from Administrator where adminID = '%s'" % adminID
        result = query.query(sql)
        print(result)

        if len(result) != 0:
            if result[0][2] == password:
                session['adminID'] = result[0][1]
                session.permanent=True
                return redirect(url_for('admin'))
            else:
                return u'账号或密码错误'
        else:
            return u'不存在这个用户'


@app.route('/employee_login', methods=['GET', 'POST'])
def employee_login():
    if request.method=='GET':
        return render_template('employee_login.html')
    else:
        empID = request.form.get('empID')
        password = request.form.get('password')

        sql = "select * from employee where empID = '%s'" % empID
        result = query.query(sql)
        print(result)
        if len(result) != 0:
            if result[0][4] == password:
                session['empID'] = result[0][1]
                session.permanent=True
                return redirect(url_for('employee'))
            else:
                return u'账号或密码错误'
        else:
            return u'不存在这个用户'


@app.route('/audit_login', methods=['GET', 'POST'])
def audit_login():
    if request.method=='GET':
        return render_template('audit_login.html')
    else:
        auditID = request.form.get('auditID')
        password = request.form.get('password')

        sql = "select * from audit where auditID = '%s'" % auditID
        result = query.query(sql)
        print(result)
        if len(result) != 0:
            if result[0][4] == password:
                session['auditID'] = result[0][1]
                session.permanent=True
                return redirect(url_for('audit'))
            else:
                return u'账号或密码错误'
        else:
            return u'不存在这个用户'


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        sql = "select * from bills"
        result = query.query(sql);
        return render_template('admin_index.html', result=result)
    else:
        return redirect(url_for('admin_update'))


@app.route('/admin_update', methods=['GET', 'POST'])
def admin_update():
    if request.method == 'POST':
        billno = request.form.get('billno')
        sql = "select * from bills where billno = '%s'" % billno;

        print(sql)
        result = query.query(sql)
        print(result)
        if not result:
            return redirect(url_for('update_failed'))
        else:
            user = request.form.get('user')
            amount = request.form.get('amount')
            reason = request.form.get('reason')
            time = request.form.get('time')
            if len(user) != 0:
                sql = "select * from employee where empID = '%s'" % user
                print(sql)
                if not query.query(sql):
                    return redirect(url_for('update_failed'))
                sql = "update bills set user = '%s' where billno = '%s'" % (user, billno)
                query.query(sql)
            if len(amount) != 0:
                sql = "update bills set amount = '%s' where billno = '%s'" % (amount, billno)
                query.query(sql)
            if len(reason) != 0:
                sql = "update bills set reason = '%s' where billno = '%s'" % (reason, billno)
                query.query(sql)
            if len(time) != 0:
                sql = "update bills set time = '%s' where billno = '%s'" % (time, billno)
                query.query(sql)
            return redirect(url_for('update_successfully'))
    else:
        return render_template('admin_update.html')


@app.route('/update/failed', methods=['GET', 'POST'])
def update_failed():
    return render_template('update_failed.html')



@app.route('/update/successfully', methods=['GET', 'POST'])
def update_successfully():
    return render_template('update_successfully.html')



@app.route('/admin_delete', methods=['GET', 'POST'])
def admin_delete():
    if request.method == 'POST':
        billno = request.form.get('billno')
        user = request.form.get('user')
        amount = request.form.get('amount')
        reason = request.form.get('reason')
        time = request.form.get('time')
        
        sql = ""
        if len(time) != 0:
            sql = "select * from bills where billno = '%s' or user = '%s' or amount = '%s' or reason = '%s' or time = '%s'" % (billno, user, amount, reason, time)
        else:
            sql = "select * from bills where billno = '%s' or user = '%s' or amount = '%s' or reason = '%s'" % (billno, user, amount, reason)
        print(sql)
        result = query.query(sql)
        print(result)
        if not result:
            return redirect(url_for('delete_failed'))
        else:
            sql = "delete " + sql[8:]
            query.query(sql)
            return redirect(url_for('delete_successfully'))
    else:
        return render_template('admin_delete.html')


@app.route('/delete/successfully', methods=['GET', 'POST'])
def delete_successfully():
    return render_template('delete_successfully.html')


@app.route('/delete/failed', methods=['GET', 'POST'])
def delete_failed():
    return render_template('delete_failed.html')


# 关于我们
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)

