# **Automation script** 

1. **Go to main directory**
   ```bash
   cd ~
   ```
2. **Make or edit file .profile**

3. **Paste this code to the file**
   ```bash
   clear
   python3 {path}
   ```
4. **How to know path file**
   1. **Go to project directory**
   2. **Write this command**
   ```bash
   pwd
   ```
   3. **Copy path**
   4. **Past path to .profile file**
5. **Result**
   ```
   clear 
   python3 /data/data/com.termux/files/home/scripts/SunsTerm/main.py
   ```

# **Secure Shell Allies**

1. **Go to ssh directoy**
   ```bash
   cd .ssh
   ```
2. **Make config file (if it not exists)**
    ```bash
    touch config
    ```
3. **Open it (nvim or nano)**
    ```bash
    nvim config
    ```
4. **Write teamplate**
   ```bash
    Host {name}
        Hostname {ip}
        User {user}
        IdentityFile {key_path}
        ForwardAgent yes
   ```
    **Usage**


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name SSH Alies  |
| `ip`      | `string` | **Required**. Host ip address |
| `keypath`      | `string` | **Required**. Path to you ssh key |
| `user`      | `string` | **Required**. User when you join |


## Authors

- [@TheDmitryY](https://www.github.com/TheDmitryY)

## Using

- [TacleApi](https://github.com/TheDmitryY/tacle-api)

## Feedback

If you have any feedback, please reach out to us at telegram: [trusres](https://t.me/trusres)