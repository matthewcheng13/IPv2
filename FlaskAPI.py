import csv
import main
from flask import Flask, redirect, url_for, request, jsonify, render_template

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    names = name.split(',')
    value = main.multi_thread(names, main.threadForSingleAddress)
    kind = "Find All Info"
    #save(name)
    columns = ['Input','IP Address','Hostname','Pingable','Open Ports']
    return render_template('info.html', name=names, value=value, kind=kind, iterate=range(len(names)), columns=columns)

'''jsonify({'ip_address': nameData[0],
                    'hostname': nameData[1],
                    'pingable': nameData[2],
                    'open_ports': nameData[3]})'''


def save(name):
    csv_rows = main.threadForSingleAddress(name)
    header = ["Ip_Addresses", "Name", "Pingable", "Open Ports"]
    with open('data_generated_og.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(csv_rows)


@app.route('/ip_address_and_hostname/<name>')
def address(name):
    names = name.split(',')
    value = main.multi_thread(names, main.getNameAndAddress)
    kind = 'IP Address and Hostname Lookup'
    columns = ['Input', 'IP Address', 'Hostname']
    return render_template('info.html', name=names, value=value, kind=kind, iterate=range(len(names)), columns=columns)


@app.route('/check_pingable/<name>')
def do_ping(name):
    names = name.split(',')
    value = main.multi_thread(names, main.pingable)
    kind = 'Check Pingability'
    columns = ['Input','Pingable']
    return render_template('info.html', name=names, value=value, kind=kind, iterate=range(len(names)), columns=columns)


@app.route('/check_open_ports/<name>')
def ports(name):
    names = name.split(',')
    value = main.multi_thread(names, main.check_ports)
    kind = 'Check Open Ports'
    columns = ['Input', 'Open Ports']
    return render_template('info.html', name=names, value=value, kind=kind, iterate=range(len(names)), columns=columns)


@app.route('/index', methods=['POST'])
def index():
    user = request.form['nm']
    if request.form.get('all'):
        return redirect(url_for('success', name=user))
    elif request.form.get('addr'):
        return redirect(url_for('address', name=user))
    elif request.form.get('ping'):
        return redirect(url_for('do_ping', name=user))
    else:
        return redirect(url_for('ports', name=user))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)