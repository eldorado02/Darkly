# 01 - Sensitive Data Exposure

## Walkthrough

1. Go to `/robots.txt` (explanation: file that tells crawlers which paths to avoid).
2. You will find two interesting paths:
   - `/.hidden`
   - `/whatever`
3. In `/whatever`, retrieve the `htpasswd` file.
4. The file contains the `root` username (used for `/admin`) and a hashed password.
5. Copy the hash and crack it with CrackStation (https://crackstation.net/).
6. Recovered password: `qwerty123@`.
7. Log in to `/admin` with:
   - Username: `root`
   - Password: `qwerty123@`
8. Once logged in, the flag is displayed.

## Screenshot
 
![Flag screenshot](root_flag.png)