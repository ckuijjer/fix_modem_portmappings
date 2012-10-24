#!/usr/bin/python

import socket
import mechanize

modem_ip = '192.168.1.1'

modem_url = 'http://%(modem_ip)s/scvrtsrv.cmd?action=a'

view_url = modem_url + '=view'
add_url = modem_url + '=add&srvName=%(server_ip)s&srvAddr=%(server_ip)s&proto=1,&eStart=%(port)s,&eEnd=%(port)s,&iStart=%(port)s,&iEnd=%(port)s'
remove_url = modem_url + '=remove&rmLst=%(server_ip_int)s|%(port)s|%(port)s|1|0|0|%(port)s|%(port)s,'

def get_ipaddress():
    return socket.gethostbyname(socket.gethostname())

def convert_ipaddress_to_int(ipaddress):
    return int(socket.inet_pton(socket.AF_INET, ipaddress).encode('hex'), 16)

if __name__ == '__main__':
    server_ip = get_ipaddress();
    server_ip_int = convert_ipaddress_to_int(server_ip)
    port = 80

    values = { 
        'modem_ip': modem_ip,
        'server_ip': server_ip,
        'server_ip_int': server_ip_int,
        'port': port,
    }

    print convert_ipaddress_to_int('192.168.1.22')
    print get_ipaddress()

    print values
    print add_url % values

    br = mechanize.Browser()
    br.add_password(modem_url % values, 'user', 'user')
    br.open(view_url % values)
    print br.response().read()
